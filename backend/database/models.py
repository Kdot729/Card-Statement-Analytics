from pydantic import BaseModel

class Analytics(BaseModel):
    PDF_ID: str
    Activity_Period: str
    Statistic: list[Statistic]

class Statistic:
    ID: str
    Mean: float
    Max: float
    Min: float
    Freq: int
    Range: float