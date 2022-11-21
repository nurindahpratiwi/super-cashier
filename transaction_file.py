"""
"""

#Import library yang akan digunakan
import mysql.connector as mysql
import user_db
from sys import exit

hostname = user_db.hostname 
user = user_db.user 
password = user_db.password 
db = user_db.db  

mydb = mysql.connect(host=hostname, user=user, password=password, database=db)

# Membuat object cursor yang terkoneksi dengan database db
cursor = mydb.cursor()

class Transaction:
    def add_item(self):
        print("-"*50)
        print("MASUKKAN ITEM BARU")

        item_name = input("Nama item : ")
        item_qty = int(input("Jumlah item : "))
        item_price = int(input("Harga per item : "))

        try:
            list_item = (item_name, item_qty, item_price)
            add_query = """INSERT INTO transaction(nama_item, jumlah_item, harga) VALUES(%s, %s, %s)"""
            cursor.execute(add_query, list_item)
            mydb.commit()
            print("\nData belanja Anda berhasil diinput.\n")
        except mysql.connector.Error as err:
            print("Gagal input item belanja Anda: {}".format(err))
        
        return menu()
    
    def delete_item(self):
        print("-"*50)
        print("MASUKKAN ITEM YANG INGIN ANDA HAPUS")

        item_name = input("\nNama item : ")

        try:
            list_item = (item_name,)
            delete_query = """DELETE FROM transaction WHERE nama_item = %s"""
            cursor.execute(delete_query,list_item)
            mydb.commit()
            print("\nData belanja Anda berhasil dihapus.\n")
        except mysql.connector.Error as err:
            print("Gagal hapus data belanja Anda: {}".format(err))

        return menu()

    def update_item_name(self):
        print("-"*50)
        print("MASUKKAN NAMA ITEM YANG INGIN ANDA UBAH")

        item_name = input("\nNama item : ")
        item_name_new = input("Nama item (update): ")

        try:
            list_item = [item_name_new, item_name]
            update_query = """UPDATE transaction SET nama_item=%s WHERE nama_item=%s"""
            cursor.execute(update_query, list_item)
            mydb.commit()
            print("\nData belanja Anda berhasil diubah.\n")
        except mysql.connector.Error as err:
            print("Gagal update nama item pada data belanja Anda: {}".format(err))
        
        return menu()

    def update_item_qty(self):
        print("-"*50)
        print("MASUKKAN JUMLAH ITEM YANG INGIN ANDA UBAH")

        item_name = input("\nNama item : ")
        item_qty_new = int(input("Jumlah item (update): "))

        try:
            list_item = [item_qty_new, item_name]
            update_query = """UPDATE transaction SET jumlah_item=%s WHERE nama_item=%s"""
            cursor.execute(update_query, list_item)
            mydb.commit()
            print("\nData belanja Anda berhasil diubah.\n")
        except mysql.connector.Error as err:
            print("Gagal update jumlah item pada data belanja Anda: {}".format(err))
        
        return menu()
        

    def update_item_price(self):
        print("-"*50)
        print("MASUKKAN HARGA ITEM YANG INGIN ANDA UBAH")

        item_name = input("\nNama item : ")
        item_price_new = int(input("Harga per item (update): "))

        try:
            list_item = [item_price_new, item_name]
            update_query = """UPDATE transaction SET harga=%s WHERE nama_item=%s"""
            cursor.execute(update_query, list_item)
            mydb.commit()
            print("\nData belanja Anda berhasil diubah.\n")
        except mysql.connector.Error as err:
            print("Gagal update harga item pada data belanja Anda: {}".format(err))
        
        return menu()


    def update_item(self):
        print("-"*50)
        print("TRANSAKSI APA YANG INGIN ANDA UPDATE?")
        print("1. Ubah Nama Item")
        print("2. Ubah Jumlah Item")
        print("3. Ubah Harga Item\n")

        choose = int(input("\nMasukkan jenis transaksi update: "))
        try:
            if choose == 1:
                self.update_item_name()
            elif choose == 2:
                self.update_item_qty()
            elif choose == 3:
                self.update_item_price()
            else:
                print("\nHarap masukkan angka yang tertera!")
        except mysql.connector.Error as err:
            print("Sepertinya angka yang Anda masukkan salah: {}".format(err))

        return menu()

    def reset_transaction(self):
        print("-"*50)
        print("APAKAH ANDA YAKIN MENGHAPUS SEMUA TRANSAKSI?")

        ensure_key = int(input("\nTekan 1 untuk melanjutkan dan any key untuk batal: "))

        try:
            if ensure_key == 1:
                delete_query = """ DELETE from transaction """
                cursor.execute(delete_query)
                mydb.commit()
                print("\nData berhasil di hapus")
            else:
                print("\nAnda telah membatalkan reset transaksi")
                menu()

        except mysql.connector.Error as err:
            print("Gagal hapus data belanja Anda: {}".format(err))

        return menu()

    def check_order(self):
        try:
            check_query = """ SELECT nama_item, jumlah_item, harga, 
                jumlah_item*harga AS total_harga FROM transaction """

            cursor.execute(check_query)
            rows=cursor.fetchall()
            print("-"*50)
            print("DAFTAR BELANJA ANDA")
            print("-"*50)

            # DATA PADA SQL ADALAH TUPLES
            template = "{0:15}|{1:10}|{2:11}|{3:7}" # lebar kolom = 15, 10, 11, 7
            print (template.format("NAMA ITEM", "JUMLAH", "HARGA", "TOTAL HARGA")) # header
            print("-"*50)
            for row in rows: 
                print (template.format(*row))
            
            print("\nPemesanan sudah sesuai.\nJika Anda ingin tambah/ubah/keluar silakan kembali ke menu.")
            key = int(input("\n\nTekan 1 untuk kembali ke menu: "))
            while key!=0:
                try:
                    if key == 1:
                        menu()
                    else:
                        break
                except ValueError:
                    print("Error Input!")

        except ValueError:
            print("\nPengecekan order Anda gagal.")

        return menu()

    def total_price(self):
        try:
            price_query = """SELECT SUM(jumlah_item*harga) AS total_harga FROM transaction"""
            cursor.execute(price_query)
            result = cursor.fetchall()[0][0]
            result = float(result)
            if result > 200000:
                print ("\nAnda mendapatkan diskon 5%")
                result_diskon = result*0.95
                print(f"Total belanja Anda adalah: {result}")
                print(f"Total belanja Anda setelah diskon adalah: {result_diskon}")
            elif result > 300000:
                print ("\nAnda mendapatkan diskon 8%")
                result_diskon = result*0.92
                print(f"Total belanja Anda adalah: {result}")
                print(f"Total belanja Anda setelah diskon adalah: {result_diskon}")
            elif result > 500000:
                print ("\nAnda mendapatkan diskon 10%")
                result_diskon = result*0.90
                print(f"Total belanja Anda adalah: {result}")
                print(f"Total belanja Anda setelah diskon adalah: {result_diskon}")
            else:
                print(f"Total belanja Anda adalah: {result}")
                print ("\nMaaf Anda belum mendapatkan diskon. Yuk belanja lagi!")      
                

        except mysql.connector.Error as err:
            print("Sepertinya angka yang Anda masukkan salah: {}".format(err))
        
        return menu()
        


def menu():
    """Fungsi untuk menampilkan daftar tugas.
    """
    print("-"*50)
    print("SELAMAT DATANG DI SELF SERVICE SUPERMARKET WIWAAW")
    print("-"*50)

    print("1. Tambah Isi Keranjang Belanja Anda")
    print("2. Ubah Keranjang Belanja Anda")
    print("3. Hapus Item Belanja Anda")
    print("4. Cek Keranjang Belanja Anda")
    print("5. Hapus Semua Keranjang Belanja Anda")
    print("6. Cek Total Bayar dan Diskon")
    print("0. Keluar\n")
    

    choice = int(input('Masukkan Pilihan Anda : '))
    Trx = Transaction()

    while choice != 0:
        try:
            if choice == 1:
                Trx.add_item()
            elif choice == 2:
                Trx.update_item()
            elif choice == 3:
                Trx.delete_item()
            elif choice == 4:
                Trx.check_order()
            elif choice == 5:
                Trx.reset_transaction()
            elif choice == 6:
                Trx.total_price()
            else:
                print("\nGunakan nomor yang tertera pada menu")
                menu()
        except ValueError:
            print("Error input!")
    
    if choice == 0:
        exit()
    
    return

    