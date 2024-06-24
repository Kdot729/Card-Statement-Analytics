from pydantic import BaseModel

class Transaction_Average(BaseModel):
    Transaction: str
    Amount: float

class Analytics(BaseModel):
    URI: str
    URI_ID: str
    Avg: list[Transaction_Average]