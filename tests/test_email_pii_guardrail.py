import unittest
from unittest.mock import patch

from app.guardrails.pii_redaction import (
    EMAIL_REDACTION_TOKEN,
    redact_email_addresses,
)
from app.schemas.support_schema import SupportClassification


class EmailPiiGuardrailTests(unittest.TestCase):
    def test_email_is_redacted(self):
        query = "Please update the account for customer@example.com."

        result = redact_email_addresses(query)

        self.assertEqual(
            result,
            f"Please update the account for {EMAIL_REDACTION_TOKEN}.",
        )

    def test_query_without_email_is_unchanged(self):
        query = "I cannot access my account."

        result = redact_email_addresses(query)

        self.assertEqual(result, query)

    def test_multiple_emails_are_redacted(self):
        query = "Move access from old@example.com to new@example.org."

        result = redact_email_addresses(query)

        self.assertEqual(result.count(EMAIL_REDACTION_TOKEN), 2)
        self.assertNotIn("old@example.com", result)
        self.assertNotIn("new@example.org", result)

    @patch("app.services.support_service.classification_chain")
    def test_classification_chain_receives_redacted_email(self, mock_chain):
        from app.services.support_service import classify_support_query

        classify_support_query("My login email is customer@example.com")

        mock_chain.invoke.assert_called_once_with(
            {
                "customer_query": (
                    f"My login email is {EMAIL_REDACTION_TOKEN}"
                )
            }
        )

    @patch("app.services.support_service.response_chain")
    def test_response_chain_receives_redacted_email(self, mock_chain):
        from app.services.support_service import generate_support_response

        classification = SupportClassification(
            category="account",
            priority="low",
        )

        generate_support_response(
            "My login email is customer@example.com",
            classification,
        )

        mock_chain.invoke.assert_called_once_with(
            {
                "customer_query": (
                    f"My login email is {EMAIL_REDACTION_TOKEN}"
                ),
                "category": "account",
                "priority": "low",
            }
        )


if __name__ == "__main__":
    unittest.main()
