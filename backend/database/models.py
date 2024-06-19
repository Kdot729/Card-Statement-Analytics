from pydantic import BaseModel

class URI(BaseModel):
    URI: str

class Analytics(URI):
    URI_ID: str
    Min: float
    Max: float
    Avg: float
    Visit: int