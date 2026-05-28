from pydantic import BaseModel,Field
from typing import Annotated




class EchoRequest(BaseModel):
    message: Annotated[str, Field(min_length =1, max_length =1000)]

class EchoResponse(BaseModel):
    echo: str

class SummariseRequest(BaseModel):
    text: Annotated[str, Field(min_length=10, max_length= 50000)]
    max_words: Annotated[int, Field(ge = 10, le=500, default = 100)]


class SummariseResponse(BaseModel):
    summary: str
