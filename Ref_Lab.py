import xlwings as xw
from datetime import datetime

wb = xw.Book("HaysDX.xlsm")
now = datetime.now()
yr = now.year
input_sht = wb.sheets['User_Input']
yr_sht = wb.sheets[yr]
ref_sht = wb.sheets['Ref labs']
input_sht = wb.sheets['Isolate_Reference']


