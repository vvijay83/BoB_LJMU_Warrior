import os, requests, uuid, json
from load_config import *
subscription_key = data['subscription_key_translate']
region = "eastus2"
endpoint = data['endpoint_translator']

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
class translate_content():
    def __init__(self):
        self.path = '/translate'
        self.params = {'api-version':'3.0','to':['en']}
        self.constructed_url = endpoint + self.path 
        self.headers = {
                'Ocp-Apim-Subscription-Key': subscription_key,
                'Ocp-Apim-Subscription-Region': region,
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
            }
    def translate_text(self,content):        
        translated_text = []
        # You can pass more than one object in body.
        for i in content:
                body = [{
            'text' : i
                }]
                request = requests.post(self.constructed_url, params =self.params ,headers=self.headers, json=body)
                response = request.json()
                translated_text.append(response[0]['translations'])
        return       translated_text  

    
