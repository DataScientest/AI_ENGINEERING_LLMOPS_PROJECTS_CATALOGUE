# RoomBook: functional documentation

RoomBook is the internal meeting-room booking service of Hub42, a coworking operator. This document describes the behaviour the service is expected to have. It is the reference for what a correct result is. The source code is in `data/application/`.

## Conventions

- All times are local to the site, written as ISO 8601 without time zone (`2025-03-05T09:00`). There is no time-zone handling.
- A booking has a start, an end, a room, an owner, a number of attendees and a status (`active` or `cancelled`).
- An interval is half-open: a booking from 09:00 to 10:00 occupies the room from 09:00 up to, but not including, 10:00. Another booking can start at 10:00.
- Identity is given by the header `X-User-Id`. A missing or unknown user returns `401 unknown_user`.
- Errors return a JSON body `{"error": "<code>", "message": "<text>"}`. The codes are stable.

## Reference data

| Rooms | Name | Capacity |
| --- | --- | --- |
| `R1` | Alpha | 4 |
| `R2` | Beta | 8 |
| `R3` | Gamma | 12 |

| Users | Role |
| --- | --- |
| `u-ana` | member |
| `u-ben` | member |
| `u-cleo` | manager |

## Business rules

### Booking time rules

- Start and end are on a 30-minute grid (minutes `00` or `30`, no seconds). Otherwise `400 invalid_time`.
- The end is after the start, on the same day. Otherwise `400 invalid_time`.
- The start is strictly after the current time. Otherwise `400 in_the_past`.
- The duration is at least 30 minutes and at most 4 hours, both included. Otherwise `400 duration_out_of_range`.
- The room is open from 08:00 to 20:00. A booking must start at or after 08:00 and end at or before 20:00. Otherwise `400 outside_opening_hours`.
- The rules are checked in the order above.

### Capacity

The number of attendees is between 1 and the room capacity, both included. Otherwise `400 capacity_exceeded`.

### Conflicts

Two active bookings of the same room cannot overlap. A new booking that overlaps one returns `409 slot_conflict`. Cancelled bookings do not block a slot. Bookings in different rooms never conflict.

### Cancellation and rescheduling notice

- A member can cancel or reschedule their own booking only if its current start is at least 24 hours from now (exactly 24 hours is allowed). Otherwise `409 cancellation_too_late`.
- A manager can cancel or reschedule any booking at any time.
- Cancelling an already cancelled booking returns `409 already_cancelled`. A cancelled booking cannot be rescheduled (`409 already_cancelled`).
- Cancelling keeps the booking with status `cancelled`.

### Roles and visibility

- A member can read, list, reschedule and cancel only their own bookings. Acting on another member's booking returns `403 forbidden`.
- A manager can act on every booking.
- A manager can create a booking on behalf of a user by passing `user_id`. A member passing a `user_id` other than their own gets `403 forbidden`.

### Weekly recurrence

- `occurrences` is an integer from 1 to 8 (default 1). The booking is repeated every week, same weekday, same times, same room, same attendees. Otherwise `400 invalid_recurrence`.
- It is all or nothing: if any occurrence breaks a rule (time rules, conflict, quota), no booking is created and the error of the first failing occurrence is returned.

### Quota

A member can hold at most 5 active bookings that start in the future. A booking that would bring the member above 5 returns `409 quota_exceeded`. Each occurrence of a recurring booking counts. Cancelled bookings and bookings that have already started do not count. Managers have no quota.

### Rescheduling

`PATCH /bookings/{id}` can change `start`, `end` and `attendees`. The same time rules, capacity rule and conflict rule as for creation apply. A booking never conflicts with itself.

### Availability

`GET /rooms/{id}/availability?date=YYYY-MM-DD` returns the free windows of that room on that day, inside opening hours 08:00-20:00, in chronological order, with adjacent free windows merged. Active bookings are excluded. Windows are not trimmed to the current time.

## Endpoints

| Method and path | Purpose | Success |
| --- | --- | --- |
| `GET /rooms` | List rooms | `200` |
| `GET /rooms/{room_id}/availability?date=` | Free windows of a room for a day | `200` |
| `POST /bookings` | Create one booking or a weekly series. The body has `room_id`, `start`, `end`, `attendees`, optional `occurrences`, optional `user_id`. Always returns a list of bookings | `201` |
| `GET /bookings` | List bookings. Filters: `room_id`, `date`, `include_cancelled` (default false). Sorted by start, then id | `200` |
| `GET /bookings/{id}` | Read a booking | `200` |
| `PATCH /bookings/{id}` | Reschedule | `200` |
| `DELETE /bookings/{id}` | Cancel | `200` |

An unknown room returns `404 unknown_room`, an unknown booking `404 unknown_booking`. A malformed body or parameter returns `422 malformed_request`.

## Error codes

`unknown_user` (401), `forbidden` (403), `unknown_room` (404), `unknown_booking` (404), `invalid_time`, `in_the_past`, `duration_out_of_range`, `outside_opening_hours`, `capacity_exceeded`, `invalid_recurrence` (400), `slot_conflict`, `cancellation_too_late`, `already_cancelled`, `quota_exceeded` (409), `malformed_request` (422).
