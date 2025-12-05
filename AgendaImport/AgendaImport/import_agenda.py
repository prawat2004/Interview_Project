from db_table import db
import pandas as pd
import sys
import os

#TODO: Add error handling codes associated with message, maybe change this to a separate file?
error = {}
#Find error code associated with print message 
def findErr(errCode):
    return error[errCode]

#TODO Clean functions
def clean_dataframe(df):
    return
#need some way to fetch data
def getColData(df, row, columnName):
    col_idx = next((column for column in df.columns if str(column) == columnName), None)

    if col_idx:
        value = row[col_idx]
        return str(value).strip()
    return ""


#TODO Read, 
def create_table(file):
    database = db()
    database.create_table

    dataframe = pd.read_excel(file, header = 14) #start from row 14
    
    for idx, row in dataframe.iterrows():
        colData = {
        }
    return

#run script - more or less finished
if(len(sys.arv)==2):
    file = sys.argv[1]
else:
    print("Incorrect # of inputs")

errno = create_table(file)
print(findErr(errno))