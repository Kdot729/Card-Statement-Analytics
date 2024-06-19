from fastapi import FastAPI, APIRouter
from backend.database.models import URI
from fastapi.middleware.cors import CORSMiddleware
from backend.dataframe.dataframe import Dataframe

app = FastAPI()
Router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@Router.post("/post/{URI_ID}")
async def testing(URI_ID: str , URI: URI):
    Dataframe(URI.URI)
    # response = API_Collection.insert_one(dict(URI))
    return {"status": 200}

app.include_router(Router)