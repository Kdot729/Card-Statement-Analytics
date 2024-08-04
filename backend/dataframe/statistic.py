from backend.dataframe.dataframe import Dataframe
import pandas as panda, numpy
from backend.dataframe.transaction import Transaction
from pandas.core.groupby import DataFrameGroupBy

class Statistic(Transaction):
    
    Mean_Column = "Mean"
    Min_Column = "Min"
    Max_Column = "Max"
    Range_Column = "Range"
    Freq_Column = "Freq"


    def __init__(self, Transaction_Dataframe):
        
        Dataframe.__init__(self, Transaction_Dataframe)

        self.Transaction_Group: DataFrameGroupBy = Transaction.Group_By(self, Transaction.ID_Column)
        self.Calculate_Mean()
        self.Calculate_Extremas()
        self.Calculate_Occurrence()
        self.Merging_Dataframes()
        self.Calculate_Range()
        Transaction.Round(self, self.Statistic_Dataframe)
        self.Statistic_Dataframe = self.Append_Dollar_Sign(self.Statistic_Dataframe)
        Transaction.Colorize(self, self.Statistic_Dataframe)
        self.Statistic_Dataframe = self.Statistic_Dataframe.drop(columns=[self.Color_Column])
        Dataframe.Convert_Dataframe_to_Dictionary(self, self.Statistic_Dataframe)
        
    def Calculate_Mean(self) -> None:
        self.Transaction_Mean = self.Transaction_Group.mean(numeric_only=True).reset_index()

    def Calculate_Extremas(self) -> None:
        Grouped_Transaction_Amount = self.Transaction_Group[Transaction.Amount_Column]

        self.Max = Grouped_Transaction_Amount.max().reset_index()
        self.Min = Grouped_Transaction_Amount.min().reset_index()

    def Merging_Dataframes(self) -> None:
        Dataframe_List = [self.Transaction_Mean, self.Max, self.Min, self.Occurence]
        self.Statistic_Dataframe: panda.DataFrame = Transaction.Merging_Dataframes(self, Transaction.ID_Column, Dataframe_List)
        self.Statistic_Dataframe.columns = [Transaction.ID_Column, self.Mean_Column, self.Max_Column, self.Min_Column, self.Freq_Column]
    
    def Calculate_Range(self) -> None:
        self.Statistic_Dataframe[self.Range_Column] = self.Statistic_Dataframe[self.Max_Column] - self.Statistic_Dataframe[self.Min_Column]

    def Calculate_Occurrence(self) -> None:
        self.Occurence = self.Dataframe[Transaction.ID_Column].value_counts().reset_index()

    def Append_Dollar_Sign(self, Dataframe) -> panda.DataFrame:
        Dollar_Columns = [self.Mean_Column, self.Max_Column, self.Min_Column, self.Range_Column]
        Dataframe[Dollar_Columns] = '$' + Dataframe[Dollar_Columns].astype(str)
        return Dataframe