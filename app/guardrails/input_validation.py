from app.config.settings import MAX_CUSTOMER_QUERY_LENGTH


class InputLengthExceededError(ValueError):
    """Raised when a customer query exceeds the configured length limit."""


def validate_input_length(customer_query: str) -> str:
    """Return the query unchanged when it is within the allowed length."""

    actual_length = len(customer_query)

    if actual_length > MAX_CUSTOMER_QUERY_LENGTH:
        raise InputLengthExceededError(
            "Customer query is too long. "
            f"Maximum length is {MAX_CUSTOMER_QUERY_LENGTH} characters; "
            f"received {actual_length}."
        )

    return customer_query
