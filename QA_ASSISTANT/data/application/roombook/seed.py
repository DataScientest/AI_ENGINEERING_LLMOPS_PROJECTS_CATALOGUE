"""Reference data loaded at startup. See data/source_documents/application_documentation.md."""

ROOMS = {
    "R1": {"id": "R1", "name": "Alpha", "capacity": 4},
    "R2": {"id": "R2", "name": "Beta", "capacity": 8},
    "R3": {"id": "R3", "name": "Gamma", "capacity": 12},
}

USERS = {
    "u-ana": {"id": "u-ana", "name": "Ana", "role": "member"},
    "u-ben": {"id": "u-ben", "name": "Ben", "role": "member"},
    "u-cleo": {"id": "u-cleo", "name": "Cleo", "role": "manager"},
}
