"""Existing regression suite of the RoomBook team (written by hand).

It covers the main happy paths and a few error paths. It does not claim to be complete.
"""


def test_create_booking_returns_201_and_the_booking(book):
    response = book("u-ana", "2025-03-05T09:00", "2025-03-05T10:00")
    assert response.status_code == 201
    created = response.json()
    assert len(created) == 1
    assert created[0]["room_id"] == "R2"
    assert created[0]["user_id"] == "u-ana"
    assert created[0]["status"] == "active"


def test_create_booking_in_unknown_room_returns_404(book):
    response = book("u-ana", "2025-03-05T09:00", "2025-03-05T10:00", room_id="R9")
    assert response.status_code == 404
    assert response.json()["error"] == "unknown_room"


def test_create_booking_over_capacity_is_rejected(book):
    response = book("u-ana", "2025-03-05T09:00", "2025-03-05T10:00", room_id="R1", attendees=9)
    assert response.status_code == 400
    assert response.json()["error"] == "capacity_exceeded"


def test_overlapping_booking_is_rejected(book):
    assert book("u-ana", "2025-03-05T09:00", "2025-03-05T11:00").status_code == 201
    response = book("u-ben", "2025-03-05T10:00", "2025-03-05T12:00")
    assert response.status_code == 409
    assert response.json()["error"] == "slot_conflict"


def test_missing_user_header_returns_401(client):
    response = client.get("/rooms")
    assert response.status_code == 401


def test_get_own_booking(client, book, as_ana):
    booking_id = book("u-ana", "2025-03-05T09:00", "2025-03-05T10:00").json()[0]["id"]
    response = client.get(f"/bookings/{booking_id}", headers=as_ana)
    assert response.status_code == 200
    assert response.json()["id"] == booking_id


def test_member_cannot_read_someone_elses_booking(client, book, as_ben):
    booking_id = book("u-ana", "2025-03-05T09:00", "2025-03-05T10:00").json()[0]["id"]
    assert client.get(f"/bookings/{booking_id}", headers=as_ben).status_code == 403


def test_owner_can_cancel_with_plenty_of_notice(client, book, as_ana):
    booking_id = book("u-ana", "2025-03-10T09:00", "2025-03-10T10:00").json()[0]["id"]
    response = client.delete(f"/bookings/{booking_id}", headers=as_ana)
    assert response.status_code == 200
    assert response.json()["status"] == "cancelled"


def test_member_cannot_cancel_someone_elses_booking(client, book, as_ben):
    booking_id = book("u-ana", "2025-03-10T09:00", "2025-03-10T10:00").json()[0]["id"]
    response = client.delete(f"/bookings/{booking_id}", headers=as_ben)
    assert response.status_code == 403


def test_list_bookings_shows_only_own_bookings_to_a_member(client, book, as_ana):
    book("u-ana", "2025-03-05T09:00", "2025-03-05T10:00")
    book("u-ben", "2025-03-05T11:00", "2025-03-05T12:00")
    response = client.get("/bookings", headers=as_ana)
    assert [b["user_id"] for b in response.json()] == ["u-ana"]


def test_availability_of_an_empty_day_is_the_full_opening_hours(client, as_ana):
    response = client.get("/rooms/R2/availability", params={"date": "2025-03-05"}, headers=as_ana)
    assert response.status_code == 200
    assert response.json() == [{"start": "2025-03-05T08:00", "end": "2025-03-05T20:00"}]
