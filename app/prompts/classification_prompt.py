from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.schemas.support_schema import SupportClassification


output_parser = PydanticOutputParser(
    pydantic_object=SupportClassification
)


classification_prompt = PromptTemplate(
    template="""
You are a customer support classification system.

Classify the customer query into one category and one priority.

Allowed categories:
- payment
- refund
- account
- general

Priority rules:

HIGH:
- Money was deducted but payment failed
- Suspected fraud or unauthorized transaction
- Account is completely blocked or compromised
- Customer cannot access critical funds or services

MEDIUM:
- Refund is delayed or missing
- Login issue where there is no indication of account compromise
- Repeated payment issue without confirmed financial loss
- Customer needs investigation or support intervention

LOW:
- General questions
- How-to questions
- Updating profile or account information
- Requests that do not indicate financial loss, security risk, or blocked access

Customer query:
{customer_query}

{format_instructions}

Important rules:
- Return only the structured output.
- Do not add explanation.
- Do not add markdown.
- Category must be exactly one of the allowed categories.
- Priority must be exactly one of the allowed priorities.
""",
    input_variables=["customer_query"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()
    }
)