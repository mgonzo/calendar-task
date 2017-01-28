import os
import pymysql

def connect():
    user = os.environ['MARIADB_CALENDAR_USER']
    database = os.environ['MARIADB_CALENDAR_DATABASE']
    password = os.environ['MARIADB_CALENDAR_PASSWORD']
    return pymysql.connect(user=user, password=password, database=database)
