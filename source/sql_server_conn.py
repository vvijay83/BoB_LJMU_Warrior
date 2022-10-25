import textwrap
import pyodbc 
import pandas as pd
from load_config import *

class connect_azure_sql():
    def __init__(self):
        self.cnxn: pyodbc.Connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:bobservernew.database.windows.net,1433;Database=BOBDB;Uid=satya;Pwd=Sathya@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        self.crsr: pyodbc.Cursor =    self.cnxn.cursor()
    def get_user_details(self):
        df = pd.read_sql_query('''select * from [dbo].[User_details]''', self.cnxn)
        self.cnxn.close()
        return({'ifsc_code' : df.iloc[0]['ifsc_code'],'Username' : df.iloc[0]['Username'],'account_num' : df.iloc[0]['account_num'],'account_total_amount' : df.iloc[0]['account_total_amount'],
'Minbalance' : df.iloc[0]['Minbalance'],'cheque_number' : df.iloc[0]['cheque_number']})

