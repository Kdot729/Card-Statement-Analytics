import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.transaction import Transaction

class Bar(Graph):

    def __init__(self, Records, Transaction_Colors):

        super().__init__(panda.DataFrame.from_dict(Records))  
        self._Transaction_Colors = Transaction_Colors
        self.Create_Percentage_Dataframe()
        Graph.Merge_Color_Dateframe(self, self.Pecentage_Transaction_Dataframe)
        Dataframe.Convert_Dataframe_to_Dictionary(self, self.Transaction_Color_Dataframe)

    def Create_Percentage_Dataframe(self):
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column)
        Dataframe.Removing_Character(self, Transaction.Amount_Column, "$", "")
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column, float)

        Transaction_Sum = Dataframe.Group_By(self, Transaction.ID_Column)[self.Amount_Column].sum().reset_index()
        self.Pecentage_Transaction_Dataframe = Transaction.Calulcate_Sum_Percentage(self, Transaction_Sum)