from fastapi import FastAPI, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from middleware import MetricsMiddleware
from models import DoRequest
from settings import MainSettings
from config import JOB_TO_FUNCTION

settings = MainSettings()

app = FastAPI()

app.add_middleware(MetricsMiddleware)

@app.post("/api/v1/do")
async def do(body: DoRequest):
    func = JOB_TO_FUNCTION[settings.DO_JOB]
    return {"result": func(body.message)}


@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
