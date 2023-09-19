class AccessDenied(Exception):
    """Exception raised when user is not allowed to access a resource."""

    def __init__(self, message: str = "Access denied") -> None:
        """Initializes a new instance of exception with default message."""
        super().__init__(message)
