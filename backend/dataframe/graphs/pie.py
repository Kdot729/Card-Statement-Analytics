import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.transaction import Transaction

class Pie(Graph):

    def __init__(self, Records):

        super().__init__(panda.DataFrame.from_dict(Records))
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column)
        Dataframe.Removing_Character(self, Transaction.Amount_Column, "$", "")
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column, float)
        Transaction.Colorize(self)
        Transaction_Sum = self._Dataframe.groupby([Transaction.ID_Column, Graph.Color_Column])[self.Amount_Column].sum().reset_index()
        Colorized_Transaction_Sum = Transaction.Calulcate_Sum_Percentage(self, Transaction_Sum)
        Dataframe.Convert_Dataframe_to_Dictionary(self, Colorized_Transaction_Sum)

