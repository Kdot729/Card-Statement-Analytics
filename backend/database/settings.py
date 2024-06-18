from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

Mongo_Client = MongoClient(os.getenv("Mongo_URI"))
Mongo_Database = Mongo_Client["Card-Statement-Analysis"]
API_Collection = Mongo_Database["API"]