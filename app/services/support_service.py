from app.chains.classification_chain import classification_chain
from app.chains.response_chain import response_chain
from app.guardrails.input_validation import validate_input_length
from app.guardrails.pii_redaction import redact_email_addresses
from app.schemas.support_schema import SupportClassification


def classify_support_query(
    customer_query: str
) -> SupportClassification:
    validated_query = validate_input_length(customer_query)
    redacted_query = redact_email_addresses(validated_query)

    result = classification_chain.invoke(
        {
            "customer_query": redacted_query
        }
    )

    return result

def generate_support_response(
    customer_query: str,
    classification: SupportClassification
) -> str:
    validated_query = validate_input_length(customer_query)
    redacted_query = redact_email_addresses(validated_query)

    response = response_chain.invoke(
        {
            "customer_query": redacted_query,
            "category": classification.category,
            "priority": classification.priority
        }
    )

    return response
