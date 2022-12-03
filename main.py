from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Security
from fastapi.security import APIKeyHeader
from starlette import status

from router.api import api

import os

app = FastAPI()


API_KEY = os.environ.get("API_KEY", "123456")
API_KEY_NAME = "x-api-key"

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def check_token(api_key_header: str = Security(api_key_header_auth)):

    if api_key_header != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid KEY"
        )


app.include_router(
    api,
    prefix="/api",
    tags=["PDF Services"],
    # dependencies=[Security(check_token)]
)
