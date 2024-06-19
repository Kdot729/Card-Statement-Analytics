from fastapi import FastAPI, APIRouter
from database.models import URI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
Router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Router)