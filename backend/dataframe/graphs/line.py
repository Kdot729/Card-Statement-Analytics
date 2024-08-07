import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.transaction import Transaction

class Line(Graph):

    def __init__(self, Records, Transaction_Colors):

        super().__init__(panda.DataFrame.from_dict(Records))
        Daily_Sum_Dataframe: panda.DataFrame = Dataframe.Group_By(self, Transaction.Transaction_Date_Column)
        Daily_Sum_Dataframe = Daily_Sum_Dataframe[Transaction.Amount_Column].sum().reset_index()

        Dataframe.Convert_Dataframe_to_Dictionary(self, Daily_Sum_Dataframe)