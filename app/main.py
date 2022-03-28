from typing import List
from pathlib import Path
from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.demo_data.users import demo_users

from app.models.schemas import User

app = FastAPI(title="Oma sanakrija", openapi_url="/openapi.json")

api_router = APIRouter()
BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app.mount("/static", StaticFiles(directory=str(BASE_PATH / "static")), name="static")
@api_router.get("/", status_code=200, response_class=HTMLResponse)
def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse("index.html", {"request": request})

@api_router.get("/users", response_model=List[User])
def users() -> list:
    return demo_users

app.include_router(api_router)
