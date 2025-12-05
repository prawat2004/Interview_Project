from db_table import db
import pandas as pd
import sys
import os

#TODO: Add error handling codes associated with message, maybe change this to a separate file?
error = {}
#Find error code associated with print message 
def findErr(errCode):
    return

#TODO Clean functions
def clean_dataframe(df):
    return

#TODO Read, 
def create_table(file):
    database = db()
    database.create_table

    dataframe = pd.read_excel(file, header = 14) #start from column 14
    return

#run script - more or less finished
if(len(sys.arv)==2):
    file = sys.argv[1]
else:
    print("Incorrect # of inputs")

errno = create_table(file)
print(findErr(errno))