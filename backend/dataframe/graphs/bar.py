import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.transaction import Transaction

class Bar(Graph):

    def __init__(self, Records, Transaction_Colors):

        super().__init__(panda.DataFrame.from_dict(Records))  
        self._Transaction_Colors = Transaction_Colors
        self.Create_Percentage_Dataframe()
        self.Merge_Color_Dateframe()
        Dataframe.Convert_Dataframe_to_Dictionary(self, self.Transaction_Color_Dataframe)

    def Create_Percentage_Dataframe(self):
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column)
        Dataframe.Removing_Character(self, Transaction.Amount_Column, "$", "")
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column, float)

        Transaction_Sum = self._Dataframe.groupby([Transaction.ID_Column])[self.Amount_Column].sum().reset_index()
        self.Pecentage_Transaction_Dataframe = Transaction.Calulcate_Sum_Percentage(self, Transaction_Sum)

    def Merge_Color_Dateframe(self):

        Columns = [Transaction.ID_Column, Transaction.Color_Column]
        Color_Dataframe = panda.DataFrame.from_dict(self._Transaction_Colors, orient="index").reset_index()
        Color_Dataframe.columns = Columns
        self.Transaction_Color_Dataframe = self.Pecentage_Transaction_Dataframe.merge(Color_Dataframe, on=Transaction.ID_Column, how='outer')

