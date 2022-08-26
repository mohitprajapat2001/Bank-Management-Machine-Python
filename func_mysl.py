from db_connector import *
def db_query(query):
    mycursor.execute(f'{query}')
    return mycursor
def loopShow(temp):
    for i in temp:
        return i