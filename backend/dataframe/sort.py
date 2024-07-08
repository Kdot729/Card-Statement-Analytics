from backend.dataframe.statistic import Statistic
from backend.dataframe.dataframe import Dataframe
import pandas as panda

class Sort(Statistic):

    Remove_Dollar_Sign_Columns = [Statistic.Mean_Column, Statistic.Max_Column, Statistic.Min_Column, Statistic.Range_Column]

    def __init__(self, Records):
        Statistic_Dataframe = panda.DataFrame.from_dict(Records)
        Dataframe.__init__(self, Statistic_Dataframe)
        self.Removing_Character()
        self.Convert_to_Numeric()

    def Removing_Character(self) -> None:
        for Column in self.Remove_Dollar_Sign_Columns:
            Dataframe.Removing_Character(self, Column, "$")

    def Convert_to_Numeric(self) -> None:
        self.Dataframe[self.Remove_Dollar_Sign_Columns] = self.Dataframe[self.Remove_Dollar_Sign_Columns].apply(panda.to_numeric)