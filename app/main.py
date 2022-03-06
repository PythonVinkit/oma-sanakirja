from typing import List
from fastapi import FastAPI, APIRouter
from app.demo_data.users import demo_users

from app.models.schemas import User

app = FastAPI(title="Oma sanakrija", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "moi"}

@api_router.get("/users", response_model=List[User])
def users() -> list:
    return demo_users

app.include_router(api_router)
