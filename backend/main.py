from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.database.settings import API_Collection
from backend.dataframe.dataframe import Dataframe
import json

app = FastAPI()
Router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@Router.post("/post/PDF")
async def PDF(request: Request):
    
    Dataframe_Object = Dataframe((await request.json())["URI"])

    Data = {"URI_ID": (await request.json())["URI_ID"], "URI": Dataframe_Object.URI, "Avg": Dataframe_Object.Avg}
    response = API_Collection.insert_one(Data)
    # print("ID:", response.inserted_id)
    return {"status": 200}

app.include_router(Router)