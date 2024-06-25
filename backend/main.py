from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.database.serializers import Analytics_Deserializer
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
@Router.get("/get/PDF")
async def Get_PDF():
    Data = API_Collection.find()
    return Analytics_Deserializer(Data)

@Router.post("/post/PDF")
async def Post_PDF(request: Request):

    Data = {"URI_ID": (await request.json())["URI_ID"]}
    URI = (await request.json())["URI"]
    
    if API_Collection.count_documents(Data, limit = 1) == 0:

        Dataframe_Object = Dataframe(URI)
        Data["Avg"] = Dataframe_Object.Avg
        response = API_Collection.insert_one(Data)
        # print("ID:", response.inserted_id)
    else:
        pass
    
    return {"status": 200}

app.include_router(Router)