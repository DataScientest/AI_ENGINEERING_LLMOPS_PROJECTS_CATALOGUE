# RoomBook: system under test

A small in-memory meeting-room booking service (Python, FastAPI) and its existing automated test suite.

## Run the tests

```bash
cd data/application
python -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
pytest
```

All tests pass on this version.

## Run the service

```bash
uvicorn roombook.api:app --reload
```

Interactive documentation: `http://127.0.0.1:8000/docs`. Every request needs the header `X-User-Id` (`u-ana`, `u-ben` or `u-cleo`).

## Layout

- `roombook/service.py`: business rules.
- `roombook/api.py`: HTTP layer.
- `roombook/seed.py`: rooms and users.
- `tests/conftest.py`: shared fixtures (fixed clock, authenticated headers, a `book` helper).
- `tests/test_bookings.py`: the existing suite.

The expected behaviour is described in `data/source_documents/application_documentation.md`.
