from functools import partial, reduce
import pandas as panda

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)

class Dataframe():

    def __init__(self, Dataframe: panda.DataFrame) -> None:
        self._Dataframe = Dataframe

    def Trim_All_Columns(self, Columns: list[str]) -> None:
        self._Dataframe[Columns] = self._Dataframe[Columns].apply(lambda row: row.str.strip())

    def Removing_Character(self, Column: str, Remove_Character=" ", New_Character="") -> None:
        self._Dataframe[Column] = self._Dataframe[Column].str.replace(Remove_Character, New_Character)

    def Group_By(self, Grouped_Column: str):
        return self._Dataframe.groupby(Grouped_Column)

    def Merging_Dataframes(self, On_Merge_Column: str, Dataframe_List: list[panda.DataFrame]) -> panda.DataFrame:

        Merged_Function: partial[panda.DataFrame] = partial(panda.merge, on=On_Merge_Column, how='outer')
        return reduce(Merged_Function, Dataframe_List)
    
    @property
    def Dataframe(self):
        return self._Dataframe
    