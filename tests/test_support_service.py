# tests/test_support_service.py

from app.services.support_service import (
    classify_support_query,
    generate_support_response,
)


class SupportServiceTester:

    def __init__(self):
        self.test_queries = [
            "My money was deducted but the payment failed.",
            "I requested a refund last week but I have not received it yet.",
            "I cannot log into my account.",
            "How can I change my email address?",
        ]

    def run_tests(self):

        for customer_query in self.test_queries:

            print("\n" + "=" * 70)

            print("\nCustomer Query:")
            print(customer_query)

            classification = classify_support_query(
                customer_query
            )

            print("\nCategory:")
            print(classification.category)

            print("\nPriority:")
            print(classification.priority)

            response = generate_support_response(
                customer_query=customer_query,
                classification=classification,
            )

            print("\nSupport Response:")
            print(response)