import re


EMAIL_REDACTION_TOKEN = "[EMAIL_REDACTED]"

EMAIL_PATTERN = re.compile(
    r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
    re.IGNORECASE,
)


def redact_email_addresses(customer_query: str) -> str:
    """Replace email addresses with a stable redaction token."""

    return EMAIL_PATTERN.sub(EMAIL_REDACTION_TOKEN, customer_query)
