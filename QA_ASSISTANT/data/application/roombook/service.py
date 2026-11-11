from __future__ import annotations

from datetime import datetime, time, timedelta
from itertools import count
from typing import Callable

from .errors import DomainError
from .seed import ROOMS, USERS

OPENING = time(8, 0)
CLOSING = time(20, 0)
SLOT_MINUTES = 30
MIN_DURATION = timedelta(minutes=30)
MAX_DURATION = timedelta(hours=4)
CANCELLATION_NOTICE = timedelta(hours=24)
MAX_ACTIVE_FUTURE_BOOKINGS = 5
MAX_OCCURRENCES = 8


class BookingService:
    def __init__(self, clock: Callable[[], datetime] = datetime.now):
        self.clock = clock
        self._bookings: dict[str, dict] = {}
        self._ids = count(1)

    # ---------- helpers ----------
    def _user(self, user_id: str) -> dict:
        user = USERS.get(user_id)
        if user is None:
            raise DomainError(401, "unknown_user", "Unknown user")
        return user

    def _room(self, room_id: str) -> dict:
        room = ROOMS.get(room_id)
        if room is None:
            raise DomainError(404, "unknown_room", "Unknown room")
        return room

    def _booking(self, booking_id: str) -> dict:
        booking = self._bookings.get(booking_id)
        if booking is None:
            raise DomainError(404, "unknown_booking", "Unknown booking")
        return booking

    @staticmethod
    def _is_manager(user: dict) -> bool:
        return user["role"] == "manager"

    def _check_time_rules(self, start: datetime, end: datetime) -> None:
        if start.minute % SLOT_MINUTES != 0 or end.minute % SLOT_MINUTES != 0 or start.second or end.second:
            raise DomainError(400, "invalid_time", "Times must be on a 30-minute grid")
        if end <= start or start.date() != end.date():
            raise DomainError(400, "invalid_time", "End must be after start, on the same day")
        if start <= self.clock():
            raise DomainError(400, "in_the_past", "Start must be in the future")
        duration = end - start
        if duration < MIN_DURATION or duration > MAX_DURATION:
            raise DomainError(400, "duration_out_of_range", "Duration must be 30 minutes to 4 hours")
        if start.time() < OPENING or end.time() > CLOSING:
            raise DomainError(400, "outside_opening_hours", "Bookings must be within 08:00-20:00")

    @staticmethod
    def _overlaps(a_start: datetime, a_end: datetime, b_start: datetime, b_end: datetime) -> bool:
        return a_start < b_end and b_start < a_end

    def _check_free(self, room_id: str, start: datetime, end: datetime, ignore_id: str | None = None) -> None:
        for b in self._bookings.values():
            if b["status"] != "active" or b["room_id"] != room_id or b["id"] == ignore_id:
                continue
            if self._overlaps(start, end, b["start"], b["end"]):
                raise DomainError(409, "slot_conflict", "The room is already booked for this slot")

    def _active_future_count(self, user_id: str) -> int:
        now = self.clock()
        return sum(
            1 for b in self._bookings.values()
            if b["user_id"] == user_id and b["status"] == "active" and b["start"] > now
        )

    def _check_notice(self, user: dict, booking: dict) -> None:
        if self._is_manager(user):
            return
        if booking["start"] - self.clock() < CANCELLATION_NOTICE:
            raise DomainError(409, "cancellation_too_late", "Less than 24 hours before the start")

    def _check_access(self, user: dict, booking: dict) -> None:
        if booking["user_id"] != user["id"] and not self._is_manager(user):
            raise DomainError(403, "forbidden", "Not allowed on this booking")

    # ---------- operations ----------
    def create(self, acting_user_id: str, room_id: str, start: datetime, end: datetime,
               attendees: int, occurrences: int = 1, on_behalf_of: str | None = None) -> list[dict]:
        actor = self._user(acting_user_id)
        owner = actor
        if on_behalf_of and on_behalf_of != actor["id"]:
            if not self._is_manager(actor):
                raise DomainError(403, "forbidden", "Only managers can book on behalf of others")
            owner = self._user(on_behalf_of)
        room = self._room(room_id)
        if occurrences < 1 or occurrences > MAX_OCCURRENCES:
            raise DomainError(400, "invalid_recurrence", "Occurrences must be between 1 and 8")
        if attendees < 1 or attendees > room["capacity"]:
            raise DomainError(400, "capacity_exceeded", "Attendees must be between 1 and the room capacity")
        slots = [(start + timedelta(weeks=i), end + timedelta(weeks=i)) for i in range(occurrences)]
        for s, e in slots:
            self._check_time_rules(s, e)
        for s, e in slots:
            self._check_free(room_id, s, e)
        if not self._is_manager(owner):
            if self._active_future_count(owner["id"]) + occurrences > MAX_ACTIVE_FUTURE_BOOKINGS:
                raise DomainError(409, "quota_exceeded", "Members can hold at most 5 active future bookings")
        created = []
        for s, e in slots:
            booking_id = f"B{next(self._ids)}"
            booking = {
                "id": booking_id, "room_id": room_id, "user_id": owner["id"],
                "start": s, "end": e, "attendees": attendees, "status": "active",
            }
            self._bookings[booking_id] = booking
            created.append(booking)
        return created

    def get(self, acting_user_id: str, booking_id: str) -> dict:
        user = self._user(acting_user_id)
        booking = self._booking(booking_id)
        self._check_access(user, booking)
        return booking

    def list(self, acting_user_id: str, room_id: str | None = None, date_=None,
             include_cancelled: bool = False) -> list[dict]:
        user = self._user(acting_user_id)
        if room_id is not None:
            self._room(room_id)
        result = []
        for b in self._bookings.values():
            if not self._is_manager(user) and b["user_id"] != user["id"]:
                continue
            if room_id is not None and b["room_id"] != room_id:
                continue
            if date_ is not None and b["start"].date() != date_:
                continue
            if b["status"] != "active" and not include_cancelled:
                continue
            result.append(b)
        return sorted(result, key=lambda b: (b["start"], b["id"]))

    def reschedule(self, acting_user_id: str, booking_id: str, start: datetime | None = None,
                   end: datetime | None = None, attendees: int | None = None) -> dict:
        user = self._user(acting_user_id)
        booking = self._booking(booking_id)
        self._check_access(user, booking)
        if booking["status"] != "active":
            raise DomainError(409, "already_cancelled", "The booking is cancelled")
        self._check_notice(user, booking)
        new_start = start or booking["start"]
        new_end = end or booking["end"]
        new_attendees = attendees if attendees is not None else booking["attendees"]
        room = self._room(booking["room_id"])
        if new_attendees < 1 or new_attendees > room["capacity"]:
            raise DomainError(400, "capacity_exceeded", "Attendees must be between 1 and the room capacity")
        self._check_time_rules(new_start, new_end)
        self._check_free(booking["room_id"], new_start, new_end, ignore_id=booking["id"])
        booking.update(start=new_start, end=new_end, attendees=new_attendees)
        return booking

    def cancel(self, acting_user_id: str, booking_id: str) -> dict:
        user = self._user(acting_user_id)
        booking = self._booking(booking_id)
        self._check_access(user, booking)
        if booking["status"] != "active":
            raise DomainError(409, "already_cancelled", "The booking is already cancelled")
        self._check_notice(user, booking)
        booking["status"] = "cancelled"
        return booking

    def availability(self, acting_user_id: str, room_id: str, day) -> list[tuple[datetime, datetime]]:
        self._user(acting_user_id)
        self._room(room_id)
        cursor = datetime.combine(day, OPENING)
        closing = datetime.combine(day, CLOSING)
        busy = sorted(
            (b["start"], b["end"]) for b in self._bookings.values()
            if b["status"] == "active" and b["room_id"] == room_id and b["start"].date() == day
        )
        free = []
        for b_start, b_end in busy:
            if b_start > cursor:
                free.append((cursor, b_start))
            cursor = max(cursor, b_end)
        if cursor < closing:
            free.append((cursor, closing))
        return free
