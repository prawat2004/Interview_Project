from db_table import db
import pandas as pd
import sys
import os

#TODO: Add error handling codes associated with message, maybe change this to a separate file?
error = {0: "Executed Properly"}
#Find error code associated with print message 


def return_val(errCode):
    return error[errCode]

#TODO Clean functions
def clean_dataframe(df):
    return
#need some way to fetch data
def get_col_data(df, row, columnName):
    col_idx = next((column for column in df.columns if str(column) == columnName), None)

    if col_idx:
        value = row[col_idx]
        return str(value).strip()
    return ""

#Data Format for Reference
# "*Date" -> date
# "*Time Start" -> time_start
# "*Time End" -> time_end
# "*Session or Sub-session(Sub)" -> type
# "*Session Title" -> title
# "*Room/Location" -> location
# "Description" -> description
# "Speakers" -> speaker
def create_table(file):
    database = db()
    database.create_table()

    dataframe = pd.read_excel(file, header = 14) #start from row 14
    rowNum = 0
    for index, row in dataframe.iterrows():
        rowData = {
            "id": index,
            "date": get_col_data(dataframe, row, "*Date"),
            "time_start": get_col_data(dataframe, row, "*Time Start"),
            "time_end": get_col_data(dataframe, row, "**Time End"),
            "title": get_col_data(dataframe, row, "*Session Title"),
            "location": get_col_data(dataframe, row, "*Room/Location"),
            "description": get_col_data(dataframe, row, "Description"),
            "speaker": get_col_data(dataframe, row, "Speakers"),
            "type": get_col_data(dataframe, row, "*Session or Sub-session(Sub)"),
            }
        database.insert(rowData)
        rowNum +=1
    return 0

#run script - more or less finished
if(len(sys.arv)==2):
    file = sys.argv[1]
else:
    print("Incorrect # of inputs")

errno = create_table(file)
print(return_val(errno))