import re
from load_config import *

from flair.data import Sentence
from flair.models import SequenceTagger
dict_vals={}
tagger = SequenceTagger.load("flair/ner-english-large")

def segregate_regex(translated_text):    
    vals_append=[]
    for i in translated_text:
        i[0]['text']=i[0]['text'].lower()
        if re.findall(r"[a-z]+,?\s+(?:[a-z]*\.?\s*)?[a-z]+", i[0]['text']):
            vals_append.append(i[0]['text'])
            dict_vals['text']=vals_append
        elif (re.findall(r"[0-9]*,[0-9]*,[0-9]*",i[0]['text']) ):
            dict_vals['amount'] = i[0]['text']
        elif(re.findall(r"⑈.*", i[0]['text'])):
            dict_vals['cheque_number'] = i[0]['text']
        elif(re.findall(r"ifsc.*",i[0]['text'])):
            dict_vals['ifsc_code'] = i[0]['text']
        elif(any([True for j in range(1900,2024) if str(j) in i[0]['text'][-4:]])):
            dict_vals['date'] = i[0]['text']  
        elif(re.findall(r"^[0-9]\s[0-9]*",i[0]['text'])):
            dict_vals['account_num'] = i[0]['text']   

    account_holder_name=[]
    locations=[]
    for i in dict_vals['text']:
        ner_model = Sentence(i)
        tagger.predict(ner_model)
        l=ner_model.get_spans('ner')
        val1 = [i.text for i in l if  i.tag=="PER"]
        if val1:
            account_holder_name.append(val1)
        val2=[i.text for i in l if  i.tag=="LOC"]
        if val2:
            locations.append(val2)
    dict_vals['account_holder_name'] = account_holder_name
    dict_vals['locations'] = locations


    digits = ['one', 'two',   'three', 'four', 'five', 
            'six', 'seven', 'eight', 'nine']

    teens  = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
            'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens   = ['twenty', 'thirty', 'fourty', 'fifty', 
            'sixty', 'seventy', 'eighty', 'ninety']


    dict_vals['amount_digits'] = set([i   for i in dict_vals['text'] for j in i.split() if j in digits+teens+tens])
    del dict_vals['text']
    return(dict_vals)   