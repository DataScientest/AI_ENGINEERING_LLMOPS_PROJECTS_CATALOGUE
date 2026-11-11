class DomainError(Exception):
    """A business rule violation, mapped to an HTTP status and a stable error code."""

    def __init__(self, status_code: int, code: str, message: str = ""):
        super().__init__(message or code)
        self.status_code = status_code
        self.code = code
        self.message = message or code
