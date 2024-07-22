import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.transaction import Transaction

class Pie(Graph):

    def __init__(self, Records, Transaction_Colors):

        super().__init__(panda.DataFrame.from_dict(Records))
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column)
        Dataframe.Removing_Character(self, Transaction.Amount_Column, "$", "")
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column, float)

        Transaction_Sum = self._Dataframe.groupby([Transaction.ID_Column])[self.Amount_Column].sum().reset_index()
        self.Pecentage_Transaction_Dataframe = Transaction.Calulcate_Sum_Percentage(self, Transaction_Sum)

        self.Merge_Color_Dateframe(Transaction_Colors)
        Dataframe.Convert_Dataframe_to_Dictionary(self, self.Pie_Dataframe)


    def Merge_Color_Dateframe(self, Transaction_Colors):

        Columns = [Transaction.ID_Column, Transaction.Color_Column]
        Color_Dataframe = panda.DataFrame.from_dict(Transaction_Colors, orient="index").reset_index()
        Color_Dataframe.columns = Columns
        self.Pie_Dataframe = self.Pecentage_Transaction_Dataframe.merge(Color_Dataframe, on=Transaction.ID_Column, how='outer')
