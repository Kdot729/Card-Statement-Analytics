import pandas as panda, random, numpy
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.transaction import Transaction

class Graph(Transaction):

    Color_Column = "Color"
    def __init__(self, Records):

        Basic_Dataframe = panda.DataFrame.from_dict(Records)
        Dataframe.__init__(self, Basic_Dataframe)

    def Colorize(self):

        Transactions = list(self._Dataframe[Transaction.ID_Column].drop_duplicates())

        self.RGB_Colors = [self.Generate_RGB() for Transaction in range(len(Transactions))]
        self.RGB_Colors = self.Check_Duplicate_Colors()
        Transaction_Colors = dict(zip(Transactions, self.RGB_Colors))

        Colorize_Transaction = lambda row: Transaction_Colors[row]
        self._Dataframe[self.Color_Column] = self._Dataframe[Transaction.ID_Column].apply(Colorize_Transaction)

    def Generate_RGB(self):

        def Randomize():
            return random.randint(0, 255)
        
        return f"rgb({Randomize()}, {Randomize()}, {Randomize()})"
    
    def Check_Duplicate_Colors(self):

        Potential_Duplicate_RGB_Colors_Length = len(self.RGB_Colors)
        No_Duplicates_RGB_Colors = numpy.unique(numpy.array(self.RGB_Colors))
        No_Duplicates_RGB_Colors_Length = len(No_Duplicates_RGB_Colors)

        if No_Duplicates_RGB_Colors_Length != Potential_Duplicate_RGB_Colors_Length:
            Amount_Color_Redos = Potential_Duplicate_RGB_Colors_Length - No_Duplicates_RGB_Colors_Length

            Append_RGB_Colors = [self.Generate_RGB() for Redo_Color in range(Amount_Color_Redos)]

            No_Duplicates_RGB_Colors = numpy.append(No_Duplicates_RGB_Colors, Append_RGB_Colors)
        
        return No_Duplicates_RGB_Colors


