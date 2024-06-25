import pandas as panda, numpy, re
from backend.extract_pdf.extract import Extract

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)

class Dataframe():

    Transaction_Date_Column = "Transaction Date"
    Post_Date_Column = "Post Date"
    Transaction_Column = "Transaction"
    Amount_Column = "Amount"
    Category_Column = "Category"
    Corporation_Column = "Corporation"
    Location_Column = "Location"

    Columns = [Transaction_Date_Column, Post_Date_Column, Transaction_Column, Amount_Column, Category_Column]

    def __init__(self, URI):
        
        #Note Removes header, leaving only the uri
        self.URI = URI.split(",")[1:2][0]

        self.Extract_Text = Extract(self.URI)
        self.Create_Dataframe()
        self.Trim_All_Columns()
        self.Removing_Character(self.Amount_Column)
        self.Extract_Corporation()
        self.Extract_Location()
        self.Create_New_Transaction()
        self.Change_Values_for_Discover()
        self.Calculate_Mean()

    def Create_Dataframe(self):
        Numpy_Array = numpy.reshape(self.Extract_Text.Text_Array, (-1, 5))
        self.Dataframe = panda.DataFrame.from_records(Numpy_Array, columns=self.Columns)

    def Trim_All_Columns(self):
        self.Dataframe[self.Columns] = self.Dataframe[self.Columns].apply(lambda row: row.str.strip())

    def Removing_Character(self, Dataframe_Column, Remove_Character=" ", New_Character=""):
        self.Dataframe[Dataframe_Column] = self.Dataframe[Dataframe_Column].str.replace(Remove_Character, New_Character)

    def Extract_Corporation(self):
        self.Dataframe[self.Corporation_Column] = self.Dataframe[self.Transaction_Column].str.split(" ").str[0].str.split(".").str[0]

    def Extract_Location(self):
        self.Dataframe[self.Location_Column] = [re.split(r'\d', index)[-1].strip() for index in self.Dataframe[self.Transaction_Column]]

    def Create_New_Transaction(self):

        #Note Combine the corporation and location if it's category is "Supermarkets" or "Warehouse Clubs"
        Merge_Corporation_and_Location = lambda row: f"{row[self.Corporation_Column]} {row[self.Location_Column]}" if row[self.Category_Column] in ["Supermarkets", "Warehouse Clubs"] else row[self.Corporation_Column]
        self.Dataframe[self.Transaction_Column] = self.Dataframe.apply(Merge_Corporation_and_Location, axis=1)

    def Change_Values_for_Discover(self):

        def Replace_String(Column, New_String):

            #Note ?i means case insensitive. s? means the s is optional
            self.Dataframe.loc[self.Dataframe[self.Category_Column].str.match(r'(?i)(Payment|Credit)(s?)'), Column] = New_String
        
        Replace_String(self.Transaction_Column, "Discover Payment")
        Replace_String(self.Corporation_Column, "Discover")

    def Calculate_Mean(self):

        self.Removing_Character(self.Amount_Column, "$", "")
        self.Dataframe[self.Amount_Column] = self.Dataframe[self.Amount_Column].astype(float) 
        Transaction_Group = self.Dataframe.groupby(self.Transaction_Column)

        Transaction_Average = Transaction_Group.mean(numeric_only=True)
        Reset_Index = Transaction_Average.reset_index()
        self._Avg = Reset_Index.to_dict("records")

    @property
    def Avg(self):
        return self._Avg