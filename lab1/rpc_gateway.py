import httpx
import logging

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from settings import RpcSettings

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rpc_gateway")


settings = RpcSettings()

METHOD_TO_SERVER = {
    'message.to_star': settings.TO_STAR_URL,
    'message.to_slash': settings.TO_SLASH_URL,
}


@app.post("/rpc")
async def handle_rpc(request: Request):
    logger.info("Received RPC request")
    rpc_request = await request.json()
    method = rpc_request.get("method")
    data = rpc_request.get("data")

    url = METHOD_TO_SERVER.get(method)
    if not url:
        raise HTTPException(detail={"error": "Unknown method"}, status_code=status.HTTP_404_NOT_FOUND)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
    return JSONResponse(content=response.json(), status_code=response.status_code)
