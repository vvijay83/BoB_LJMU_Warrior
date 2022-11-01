from optparse import Values
import textwrap
import pyodbc 
import pandas as pd
from load_config import *

class connect_azure_sql():
    def __init__(self):
        self.cnxn1: pyodbc.Connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:bobservernew.database.windows.net,1433;Database=BOBDB;Uid=satya;Pwd=Sathya@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        self.crsr1: pyodbc.Cursor =    self.cnxn1.cursor()
        # self.cnxn2: pyodbc.Connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:bobservernew.database.windows.net,1433;Database=BOBcheckdetails;Uid=satya;Pwd=Sathya@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        # self.crsr2: pyodbc.Cursor =    self.cnxn2.cursor()
    def get_user_details(self):
        df = pd.read_sql_query('''select * from [dbo].[User_details]''', self.cnxn1)
        self.cnxn1.close()
        return({'ifsc_code' : df.iloc[0]['ifsc_code'],'Username' : df.iloc[0]['Username'],'account_num' : df.iloc[0]['account_num'],'account_total_amount' : df.iloc[0]['account_total_amount'],
'Minbalance' : df.iloc[0]['Minbalance'],'cheque_number' : df.iloc[0]['cheque_number']})
    def update_cheque_dtails(self,cheque_details):
        stmt = "insert into {table} ({columns}) values ({'values'});".format(table='[dbo].[cheuque_details]', columns=",".join(cheque_details.keys()), values=",".join(cheque_details.values()))
       # stmt = "insert into {table} ({columns}) values ({values});".format(table='[dbo].[cheuque_details]', columns=",".join(cheque_details.keys()), values=",".join(cheque_details.values()))
        '''stmt1 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='ifsc_code',row_value=cheque_details['ifsc_code'])
        
        self.crsr1.execute(stmt1)
        stmt2 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='date_value',row_value=cheque_details['date'])
        
        self.crsr1.execute(stmt2)
        stmt3 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='account_num',row_value=cheque_details['account_num'])
        
        self.crsr1.execute(stmt3)
        stmt4 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='amount',row_value=cheque_details['amount'])
        
        self.crsr1.execute(stmt4)
        stmt5 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='cheque_number',row_value=cheque_details['cheque_number'])
        
        self.crsr1.execute(stmt5)
        stmt6 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='account_holder_name',row_value=cheque_details['account_holder_name'])
        
        self.crsr1.execute(stmt6)
        stmt7 = "insert into {table} ({column_value}) values ('{row_value}');".format(table='[dbo].[cheuque_details]',column_value='amount_digits',row_value=cheque_details['amount_digits'])
        '''
        self.crsr1.execute(stmt)
    
        self.cnxn1.close()


