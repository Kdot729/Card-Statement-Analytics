from functools import partial, reduce
import pandas as panda, numpy, re

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
    Average_Column = "Avg"
    Min_Column = "Min"
    Max_Column = "Max"
    Range_Column = "Range"

    Columns = [Transaction_Date_Column, Post_Date_Column, Transaction_Column, Amount_Column, Category_Column]

    def __init__(self, Transactions):
        
        self.Transactions = Transactions

        self.Create_Dataframe()
        self.Trim_All_Columns()
        self.Removing_Character(self.Amount_Column)
        self.Extract_Corporation()
        self.Extract_Location()
        self.Create_New_Transaction()
        self.Change_Values_for_Discover()
        self.Group_By()
        self.Calculate_Mean()
        self.Calculate_Extremas()
        self.Merging_Dataframes()
        self.Calculate_Range()

    def Create_Dataframe(self):
        Numpy_Array = numpy.reshape(self.Transactions, (-1, 5))
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

    def Group_By(self):
        self.Transaction_Group = self.Dataframe.groupby(self.Transaction_Column)

    def Calculate_Mean(self):

        self.Removing_Character(self.Amount_Column, "$", "")
        self.Dataframe[self.Amount_Column] = self.Dataframe[self.Amount_Column].astype(float) 

        self.Transaction_Average = self.Transaction_Group.mean(numeric_only=True).reset_index()
        self._Avg = self.Transaction_Average.to_dict("records")

    def Calculate_Extremas(self):
        Grouped_Transaction_Amount = self.Transaction_Group[self.Amount_Column]

        self.Max = Grouped_Transaction_Amount.max().reset_index()
        self.Min = Grouped_Transaction_Amount.min().reset_index()

    def Merging_Dataframes(self):

        Dataframe_List = [self.Transaction_Average, self.Max, self.Min]
        Merged_Function = partial(panda.merge, on=self.Transaction_Column, how='outer')
        self.Statistical_Dataframe = reduce(Merged_Function, Dataframe_List)
        self.Statistical_Dataframe.columns = [self.Transaction_Column, self.Average_Column, self.Max_Column, self.Min_Column]
    
    def Calculate_Range(self):
        self.Statistical_Dataframe[self.Range_Column] = self.Statistical_Dataframe[self.Max_Column] - self.Statistical_Dataframe[self.Min_Column]

    @property
    def Avg(self):
        return self._Avg