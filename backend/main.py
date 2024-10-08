from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.database.models import Graph, Sorting, Sorting_Column
from backend.database.serializers import Analytics_Deserializer
from backend.database.settings import API_Collection
import json
from backend.dataframe.graphs.bar import Bar
from backend.dataframe.graphs.pie import Pie
from backend.dataframe.graphs.line import Line
from backend.dataframe.graphs.heatmap import Heatmap
from backend.dataframe.sort import Sort
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
        Data["Statistic"] = Statistic_Object.Records
        Data["Records"] = Transaction_Object.Records
        Data["Color"] = Statistic_Object.Transaction_Colors

        response = API_Collection.insert_one(Data)
        # print("ID:", response.inserted_id)

    else:
        pass
    
    return {"status": 200}

@Router.get("/get/{sorting}/{sorting_column}/PDF/{id}")
async def Get_Sorted_PDF(sorting: Sorting, sorting_column: Sorting_Column, id: str):

    Data = API_Collection.find_one({"PDF_ID": id})

    if sorting is Sorting.Ascending:
        Boolean_Sort = True

    elif sorting is Sorting.Descending:
        Boolean_Sort = False

    Sorted_Data = Sort(Data["Statistic"], sorting_column.value, Boolean_Sort)

    return {"Statistic": Sorted_Data.Records, "Color": Data["Color"]}

@Router.get("/get/{graph}/PDF/{id}")
async def Get_Graph_Data(graph: Graph, id: str):

    Data = API_Collection.find_one({"PDF_ID": id})

    if graph is Graph.Pie:
        Graph_Data = Pie(Data["Records"], Data["Color"])
        JSON_Key = "Pie"
    
    elif graph is Graph.Bar:
        Graph_Data = Bar(Data["Records"], Data["Color"])
        JSON_Key = "Bar"
    
    elif graph is Graph.Line:
        Graph_Data = Line(Data["Records"], Data["Color"])
        JSON_Key = "Line"
    
    elif graph is Graph.Heatmap:
        Graph_Data = Heatmap(Data["Records"], Data["Activity_Period"])
        JSON_Key = "Heatmap"

    return {JSON_Key: Graph_Data.Records}

app.include_router(Router)