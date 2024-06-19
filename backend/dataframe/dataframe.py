import pandas as panda, numpy
from backend.extract_pdf.extract import Extract

panda.set_option('display.max_rows', None)
panda.set_option('display.max_columns', None)
panda.set_option('display.width', None)
panda.set_option('display.max_colwidth', None)

class Dataframe():

    def __init__(self, URI):
        
        #Note Removes header, leaving only the uri
        self.URI = URI.split(",")[1:2][0]

        self.Extract_Text = Extract(self.URI)
        self.Create_Dataframe()


    def Create_Dataframe(self):
        Columns = ["Transaction Date", "Post Date", "Transaction", "Amount", "Category"]
        Numpy_Array = numpy.reshape(self.Extract_Text.Text_Array, (-1, 5))
        Dataframe = panda.DataFrame.from_records(Numpy_Array, columns=Columns)
        print(Dataframe)
