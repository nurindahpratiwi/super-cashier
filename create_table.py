# Import library yang akan digunakan
import mysql.connector 
from mysql.connector import Error
import user_db
import create_db

# Memanggil function create_tables() dari module 'create_db'
# Function ini harus dijalankan
create_db.create_tables()

# Memanggil function insert_tables() dari module 'create_db'
#create_db.insert_tables()