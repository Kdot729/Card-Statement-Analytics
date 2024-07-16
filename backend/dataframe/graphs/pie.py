import pandas as panda
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.transaction import Transaction

class Pie(Transaction):

    def __init__(self, Records):
        Basic_Dataframe = panda.DataFrame.from_dict(Records)

        Dataframe.__init__(self, Basic_Dataframe)
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column)
        Dataframe.Removing_Character(self, Transaction.Amount_Column, "$", "")
        Dataframe.Change_Column_Type(self, Transaction.Amount_Column, float)

        Transaction_Sum = self._Dataframe.groupby(self.ID_Column)[self.Amount_Column].sum().reset_index()
        Dataframe.Convert_Dataframe_to_Dictionary(self, Transaction_Sum)