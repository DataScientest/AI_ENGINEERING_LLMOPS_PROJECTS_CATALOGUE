from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from roombook.api import create_app

# Fixed "now" for every test: Monday 3 March 2025, 10:00 (site local time).
NOW = datetime(2025, 3, 3, 10, 0)


class Clock:
    def __init__(self, now: datetime = NOW):
        self.now = now

    def __call__(self) -> datetime:
        return self.now


@pytest.fixture
def clock() -> Clock:
    return Clock()


@pytest.fixture
def client(clock) -> TestClient:
    return TestClient(create_app(clock))


def headers(user_id: str) -> dict:
    return {"X-User-Id": user_id}


@pytest.fixture
def as_ana():
    return headers("u-ana")


@pytest.fixture
def as_ben():
    return headers("u-ben")


@pytest.fixture
def as_cleo():
    return headers("u-cleo")


@pytest.fixture
def book(client):
    """Create a booking and return the HTTP response. Defaults: room R2, 5 attendees."""

    def _book(user: str, start: str, end: str, room_id: str = "R2", attendees: int = 5, **extra):
        body = {"room_id": room_id, "start": start, "end": end, "attendees": attendees, **extra}
        return client.post("/bookings", json=body, headers=headers(user))

    return _book
