from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path
from fastapi import HTTPException
from fastapi import status
from typing import Annotated

from ..openapi.tags import Tags

from ..dependencies import get_token_header

router = APIRouter(
  prefix = "/items",
  tags = [Tags.ITEMS],
  dependencies = [Depends(get_token_header)],
  responses = {
    404: {
      "description": "Not Found"
    }
  }
)

ITEMS = {
  "plumbus": {"name": "Plumbus"},
  "gun": {"name": "Portal Gun"}
}

@router.get("/")
async def read_items():
  return ITEMS

@router.get("/{id}")
async def read_item(id: Annotated[str, Path()]):
  if id not in ITEMS:
    raise HTTPException(
      status_code = status.HTTP_404_NOT_FOUND,
      detail = "Item not found"
    )

  return ITEMS[id]
