from pydantic import BaseModel

class Transaction_Average(BaseModel):
    Transaction: str
    Amount: float

class Analytics(BaseModel):
    PDF_ID: str
    Activity_Period: str
    Mean: list[Transaction_Average]