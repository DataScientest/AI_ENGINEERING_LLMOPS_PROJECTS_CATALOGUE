from __future__ import annotations

from datetime import date, datetime
from typing import Callable

from fastapi import FastAPI, Header, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .errors import DomainError
from .seed import ROOMS
from .service import BookingService


class BookingIn(BaseModel):
    room_id: str
    start: datetime
    end: datetime
    attendees: int
    occurrences: int = 1
    user_id: str | None = None  # managers only: book on behalf of this user


class BookingPatch(BaseModel):
    start: datetime | None = None
    end: datetime | None = None
    attendees: int | None = None


def _view(b: dict) -> dict:
    return {
        "id": b["id"], "room_id": b["room_id"], "user_id": b["user_id"],
        "start": b["start"].isoformat(timespec="minutes"),
        "end": b["end"].isoformat(timespec="minutes"),
        "attendees": b["attendees"], "status": b["status"],
    }


def create_app(clock: Callable[[], datetime] = datetime.now) -> FastAPI:
    app = FastAPI(title="RoomBook", version="1.0.0")
    service = BookingService(clock)

    @app.exception_handler(DomainError)
    async def domain_error_handler(_: Request, exc: DomainError):
        return JSONResponse(status_code=exc.status_code, content={"error": exc.code, "message": exc.message})

    @app.exception_handler(RequestValidationError)
    async def validation_handler(_: Request, exc: RequestValidationError):
        return JSONResponse(status_code=422, content={"error": "malformed_request", "message": "Malformed request"})

    def who(x_user_id: str | None) -> str:
        if not x_user_id:
            raise DomainError(401, "unknown_user", "Missing X-User-Id header")
        return x_user_id

    @app.get("/rooms")
    def list_rooms(x_user_id: str | None = Header(default=None)):
        service._user(who(x_user_id))
        return list(ROOMS.values())

    @app.get("/rooms/{room_id}/availability")
    def availability(room_id: str, day: date = Query(alias="date"), x_user_id: str | None = Header(default=None)):
        free = service.availability(who(x_user_id), room_id, day)
        return [{"start": s.isoformat(timespec="minutes"), "end": e.isoformat(timespec="minutes")} for s, e in free]

    @app.post("/bookings", status_code=201)
    def create_booking(body: BookingIn, x_user_id: str | None = Header(default=None)):
        created = service.create(who(x_user_id), body.room_id, body.start, body.end,
                                 body.attendees, body.occurrences, body.user_id)
        return [_view(b) for b in created]

    @app.get("/bookings")
    def list_bookings(room_id: str | None = None, day: date | None = Query(default=None, alias="date"),
                      include_cancelled: bool = False, x_user_id: str | None = Header(default=None)):
        return [_view(b) for b in service.list(who(x_user_id), room_id, day, include_cancelled)]

    @app.get("/bookings/{booking_id}")
    def get_booking(booking_id: str, x_user_id: str | None = Header(default=None)):
        return _view(service.get(who(x_user_id), booking_id))

    @app.patch("/bookings/{booking_id}")
    def reschedule_booking(booking_id: str, body: BookingPatch, x_user_id: str | None = Header(default=None)):
        return _view(service.reschedule(who(x_user_id), booking_id, body.start, body.end, body.attendees))

    @app.delete("/bookings/{booking_id}")
    def cancel_booking(booking_id: str, x_user_id: str | None = Header(default=None)):
        return _view(service.cancel(who(x_user_id), booking_id))

    return app


app = create_app()
