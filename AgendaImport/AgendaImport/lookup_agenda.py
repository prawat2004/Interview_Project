from db_table import database
import sys

def print_event(row):
    return

def find_info(column, value):
    db = database.DB()

    search = db.select(where={column:value})
    #there exists cases where there's only one speaker

    
    id_checked = set()
    for row in search:
        #could be subsession with same val
        if row.get('id') in id_checked:
            continue

        id_checked.add(row.get('id'))
        print_event(row)
        #look for subsession
        if(row.get('type')=='Session'):
            #all subsessions should have these similar properties
            findSub = {'date': row.get('date'),
                       'time_Start': row.get('time_start'),
                       'type':'Sub',
                       }
            sub = db.select(where = findSub)

            if sub:
                for s in sub:
                    if s.get('id') in id_checked:
                        continue
                    print_event(s)
                    id_checked.add(s.get('id'))
    

