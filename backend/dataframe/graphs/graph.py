import pandas as panda, random, numpy
from backend.dataframe.dataframe import Dataframe
from backend.dataframe.transaction import Transaction

class Graph(Transaction):

    def __init__(self, Records):

        Basic_Dataframe = panda.DataFrame.from_dict(Records)
        Dataframe.__init__(self, Basic_Dataframe)


