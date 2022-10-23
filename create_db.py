import mysql.connector
from mysql.connector import Error
import user_db

hostname = user_db.hostname
user = user_db.user
password = user_db.password
db = user_db.db

myconn = mysql.connector.connect(host=hostname, user=user, passwd = password, database=db)

mycursor = myconn.cursor()

try:
    create_db = "CREATE DATABASE {}".format(db)
    mycursor.execute(create_db)
except:
    print(f"\nDatabase dengan nama '{db}' sudah dibuat.")
    print("Anda dapat langsung menjalankan module main.py")
    print("-"*60)

conn = mysql.connector.connect(host=hostname, user=user,
                               passwd=password, database=db)

cursor = conn.cursor()

def create_tables():
    try:
        TABLES = {}
        TABLES['transaction'] =  (""" CREATE TABLE IF NOT EXISTS transaction(
                            nama_item VARCHAR(50) NOT NULL KEY,
                            jumlah_item INT NOT NULL, 
                            harga INT) """)
        for table in TABLES:
            table_list = TABLES[table]
            cursor.execute(table_list)
    except:
        print(f"Tabel-tabel dalam database '{db}' sudah dibuat.")

def insert_tables():
    try:
        insert_transaction = """ INSERT INTO transaction(nama_item, jumlah_item, harga)
                        VALUES(%s, %s, %s) """
        cursor.execute(insert_tables)
        conn.commit()
    except:
        print(f"Tabel dan data contoh pada database '{db}' sudah dibuat.\n")
