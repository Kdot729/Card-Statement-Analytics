from backend.dataframe.dataframe import Dataframe
import pandas as panda
from backend.dataframe.transaction import Transaction
from pandas.core.groupby import DataFrameGroupBy

class Statistic(Transaction):
    
    Mean_Column = "Mean"
    Min_Column = "Min"
    Max_Column = "Max"
    Range_Column = "Range"
    Occurrence_Column = "Occurrence"


    def __init__(self, Transaction_Dataframe):
        
        Dataframe.__init__(self, Transaction_Dataframe)

        self.Transaction_Group: DataFrameGroupBy = Transaction.Group_By(self, Transaction.Transaction_Column)
        self.Calculate_Mean()
        self.Calculate_Extremas()
        self.Calculate_Occurrence()
        self.Merging_Dataframes()
        self.Calculate_Range()

        self._Statistic_Model = self.Statistic_Dataframe.to_dict(orient="records")
        
    def Calculate_Mean(self) -> None:

        Dataframe.Removing_Character(self, Transaction.Amount_Column, "$", "")
        self._Dataframe[Transaction.Amount_Column] = self._Dataframe[Transaction.Amount_Column].astype(float)
        self.Transaction_Mean = self.Transaction_Group.mean(numeric_only=True).round(2).reset_index()

    def Calculate_Extremas(self) -> None:
        Grouped_Transaction_Amount = self.Transaction_Group[Transaction.Amount_Column]

        self.Max = Grouped_Transaction_Amount.max().reset_index()
        self.Min = Grouped_Transaction_Amount.min().reset_index()

    def Merging_Dataframes(self) -> None:
        Dataframe_List = [self.Transaction_Mean, self.Max, self.Min, self.Occurence]
        self.Statistic_Dataframe: panda.DataFrame = Transaction.Merging_Dataframes(self, Transaction.Transaction_Column, Dataframe_List)
        self.Statistic_Dataframe.columns = [Transaction.Transaction_Column, self.Mean_Column, self.Max_Column, self.Min_Column, self.Occurrence_Column]
    
    def Calculate_Range(self) -> None:
        self.Statistic_Dataframe[self.Range_Column] = self.Statistic_Dataframe[self.Max_Column] - self.Statistic_Dataframe[self.Min_Column]

    def Calculate_Occurrence(self) -> None:
        self.Occurence = self.Dataframe[Transaction.Transaction_Column].value_counts().reset_index()

    @property
    def Statistic_Model(self):
        return self._Statistic_Model