from enum import StrEnum, Enum, auto
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

class Sorting(StrEnum):

    #Note auto() converts the field to lowercase
    Ascending = auto()
    Descending = auto()

    #Note Case insensitive
    @classmethod
    def _missing_(cls, Value):
        Value = Value.lower()
        for Field in cls:
            if Field == Value:
                return Field
        return None

class Sorting_Column(Enum):
    ID = "ID"
    Mean = "Mean"
    Min = "Min"
    Max = "Max"
    Range = "Range"
    Freq = "Freq"