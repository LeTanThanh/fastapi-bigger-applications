from fastapi import Header
from fastapi import Query
from fastapi import HTTPException
from fastapi import status

from typing import Annotated

async def get_token_header(x_token: Annotated[str, Header()]) -> str:
  if x_token != "fake-super-secret-token":
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = "X-Token header invalid"
    )

  return x_token

async def get_token_query(token: Annotated[str, Query()]) -> str:
  if token != "jessica":
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail="No Jessica token provided"
    )

  return token
