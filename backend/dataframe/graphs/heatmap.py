from datetime import timedelta, date, datetime
import pandas as panda, re
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.graphs.graph import Graph
from backend.dataframe.graphs.line import Line
from backend.dataframe.transaction import Transaction

class Heatmap(Line):

    Day_Column = "Day"
    Month_Column = "Month"
    Numbered_Day_Column = "Numbered Day"

    def __init__(self, Records, Time_Period):

        self.Get_Date_Range(Time_Period)
        Graph.__init__(self, Records)

        Line.Calculate_Daily_Sum(self)

        self.Merging_Dataframes()
        Dataframe.Convert_Dataframe_to_Dictionary(self, self.Heatmap_Dataframe)

    def Get_Date_Range(self, Time_Period: str):

        Split_Time_Period = re.split(r'-|,', Time_Period)
        
        def Strp_Time(Date: str):
            Stripped_Date = f"{Date.strip()} {Split_Time_Period[2].strip()}"
            return datetime.strptime(Stripped_Date, "%b %d %Y")

        self.Starting_Date = Strp_Time(Split_Time_Period[0])
        self.Ending_Date = Strp_Time(Split_Time_Period[1])

    def Merging_Dataframes(self):
        
        self.Heatmap_Dates = panda.date_range(self.Starting_Date, self.Ending_Date-timedelta(days=1), freq='d')
        Day_of_Weeks = self.Strf_Time("%a")
        Months = self.Strf_Time("%b")
        Numbered_Days = self.Strf_Time("%d")
        
        self.Heatmap_Dataframe = panda.DataFrame({Transaction.Transaction_Date_Column: self.Heatmap_Dates, 
                                                    self.Day_Column: Day_of_Weeks, 
                                                    self.Month_Column: Months,
                                                    self.Numbered_Day_Column: Numbered_Days})

        #Note Need to convert Transaction.Transaction_Date_Column to type datetime64[ns] to merge with other dataframe
        self.Daily_Sum_Dataframe[Transaction.Transaction_Date_Column] = panda.to_datetime(self.Daily_Sum_Dataframe[Transaction.Transaction_Date_Column])

        self.Heatmap_Dataframe = self.Heatmap_Dataframe.merge(self.Daily_Sum_Dataframe, on=Transaction.Transaction_Date_Column, how='left').fillna(0)
        Dataframe.Drop_Columns(self, self.Heatmap_Dataframe, self.Transaction_Date_Column)
    
    def Strf_Time(self, Format) -> list[str]: 
        return [Day.strftime(Format) for Day in self.Heatmap_Dates]