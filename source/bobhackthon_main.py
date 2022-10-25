from detail_segregation import segregate_regex
from form_recog import *
from sql_server_conn import *
from translator_content import *
from load_config import *
import re
from datetime import date

import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import cv2

#title
st.title("Automated Cheque Processing")

#subtitle
st.markdown("## OCR using Azure Cognitive Services")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload the cheque here",type=['png','jpg','jpeg'])
#@st.cache


if image is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="BGR")

def clean_segregated_text(val):
    val['ifsc_code'] = val['ifsc_code'][7:]
    val['account_num'] = re.sub('(?<=\d) (?=\d)', '', val['account_num'])
    if 'amount' in val.keys():
        val['amount'] = re.sub("[^\d\.]", "", val['amount'])
    if 'account_total_amount' in val.keys():
        val['account_total_amount'] = re.sub("[^\d\.]", "", val['account_total_amount'])
    val['cheque_number'] = val['cheque_number'].replace("⑈","").replace('⑆',"").replace(" ","").replace("?","")
    if 'account_holder_name' in val.keys():
        val['account_holder_name'] = val['account_holder_name'][0][0]
    return val

def validate_details(cleaned_check_details,cleaned_user_details):
    date_current = date.today()
    date_diff = int(str(date.today().day)+str(date.today().month)+str(date.today().year)) - int(cleaned_check_details['date'])
    balance = int(cleaned_user_details['account_total_amount']) - int(cleaned_check_details['amount'])
    if (cleaned_user_details['cheque_number']==cleaned_check_details['cheque_number']) & (cleaned_user_details['ifsc_code']==cleaned_check_details['ifsc_code']) &(cleaned_user_details['account_num']==cleaned_check_details['account_num']) & (cleaned_user_details['Username']==cleaned_check_details['account_holder_name']):
        print("validations are sucesfull")    
    
if __name__== "__main__":
    cheque_file=data['cheque_path']
    form_rec = form_recognizer(cheque_file)
    content = form_rec.form_content()
    translator = translate_content()
    translated_text = translator.translate_text(content)
    segregated_text = segregate_regex(translated_text)
    st.write("extracting features from cheque'")
    azure_sql_conn = connect_azure_sql()
    user_bank_details = azure_sql_conn.get_user_details()
    cleaned_check_details = clean_segregated_text(segregated_text)
    cleaned_user_details = clean_segregated_text(user_bank_details)
    validate_details(cleaned_check_details,cleaned_user_details)








