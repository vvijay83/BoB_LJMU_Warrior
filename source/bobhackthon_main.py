from detail_segregation import *
from form_recog import *
from sql_server_conn import *
from translator_content import *
from load_config import *
import re
from datetime import date
validations=False




def clean_segregated_text(val):
    val['ifsc_code'] = val['ifsc_code'][7:]
    val['account_num'] = re.sub('(?<=\d) (?=\d)', '', val['account_num'])
    if 'amount' in val.keys():
        val['amount'] = re.sub("[^\d\.]", "", val['amount'])
    if 'account_total_amount' in val.keys():
        val['account_total_amount'] = re.sub("[^\d\.]", "", val['account_total_amount'])
    val['cheque_number'] = val['cheque_number'].replace("⑈","").replace('⑆',"").replace(" ","").replace("?","")
    if 'account_holder_name' in val.keys():
        val['account_holder_name'] = str(val['account_holder_name'][0][0])
    return val

def validate_details(cleaned_check_details,cleaned_user_details):
    date_current = date.today()
    date_diff = int(str(date.today().day)+str(date.today().month)+str(date.today().year)) - int(cleaned_check_details['date'])
    balance = int(cleaned_user_details['account_total_amount']) - int(cleaned_check_details['amount'])
    if (cleaned_user_details['cheque_number']==cleaned_check_details['cheque_number']) & (cleaned_user_details['ifsc_code']==cleaned_check_details['ifsc_code']) &(cleaned_user_details['account_num']==cleaned_check_details['account_num']) & (cleaned_user_details['Username']==cleaned_check_details['account_holder_name']):
        print("validations are sucesfull") 
        global validations=True
    
if __name__== "__main__":
#def final_code():   
    cheque_file=data['cheque_path']
    form_rec = form_recognizer(cheque_file)
    content = form_rec.form_content()
   
    translator = translate_content()
    translated_text = translator.translate_text(content)
    segregated_text = segregate_regex(translated_text)
   
    azure_sql_conn = connect_azure_sql()
    user_bank_details = azure_sql_conn.get_user_details()
   

    cleaned_check_details = clean_segregated_text(segregated_text)
    print(cleaned_check_details.keys())
    val="extracted user details from bank are {cleaned_check_details}"
   
    cleaned_user_details = clean_segregated_text(user_bank_details)

    azure_sql_conn = connect_azure_sql()
    azure_sql_conn.update_cheque_dtails(cleaned_check_details)
    validate_details(cleaned_check_details,cleaned_user_details)








