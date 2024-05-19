from fastapi import APIRouter

from ..openapi.tags import Tags

router = APIRouter()

@router.get("/users", tags = [Tags.USERS])
async def read_users():
  return [
    {"username": "Rick"},
    {"username": "Morty"}
  ]

@router.get("/users/me", tags = [Tags.USERS])
async def read_user_me():
  return {"username": "Rick"}

@router.get("/users/{id}", tags = [Tags.USERS])
async def read_user(id: int):
  return {"username": "Rick"}
