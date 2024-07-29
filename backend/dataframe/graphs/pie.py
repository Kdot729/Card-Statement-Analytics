import pandas as panda
from backend.dataframe.graphs.bar import Bar
from backend.dataframe.transaction import Transaction

class Pie(Bar):

    def __init__(self, Records, Transaction_Colors):

        super().__init__(panda.DataFrame.from_dict(Records), Transaction_Colors)

    def Merge_Color_Dateframe(self):
        Bar.Merge_Color_Dateframe(self)

        #Note Getting rid of Discover Payment so it doesn't show up in the pie graph
        self.Transaction_Color_Dataframe = self.Transaction_Color_Dataframe[self.Transaction_Color_Dataframe[Transaction.ID_Column] != "Discover Payment"]
