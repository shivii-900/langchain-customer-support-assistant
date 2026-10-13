from typing import Literal
from pydantic import BaseModel


class SupportClassification(BaseModel):
    category: Literal[
        "payment",
        "refund",
        "account",
        "general"
    ]

    priority: Literal[
        "low",
        "medium",
        "high"
    ]