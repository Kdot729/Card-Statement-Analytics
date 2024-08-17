from functools import partial, reduce
from typing import Callable
import pandas as panda

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)

class Dataframe():

    def __init__(self, Dataframe: panda.DataFrame) -> None:
        self._Dataframe = Dataframe

    def Trim_All_Columns(self, Columns: list[str]) -> None:
        Stripping_Value = lambda row: row.str.strip()
        self._Dataframe[Columns] = self.Applying_Column_Lambda(Columns, Stripping_Value)

    def Removing_Character(self, Column: str, Remove_Character=" ", New_Character="") -> None:
        self._Dataframe[Column] = self._Dataframe[Column].str.replace(Remove_Character, New_Character)

    def Group_By(self, Grouped_Column: str):
        return self._Dataframe.groupby(Grouped_Column)

    def Merging_Dataframes(self, On_Merge_Column: str, Dataframe_List: list[panda.DataFrame]) -> panda.DataFrame:

        Merged_Function: partial[panda.DataFrame] = partial(panda.merge, on=On_Merge_Column, how='outer')
        return reduce(Merged_Function, Dataframe_List)
    
    def Sort(self, Column: str, Boolean_Sort: bool) -> None:
        self._Dataframe = self._Dataframe.sort_values(by=[Column], ascending=Boolean_Sort)
    
    def Convert_Dataframe_to_Dictionary(self, Dataframe: panda.DataFrame, Orient: str = "records") -> None:
        self._Records = Dataframe.to_dict(orient=Orient)

    def Change_Column_Type(self, Column: str, Column_Type: object = str) -> None:
        self._Dataframe[Column] = self._Dataframe[Column].astype(Column_Type)

    def Applying_Column_Lambda(self, Columns: str | list[str], Lambda: Callable) -> panda.DataFrame:
        return self._Dataframe[Columns].apply(Lambda)

    def Sum_Group_By(self, Grouped_Column: str, Sum_Column: str) -> panda.DataFrame:
        return self.Group_By(Grouped_Column)[Sum_Column].sum().reset_index()
    
    def Drop_Columns(self, Dataframe: panda.DataFrame, Columns: str | list[str]) -> None: 
        Dataframe.drop(columns=Columns, inplace=True)

    @property
    def Dataframe(self):
        return self._Dataframe
    
    @property
    def Records(self):
        return self._Records
    