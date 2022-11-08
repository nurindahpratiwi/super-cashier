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
    def add_item(self, item_name, item_price) :
        print("-"*60)
        print("MASUKKAN ITEM BARU")
        print("-"*60)

        item_name = input("Nama item : ")
        item_qty = int(input("Jumlah item : "))
        item_price = int(input("Harga per item : "))
        
        try:
            list_item = {'item_name': item_name,'item_qty': item_qty,'item_price': item_price}
            add_item = """ INSERT INTO transaction(nama_item, jumlah_item, harga)
                        VALUES(%(item_name)s, %(itqm_qty)s, %(item_price)s) """
            cursor.execute(add_item,list_item)
            myconn.commit()
            print("\nData belanja Anda berhasil diinput.\n")
        except mysql.connector.Error as err:
            print("\nPenambahan data belanja Anda gagal. Periksa kembali input Anda.\n")
        
        menu()
    
    def update_item_name(self, item_name, item_name_upd):
        try:
            list_item = {'item_name': item_name, 'item_name_upd': item_name_upd}
            upd_item_name = """UPDATE transaction SET nama_item =%(item_name_upd)s WHERE nama_item =%(item_name)s"""
            cursor.execute(upd_item_name,list_item)
            myconn.commit()
            print("\nData belanja Anda berhasil diupdate.\n")
        except mysql.connector.Error as err:
            print("\nPerubahan data belanja Anda gagal. Periksa kembali input Anda.\n")

    def update_item_qty(item_name, item_qty_upd):
        pass

    def update_item_price(item_price, item_price_upd):
        pass

    def delete_item(item_name):
        pass

    def reset_transaction():
        pass

    def check_order():
        try:
            item_list = """ SELECT nama_item, jumlah_item, harga, 
                jumlah_item*harga AS total_harga FROM transaction """
            cursor.execute(item_list)
            rows=cursor.fetchall()
            print("-"*60)
            print("DAFTAR BELANJA ANDA")
            print("-"*60)
            for row in rows:
                print(row)
        except mysql.connector.Error as err:
            print("\nPengecekan order Anda gagal, kemungkikan keranjang belanja Anda kosong atau Anda dapat periksa kembali input Anda .\n")

        menu()

    def total_price():
        total = """SELECT SUM(total_harga) grand_total FROM transaction"""

        menu()

def menu():
    """Fungsi untuk menampilkan daftar tugas.
    """
    print("-"*60)
    print("SELAMAT DATANG DI SELF SERVICE SUPERMARKET XYZ")
    print("-"*60)
    print("1. Tambah Isi Keranjang Belanja Anda")
    print("2. Update Keranjang Belanja Anda")
    print("3. Check Keranjang Belanja Anda")
    print("0. Exit\n")
    
    choice = int(input('Masukkan Nomor Tugas : '))
    Trx = Transaction()

    try:
        if choice == 1:
            Trx.add_item()
        elif choice == 2:
            Trx.update_item_name()
        elif choice == 3:
            Trx.check_order()
        elif choice == 0:
            print("-"*60)
            print("Terima kasih telah mengunjungi Supermarket XYZ.")
            print("-"*60)
            pass
        else:
            print("Input Anda Salah.\n")
            menu()
    except:
        print("Input Anda salah.\n")
        menu()
        
menu()