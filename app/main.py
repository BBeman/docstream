from fastapi import FastAPI, status
from pydantic import BaseModel,Field
from typing import Annotated

class EchoRequest(BaseModel):
    message: Annotated[str, Field(min_length =1, max_length =1000)]

class EchoResponse(BaseModel):
    echo: str



app = FastAPI(title = "LLM_summarizer")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/echo" , response_model = EchoResponse)
async def echo(req: EchoRequest): 
    return EchoResponse(echo = req.message)