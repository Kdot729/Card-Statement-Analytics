import os, json, re, logging, base64
from dotenv import load_dotenv
from adobe.pdfservices.operation.auth.service_principal_credentials import ServicePrincipalCredentials
from adobe.pdfservices.operation.io.cloud_asset import CloudAsset
from adobe.pdfservices.operation.io.stream_asset import StreamAsset
from adobe.pdfservices.operation.pdf_services import PDFServices
from adobe.pdfservices.operation.pdf_services_media_type import PDFServicesMediaType
from adobe.pdfservices.operation.pdfjobs.jobs.extract_pdf_job import ExtractPDFJob
from adobe.pdfservices.operation.pdfjobs.params.extract_pdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.pdfjobs.params.extract_pdf.extract_pdf_params import ExtractPDFParams
from adobe.pdfservices.operation.pdfjobs.result.extract_pdf_result import ExtractPDFResult
from zipfile import ZipFile

load_dotenv()
#Note Logger
# logging.basicConfig(level=logging.INFO)

Extract_PDF_Folder = "extract_pdf"
Zipped_Name = "ExtractTextInfoFromPDF"
PDF_Directory = f"./{Extract_PDF_Folder}/PDF"
Zip_Directory = f"./{Extract_PDF_Folder}/zip"

class Extract:

    def __init__(self, PDF_ID, PDF_URI):

        self.PDF_ID = PDF_ID

        #Note Removes header, leaving only the uri
        self.PDF_URI = PDF_URI.split(",")[1:2][0]

        self.Create_Directories()
        self.Create_PDF()
        self.Create_Zipped_File_Path()
        self.Convert_PDF_to_JSON()
        self.Extract_Data_from_PDF()
        # self.Delete_Output_Files()

    def Create_Directories(self):

        Directories = [PDF_Directory, Zip_Directory]

        for Directory in Directories:
            if not os.path.exists(Directory):
                os.makedirs(Directory)
                
    def Create_PDF(self):
        self.PDF_File_Path = f"{PDF_Directory}/{self.PDF_ID}.pdf"

        if os.path.isfile(self.PDF_File_Path):
            pass
        else:
            with open(self.PDF_File_Path, "wb") as file:
                file.write(base64.b64decode(self.PDF_URI))

    #Note Generates the file path for the zipped file
    def Create_Zipped_File_Path(self):
        Folder_Path = f"{Zip_Directory}/{Zipped_Name}"
        os.makedirs(Folder_Path, exist_ok=True)
        self.Zipped_File_Path = f"{Folder_Path}/{self.PDF_ID}.zip"
    
    def Convert_PDF_to_JSON(self):

        if os.path.isfile(self.Zipped_File_Path):
            pass
        else:
            self.Zipped_File = f"./{Zipped_Name}.zip"

            file = open(self.PDF_File_Path, 'rb')
            input_stream = file.read()
            file.close()

            # Initial setup, create credentials instance
            credentials = ServicePrincipalCredentials(
                client_id=os.getenv("Adobe_ID"),
                client_secret=os.getenv("Adobe_Secret")
            )

            # Creates a PDF Services instance
            pdf_services = PDFServices(credentials=credentials)

            # Creates an asset(s) from source file(s) and upload
            input_asset = pdf_services.upload(input_stream=input_stream, mime_type=PDFServicesMediaType.PDF)

            # Create parameters for the job
            extract_pdf_params = ExtractPDFParams(elements_to_extract=[ExtractElementType.TEXT])

            # Creates a new job instance
            extract_pdf_job = ExtractPDFJob(input_asset=input_asset, extract_pdf_params=extract_pdf_params)

            # Submit the job and gets the job result
            location = pdf_services.submit(extract_pdf_job)
            pdf_services_response = pdf_services.get_job_result(location, ExtractPDFResult)

            # Get content from the resulting asset(s)
            result_asset: CloudAsset = pdf_services_response.get_result().get_resource()
            stream_asset: StreamAsset = pdf_services.get_content(result_asset)

            # Creates an output stream and copy stream asset's content to it
            with open(self.Zipped_File_Path, "wb") as file:
                file.write(stream_asset.get_input_stream())

        archive = ZipFile(self.Zipped_File_Path, 'r')
        jsonentry = archive.open('structuredData.json')
        jsondata = jsonentry.read()
        self.data = json.loads(jsondata)
    
    def Extract_Data_from_PDF(self):
        #Note \S+ means any nonspace characters
        #Note | means nothing after TD
        #Example of matches are //Document/Sect[2]/Table/TR[8]/TD[2]/P and //Document/Sect[2]/Table/TR[2]/TD/P
        Regex_Condtion = r'\S+Table\/TR\[\d+\]\/TD(\[\d+\]|)\/P'
        self._Text_Array = []

        for element in self.data["elements"]:
            if re.search(Regex_Condtion, element["Path"]):
                self.Text_Array.append(element["Text"])

    def Delete_Output_Files(self):

        #Note Delete PDF
        if os.path.isfile(self.PDF_File_Path):
            os.remove(self.PDF_File_Path)
    
        #Note Delete zipped file
        if os.path.isfile(self.Zipped_File_Path):
            os.remove(self.Zipped_File_Path)

    @property
    def Text_Array(self):
        return self._Text_Array