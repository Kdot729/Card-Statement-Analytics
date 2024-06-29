from pydantic import BaseModel

class Analytics(BaseModel):
    PDF_ID: str
    Activity_Period: str
    Statistic: list[Statistic]

class Statistic:
    Transaction: str
    Mean: float
    Max: float
    Min: float
    Occurrence: int
    Range: float