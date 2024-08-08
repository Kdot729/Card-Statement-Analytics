import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.transaction import Transaction

class Graph(Transaction):

    def __init__(self, Records):

        Basic_Dataframe = panda.DataFrame.from_dict(Records)
        Dataframe.__init__(self, Basic_Dataframe)

    def Merge_Color_Dateframe(self, Dataframe: panda.DataFrame) -> None:

        Color_Dataframe = panda.DataFrame.from_dict(self._Transaction_Colors, orient="index").reset_index()
        Color_Dataframe.columns = [Transaction.ID_Column, Transaction.Color_Column]
        self.Transaction_Color_Dataframe = Dataframe.merge(Color_Dataframe, on=Transaction.ID_Column, how='outer')
        Transaction.Round(self, self.Transaction_Color_Dataframe)
