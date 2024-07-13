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
        self.Round()
        self.Statistic_Dataframe = self.Append_Dollar_Sign(self.Statistic_Dataframe)

        self.Convert_Dataframe_to_Dictionary()
        
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

    def Round(self):
        Numeric_Columns = self.Statistic_Dataframe.select_dtypes(include=[numpy.number])
        self.Statistic_Dataframe.loc[:, Numeric_Columns.columns] = numpy.round(Numeric_Columns, 2)

    def Append_Dollar_Sign(self, Dataframe) -> panda.DataFrame:
        Dollar_Columns = [self.Mean_Column, self.Max_Column, self.Min_Column, self.Range_Column]
        Dataframe[Dollar_Columns] = '$' + Dataframe[Dollar_Columns].astype(str)
        return Dataframe

    def Convert_Dataframe_to_Dictionary(self, Orient: str = "records") -> None:
        self._Statistic_Model = self.Statistic_Dataframe.to_dict(orient="records")
    
    @property
    def Statistic_Model(self):
        return self._Statistic_Model