from pydantic import BaseModel

class Statistic(BaseModel):
    ID: str
    Mean: float
    Max: float
    Min: float
    Freq: int
    Range: float

class Analytics(BaseModel):
    PDF_ID: str
    Activity_Period: str
    Statistic: list[Statistic]