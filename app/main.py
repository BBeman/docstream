from fastapi import FastAPI
from app.schemas import EchoRequest, EchoResponse, SummariseRequest, SummariseResponse
from app.llm import summarise

app = FastAPI(title = "docstream")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/echo" , response_model = EchoResponse)
async def echo(req: EchoRequest): 
    return EchoResponse(echo = req.message)

@app.post("/summarise", response_model = SummariseResponse)
async def summarisation(req : SummariseRequest):
    summary = await summarise(req.text, req.max_words)
    return SummariseResponse(summary = summary)