import unittest
from unittest.mock import patch

from app.config.settings import MAX_CUSTOMER_QUERY_LENGTH
from app.guardrails.input_validation import (
    InputLengthExceededError,
    validate_input_length,
)


class InputLengthGuardrailTests(unittest.TestCase):
    def test_query_at_limit_is_accepted(self):
        query = "a" * MAX_CUSTOMER_QUERY_LENGTH

        result = validate_input_length(query)

        self.assertEqual(result, query)

    def test_query_over_limit_is_rejected(self):
        query = "a" * (MAX_CUSTOMER_QUERY_LENGTH + 1)

        with self.assertRaises(InputLengthExceededError):
            validate_input_length(query)

    @patch("app.services.support_service.classification_chain")
    def test_rejected_query_does_not_reach_llm(self, mock_chain):
        from app.services.support_service import classify_support_query

        query = "a" * (MAX_CUSTOMER_QUERY_LENGTH + 1)

        with self.assertRaises(InputLengthExceededError):
            classify_support_query(query)

        mock_chain.invoke.assert_not_called()

    @patch("app.services.support_service.response_chain")
    def test_rejected_query_does_not_reach_response_llm(self, mock_chain):
        from app.schemas.support_schema import SupportClassification
        from app.services.support_service import generate_support_response

        query = "a" * (MAX_CUSTOMER_QUERY_LENGTH + 1)
        classification = SupportClassification(
            category="general",
            priority="low",
        )

        with self.assertRaises(InputLengthExceededError):
            generate_support_response(query, classification)

        mock_chain.invoke.assert_not_called()


if __name__ == "__main__":
    unittest.main()
