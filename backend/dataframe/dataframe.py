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

    def __init__(self, URI):
        
        #Note Removes header, leaving only the uri
        self.URI = URI.split(",")[1:2][0]

        self.Extract_Text = Extract(self.URI)
        self.Create_Dataframe()
        self.Trim_All_Columns()
        self.Removing_Character(self.Amount_Column)
        self.Extract_Corporation()
        self.Extract_Location()

    def Create_Dataframe(self):
        Columns = [self.Transaction_Date_Column, self.Post_Date_Column, self.Transaction_Column, self.Amount_Column, self.Category_Column]
        Numpy_Array = numpy.reshape(self.Extract_Text.Text_Array, (-1, 5))
        self.Dataframe = panda.DataFrame.from_records(Numpy_Array, columns=Columns)

    def Trim_All_Columns(self):
        Trimming_Condition = lambda row: row.strip() if isinstance(row, str) else row
        self.Dataframe = self.Dataframe.apply(Trimming_Condition)

    def Removing_Character(self, Dataframe_Column, Remove_Character=" ", New_Character=""):
        self.Dataframe[Dataframe_Column] = self.Dataframe[Dataframe_Column].str.replace(Remove_Character, New_Character)

    def Extract_Corporation(self):
        self.Dataframe[self.Corporation_Column] = self.Dataframe[self.Transaction_Column].str.split(" ").str[0].str.split(".").str[0]

    def Extract_Location(self):
        self.Dataframe[self.Location_Column] = [re.split(r'\d', index)[-1].strip() for index in self.Dataframe[self.Transaction_Column]]