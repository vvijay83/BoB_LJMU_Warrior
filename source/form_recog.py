from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from load_config import *

endpoint = data['endpoint']
credential = AzureKeyCredential(data['form_recog_cred'])

document_analysis_client = DocumentAnalysisClient(endpoint, credential)
class form_recognizer():
    def __init__(self,cheque_file):
        with open(cheque_file, "rb") as fd:
            self.document = fd.read()
        self.poller = document_analysis_client.begin_analyze_document("prebuilt-layout", self.document)
        self.result = self.poller.result()
    def form_content(self):
        for page in self.result.pages:
            content=[]
            for line_idx, line in enumerate(page.lines):
                content.append(line.content)
        return  content       
    

   

  