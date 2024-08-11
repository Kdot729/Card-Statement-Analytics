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

        self.Daily_Sum_Dataframe: panda.DataFrame = Dataframe.Sum_Group_By(self, Transaction.Transaction_Date_Column, Transaction.Amount_Column)
        self.Daily_Sum_Dataframe.columns = [Transaction.Transaction_Date_Column, self.Sum_Column]
        Transaction.Round(self, self.Daily_Sum_Dataframe)
        self.Format_Date(self.Daily_Sum_Dataframe)
        Dataframe.Convert_Dataframe_to_Dictionary(self, self.Daily_Sum_Dataframe)

    def Merge_Color_Dateframe(self) -> None:
        Graph.Merge_Color_Dateframe(self, self._Dataframe)
        self.Transaction_Color_Dataframe = self.Transaction_Color_Dataframe[self.Selected_Columns]

    def Format_Date(self, Dataframe: panda.DataFrame) -> None:
        Dataframe[Transaction.Transaction_Date_Column] = panda.to_datetime(Dataframe[Transaction.Transaction_Date_Column], format="%m/%d/%y").dt.strftime('%Y-%m-%d')
