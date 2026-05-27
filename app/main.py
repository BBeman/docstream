from fastapi import FastAPI
from app.schemas import EchoRequest,EchoResponse


app = FastAPI(title = "docstream")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/echo" , response_model = EchoResponse)
async def echo(req: EchoRequest): 
    return EchoResponse(echo = req.message)