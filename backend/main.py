from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.database.serializers import Analytics_Deserializer
from backend.database.settings import API_Collection
import json
from backend.dataframe.statistic import Statistic
from backend.dataframe.transaction import Transaction
from backend.extract_pdf.extract import Extract

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
async def Get_All_PDF():
    Data = API_Collection.find()
    return Analytics_Deserializer(Data)

@Router.get("/get/PDF/{id}")
async def Get_PDF(id: str):
    Data = API_Collection.find_one({"PDF_ID": id})
    return Analytics_Deserializer(Data)

@Router.post("/post/PDF")
async def Post_PDF(request: Request):

    PDF_ID = (await request.json())["PDF_ID"]
    Data = {"PDF_ID": PDF_ID}
    PDF = (await request.json())["PDF"]

    if API_Collection.count_documents(Data, limit = 1) == 0:

        PDF_Object = Extract(PDF_ID, PDF)
        Transaction_Object = Transaction(PDF_Object.Text_Array)
        Statistic_Object = Statistic(Transaction_Object.Dataframe)

        Data["Activity_Period"] = PDF_Object.Activity_Period
        Data["Statistic"] = Statistic_Object.Statistic_Model

        response = API_Collection.insert_one(Data)
        # print("ID:", response.inserted_id)

    else:
        pass
    
    return {"status": 200}

app.include_router(Router)