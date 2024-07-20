from backend.dataframe.dataframe import Dataframe
import pandas as panda, numpy, re

class Transaction(Dataframe):

    Transaction_Date_Column = "Transaction Date"
    Post_Date_Column = "Post Date"
    ID_Column = "ID"
    Amount_Column = "Amount"
    Category_Column = "Category"
    Corporation_Column = "Corporation"
    Location_Column = "Location"
    Percentage_Column = "Percentage"

    Columns = [Transaction_Date_Column, Post_Date_Column, ID_Column, Amount_Column, Category_Column]

    def __init__(self, Transactions):
        
        Numpy_Array = numpy.reshape(Transactions, (-1, 5))
        super().__init__(panda.DataFrame.from_records(Numpy_Array, columns=self.Columns)) 

        Dataframe.Trim_All_Columns(self, self.Columns)
        self.Extract_Corporation()
        self.Extract_Location()
        self.Create_New_Transaction()
        self.Change_Values_for_Discover()
        Dataframe.Removing_Character(self, self.Amount_Column, "$", "")
        Dataframe.Change_Column_Type(self, self.Amount_Column, float)
        Dataframe.Convert_Dataframe_to_Dictionary(self, self._Dataframe)

    def Extract_Corporation(self):
        self._Dataframe[self.Corporation_Column] = self._Dataframe[self.ID_Column].str.split(" ").str[0].str.split(".").str[0]

    def Extract_Location(self):
        self._Dataframe[self.Location_Column] = [re.split(r'\d', index)[-1].strip() for index in self._Dataframe[self.ID_Column]]

    def Create_New_Transaction(self):

        Columns = ["Supermarkets", "Warehouse Clubs", "Gasoline"]
        #Note Combine the corporation and location if it's category is "Supermarkets", "Warehouse Clubs" or "Gasoline"
        Merge_Corporation_and_Location = lambda row: f"{row[self.Corporation_Column]} {row[self.Location_Column]}" if row[self.Category_Column] in Columns else row[self.Corporation_Column]
        self._Dataframe[self.ID_Column] = self._Dataframe.apply(Merge_Corporation_and_Location, axis=1)

    def Change_Values_for_Discover(self):

        def Replace_String(Column: str, New_String: str):

            #Note ?i means case insensitive. s? means the s is optional
            self._Dataframe.loc[self._Dataframe[self.Category_Column].str.match(r'(?i)(Payment|Credit)(s?)'), Column] = New_String
        
        Replace_String(self.ID_Column, "Discover Payment")
        Replace_String(self.Corporation_Column, "Discover")

    def Calulcate_Sum_Percentage(self, Dataframe: panda.DataFrame) -> panda.DataFrame:

        def Round_Percentage(Percent):
            return round(Percent, 2)
        
        Sum_Positive = Dataframe[Transaction.Amount_Column][Dataframe[Transaction.Amount_Column].gt(0)].sum()

        Calculate_Percent = lambda row: Round_Percentage((row / Sum_Positive) * 100) if row > 0 else Round_Percentage(row / Sum_Positive)
        Dataframe[self.Percentage_Column] = Dataframe[Transaction.Amount_Column].apply(Calculate_Percent)

        return Dataframe