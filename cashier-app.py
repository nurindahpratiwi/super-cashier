import mysql.connector
from mysql.connector import errorcode
import pandas as pd
from datetime import date, datetime, timedelta
import warnings
warnings.filterwarnings('ignore')
import user_db

hostname = user_db.hostname 
user = user_db.user 
password = user_db.password 
db = user_db.db  

myconn = mysql.connector.connect(host=hostname, user=user,
                               password=password, database=db, auth_plugin='mysql_native_password')

# Membuat object cursor yang terkoneksi dengan database db
cursor = myconn.cursor()

class Transaction:
    def __init__(self, item_name, item_qty, item_price):
        self.item_name = item_name
        self.item_qty = item_qty
        self.item_price = item_price

    def add_item 