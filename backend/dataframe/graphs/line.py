import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.transaction import Transaction

class Line(Graph):

    Selected_Columns = [Transaction.Transaction_Date_Column, Transaction.ID_Column, Transaction.Amount_Column, Transaction.Color_Column]
    Lambda_Columns = Selected_Columns[1:]
    Sum_Column = "Sum"

    def __init__(self, Records, Transaction_Colors):

        self._Transaction_Colors = Transaction_Colors
        super().__init__(panda.DataFrame.from_dict(Records))

        self.Calculate_Daily_Sum()

        self.Daily_Sum_Dictionary = self.Daily_Sum_Dataframe.set_index(Transaction.Transaction_Date_Column).to_dict('index')

        self.Merge_Color_Dateframe()
        self.Convert_Column_to_DateTime(self.Transaction_Color_Dataframe)
        self.Group_Transactions_Per_Day()
        self.Merge_Dictionaries()

    def Calculate_Daily_Sum(self) -> None:
        self.Daily_Sum_Dataframe: panda.DataFrame = Dataframe.Sum_Group_By(self, Transaction.Transaction_Date_Column, Transaction.Amount_Column)
        self.Daily_Sum_Dataframe.columns = [Transaction.Transaction_Date_Column, self.Sum_Column]
        Transaction.Round(self, self.Daily_Sum_Dataframe)
        self.Convert_Column_to_DateTime(self.Daily_Sum_Dataframe)

    def Merge_Color_Dateframe(self) -> None:
        Graph.Merge_Color_Dateframe(self, self._Dataframe)
        self.Transaction_Color_Dataframe = self.Transaction_Color_Dataframe[self.Selected_Columns]

    #Note Convert column type to datetime64[ns] 
    def Convert_Column_to_DateTime(self, Dataframe: panda.DataFrame) -> None:
        Dataframe[Transaction.Transaction_Date_Column] = panda.to_datetime(Dataframe[Transaction.Transaction_Date_Column], format="%m/%d/%y").dt.strftime('%Y-%m-%d')

    def Group_Transactions_Per_Day(self) -> None:
        Transaction_Dates = self.Transaction_Color_Dataframe[Transaction.Transaction_Date_Column]
        self.Daily_Grouped_Transactions = {row: self.Transaction_Color_Dataframe[Transaction_Dates == row][self.Lambda_Columns].to_dict(orient='records') for row in Transaction_Dates}

    def Merge_Dictionaries(self) -> None:
        self.Daily_Sum_Dictionary.update({key: [self.Daily_Sum_Dictionary[key], self.Daily_Grouped_Transactions[key]] if key in self.Daily_Grouped_Transactions else self.Daily_Sum_Dictionary[key] for key in self.Daily_Sum_Dictionary})
        self._Records = [{"Transaction Date": Key, "Sum": Value[0]["Sum"], "Grouped Transactions": Value[1]} for Key,Value in self.Daily_Sum_Dictionary.items()]