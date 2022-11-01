from sql_server_conn import *
from load_config import *
azure_sql_conn = connect_azure_sql()
check_bank_details = azure_sql_conn.get_check_details_db()
from bobhackthon_main import validations
from random import randint     
    

def generate_token(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#import easyocr as ocr  #OCR
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
    st.image(opencv_image, channels="BGR")
    st.write("extracting features from cheque")
    st.write("extracted features are {checkdetails}".format(checkdetails = check_bank_details ))
    if validations==True:
        st.write("validations are successfull")
        st.write("please share the generated 9 digit code as positive pay confirmation".format(generate_token(9)))
    st.caption("Made with ❤️ by @1littlecoder")




