from langchain_core.output_parsers import PydanticOutputParser

from app.models.llm import llm
from app.prompts.classification_prompt import classification_prompt
from app.schemas.support_schema import SupportClassification


output_parser = PydanticOutputParser(
    pydantic_object=SupportClassification
)


classification_chain = (
    classification_prompt
    | llm
    | output_parser
)