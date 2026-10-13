from langchain_core.output_parsers import StrOutputParser

from app.models.llm import llm
from app.prompts.response_prompt import response_prompt


output_parser = StrOutputParser()


response_chain = (
    response_prompt
    | llm
    | output_parser
)