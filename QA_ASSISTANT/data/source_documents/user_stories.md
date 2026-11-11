# User stories

Stories of the current backlog. Ids match `data/tabular_data/tickets.csv`. Criterion ids are written `AC-<story>-<n>`.

## RB-101: Book a room

As a member, I want to book a free room for a time slot so that I have a place to meet.

- AC-101-1: A member can book a free room with a start and an end on a 30-minute grid. The response is `201` with the booking.
- AC-101-2: A booking lasts at least 30 minutes and at most 4 hours.
- AC-101-3: A booking is inside opening hours, 08:00 to 20:00. A booking ending at 20:00 is allowed.
- AC-101-4: A booking must start in the future.

## RB-102: No double booking

As a member, I want a room never to be booked twice at the same time so that nobody finds their room taken.

- AC-102-1: Two active bookings of the same room cannot overlap.
- AC-102-2: A booking can start exactly when another one ends in the same room.
- AC-102-3: Bookings in different rooms do not conflict.

## RB-103: Respect room capacity

As a facility manager, I want bookings to respect the room capacity so that rooms are not overcrowded.

- AC-103-1: The number of attendees is at least 1 and at most the capacity of the room.
- AC-103-2: A booking with exactly as many attendees as the capacity is accepted.

## RB-104: Cancel a booking

As a member, I want to cancel my booking so that the room can be used by someone else.

- AC-104-1: A member can cancel their own booking up to 24 hours before its start.
- AC-104-2: Within 24 hours of the start, a member cannot cancel.
- AC-104-3: A cancelled booking keeps its record with status `cancelled`.
- AC-104-4: Cancelling a booking that is already cancelled is refused.

## RB-105: Release cancelled slots

As a member, I want a cancelled slot to be bookable again so that rooms are not wasted.

- AC-105-1: After a cancellation, the same room and slot can be booked again.
- AC-105-2: The availability of the room shows the released slot as free.

## RB-106: Manager privileges

As a manager, I want to manage bookings for the whole site.

- AC-106-1: A manager can cancel any booking at any time.
- AC-106-2: A manager can create a booking on behalf of a member.
- AC-106-3: A member cannot create a booking on behalf of someone else.

## RB-107: Booking visibility

As a member, I want my bookings to be private so that my schedule is not exposed.

- AC-107-1: A member can read and list only their own bookings.
- AC-107-2: A member reading another member's booking is refused.
- AC-107-3: A manager can read and list all bookings.

## RB-108: Weekly recurring bookings

As a member, I want to book the same slot for several weeks in one go.

- AC-108-1: A booking can be repeated weekly for 1 to 8 occurrences.
- AC-108-2: All occurrences share the weekday, times, room and attendees.
- AC-108-3: If one occurrence cannot be booked, no occurrence is created.
- AC-108-4: More than 8 occurrences is refused.

## RB-109: Booking quota

As a facility manager, I want to limit how many future bookings a member holds so that rooms are shared fairly.

- AC-109-1: A member can hold at most 5 active future bookings.
- AC-109-2: Each occurrence of a recurring booking counts toward the quota.
- AC-109-3: Cancelled bookings do not count toward the quota.
- AC-109-4: Managers have no quota.

## RB-110: Reschedule a booking

As a member, I want to move my booking instead of cancelling and rebooking.

- AC-110-1: The owner can change start, end and attendees.
- AC-110-2: The new values follow the same rules as a new booking.
- AC-110-3: A booking does not conflict with itself when moved.
- AC-110-4: A member must respect the 24-hour notice before the current start.

## RB-111: Room availability

As a member, I want to see when a room is free on a given day.

- AC-111-1: The availability lists the free windows inside opening hours, in order.
- AC-111-2: Booked periods are not part of the free windows.
- AC-111-3: Cancelled bookings do not reduce availability.

## RB-112: Flexible cancellation for loyal members

As a loyal member, I want a more flexible cancellation policy.

- AC-112-1: Loyal members get better cancellation conditions.

## RB-113: Limit bookings too far ahead

As a facility manager, I do not want members to block rooms too far in advance.

- AC-113-1: Bookings cannot be made too far in the future.

## RB-114: Deal with no-shows

As a facility manager, I want to deal with members who book a room and do not use it.

- AC-114-1: No-shows are handled.
