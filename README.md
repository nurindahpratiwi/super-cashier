
## Super Cashier Project

Super cashier app ini merupakan aplikasi perhitungan kasir
sederhana berbasis bahasa pemrograman Python yang terhubung dengan MySQL.
Super cashier app ini berisi fitur-fitur perhitungan kasir sehingga user dapat melakukan transaksi secara mandiri (*self-service*).

## Features

- [x]   User dapat memasukkan nama barang, jumlah item, dan harga per item
- [x]   Jika terdapat kesalahan dalam memasukkan nama item/jumlah item/harga per item, user dapat mengubahnya dengan *rule* sebagai berikut:
    - [x]  Update nama item: input __**nama item lama**__ dan masukkan __**nama item (update)**__
    - [x]  Update jumlah item: input __**nama item lama**__ dan masukkan __**jumlah item (update)**__
    - [x]  Update harga per item: input __**nama item lama**__ dan masukkan __**harga per item (update)**__
- [x]   Jika user batal membeli belanjaan, user dapat menghapus item tersebut dengan memasukkan __**nama item**__
- [x]   User dapat menghapus seluruh keranjang belanjaan dengan cara melakukan __**reset transaction**__
- [x]   Customer dapat melakukan pengecekan ulang terhadap item yang telah diinput
- [x]   Customer dapat melihat total harga dan mendapatkan potongan (diskon) jika barang belanjaan memenuhi minimal harga diskon.
## Requirements

- Pastikan Anda telah menginstall python versi terbaru, super cashier app ini menggunakan Python versi:
```Python
python --version
Python 3.8.10
```
- Install MySQL versi terbaru, super cashier ini menggunakan Mysql versi:
```
mysql --version
mysql  Ver 8.0.30
```
- Install mysql connector python: [docs mysql connector]
```Python
pip install mysql-connector-python
```
- Buat database bernama `cashier` dan table bernama `transaction`

[docs mysql connector]: https://pypi.org/project/mysql-connector-python/
## Module Explanation
- Module **main.py** berisi daftar menu pada aplikasi super cashier
- Module **transaction.py** berisi daftar fungsi yang didefinisikan sebagai fitur aplikasi
- Module **user_db.py** berisi informasi mengenai nama database, username dan password MySQL
## Code Explanation
- _Function_ untuk **menambahkan item** barang belanja
```python
def add_item(self):
    #list variabel yang ingin ditambahkan
    list_item = (item_name, item_qty, item_price)

    #query untuk menambahkan nama, jumlah dan harga item ke dalam database
    add_query = """INSERT INTO transaction(nama_item, jumlah_item, harga) VALUES(%s, %s, %s)"""
    
    #eksekusi query dengan perintah execute
    cursor.execute(add_query, list_item)

    #send hasil eksekusi ke dalam database
    mydb.commit()
```

- _Function_ untuk **menghapus salah satu item** barang belanja
```python
def delete_item(self):
    #list input yang dibutuhkan untuk mengubah nama
    list_item = (item_name,)

    #query untuk menghapus sebuah item berdasarkan nama yang diinput
    delete_query = """DELETE FROM transaction WHERE nama_item = %s"""
    
    #eksekusi query delete item dengan perintah execute
    cursor.execute(delete_query,list_item)
    
    #send hasil eksekusi ke dalam database
    mydb.commit()
```

- _Function_ untuk **menghapus seluruh item** barang belanja
```python
def reset_transaction(self):
    #query untuk langsung menghapus seluruh row dari tabel transaction
    delete_query = """ DELETE from transaction """
    
    #eksekusi query delete all dengan perintah execute
    cursor.execute(delete_query)

    #send hasil eksekusi ke dalam database
    mydb.commit()
    print("\nData berhasil di hapus")
```

- _Function_ untuk **mengecek item** barang belanja
```python
def check_order(self):
    #query untuk melakukan pengecekan barang
    check_query = """ SELECT nama_item, jumlah_item, harga, 
                jumlah_item*harga AS total_harga FROM transaction """

    #eksekusi query cek dengan perintah execute
    cursor.execute(check_query)

    #variabel untuk menyimpan seluruh data yang diambil dari query
    rows=cursor.fetchall()
```

- _Function_ untuk **mengecek total bayar dan diskon** barang belanja
```python
def add_item(self):
    #query untuk menghitung total bayar dari harga item
    price_query = """SELECT SUM(jumlah_item*harga) AS total_harga FROM transaction"""
    
    #eksekusi query hitung dengan perintah execute
    cursor.execute(price_query)

    #hasil query disimpan dalam variabel result
    result = cursor.fetchall()[0][0]
```

- _Function_ untuk **mengubah nama item** barang belanja
```python
def update_item_name(self):
    #list variabel nama yang ingin dieksekusi
    list_item = [item_name_new, item_name]

    #query untuk mengubah nama sesuai dengan input user
    update_query = """UPDATE transaction SET nama_item=%s WHERE nama_item=%s"""
    
    #eksekusi query ubah nama dengan perintah execute
    cursor.execute(update_query, list_item)

    #send hasil eksekusi ke dalam database
    mydb.commit()
```

- _Function_ untuk **mengubah jumlah item** barang belanja
```python
def update_item_qty(self):
    #list variabel jumlah yang ingin dieksekusi
    list_item = [item_qty_new, item_name]

    #query untuk mengubah jumlah item berdasarkan nama yang diinput
    update_query = """UPDATE transaction SET jumlah_item=%s WHERE nama_item=%s"""
    
    #eksekusi query ubah jumlah item dengan perintah execute
    cursor.execute(update_query, list_item)

    #send hasil eksekusi ke dalam database
    mydb.commit()
```

- _Function_ untuk **mengubah harga item** barang belanja
```python
def update_item_price(self):
    #list variabel harga yang ingin dieksekusi
    list_item = [item_price_new, item_name]

    #eksekusi query ubah harga per item dengan perintah execute
    update_query = """UPDATE transaction SET harga=%s WHERE nama_item=%s"""
    
    #eksekusi query ubah harga item dengan perintah execute
    cursor.execute(update_query, list_item)

    #send hasil eksekusi ke dalam database
    mydb.commit()
```
## Flowchart
![flow-chart](https://user-images.githubusercontent.com/22311240/203033408-7d8a75b1-1354-4c43-b979-66efffbfaab1.jpg)

## How to Start Program
- Clone project ini ke dalam direktori lokal Anda.
- Definisikan variabel-variabel di module **user_db.py** dan simpan.
- Buka terminal dan sesuaikan lokasi direktori lokal.
- Jalankan module python **main.py** di terminal.
## Test Case
- Penambahan keranjang belanja
![image](https://drive.google.com/uc?export=view&id=1WhwZ6A-M5UOZH8Qj2hvKFuan8DktGku3)

- Cek keranjang belanja (hasil input)
![image](https://drive.google.com/uc?export=view&id=1F9qzMQEwRCyHjdcRmUFQ-TsYtQo19LN6)

- Hapus salah satu item di keranjang belanja
![image](https://drive.google.com/uc?export=view&id=1bDD8EC4gc9c33Inc6oNx_gEI32mXxxuv)

- Cek keranjang belanja
![image](https://drive.google.com/uc?export=view&id=13BpAXJ0e8hX-kb1sJHu5RpzVhqsMD8Fi)

- Hapus seluruh keranjang belanja
![image](https://drive.google.com/uc?export=view&id=1VG5WsUr2JebglVHVwwoYTWshxAGeXLg7)

- Cek  keranjang belanja (setelah reset)
![image](https://drive.google.com/uc?export=view&id=10PKZoBhAr0akdreeX4ZPPtRU-6ajZ1h4)

- Cek total barang (input barang sesuatu test case)
![image](https://drive.google.com/uc?export=view&id=1BWF_gxvcyrrTXavb0QnYVHd8SzlvZHYX)

- Cek total diskon
![image](https://drive.google.com/uc?export=view&id=18YEtdS59G8nyCiIL4yyxT6bhjK9jC76P)

- Ubah salah satu item di keranjang belanja
    - Ubah nama item
    ![image](https://drive.google.com/uc?export=view&id=1OX6ap7vuck-K2G3HWA2cEoV6LWnnMo03)
    
    - Ubah jumlah item
    ![image](https://drive.google.com/uc?export=view&id=1vie6APezdOXV2gjDZybHd15TCrSwHveC)
    
    - Ubah harga per item
    ![image](https://drive.google.com/uc?export=view&id=1q1lpZimw3ULttUuYWT0xAhkKIXa8nITA)

- Cek keranjang belanja (setelah ubah data)
![image](https://drive.google.com/uc?export=view&id=1PsDeJ3245s1GGOrMpiB30xX8PXG40CBk)




## Conclusion

- Super cashier ini telah sukses melewati test case, diharapkan kedepannya dapat diubah menjadi program yang berbasis class/objek
- Saran/perbaikan program sangat terbuka jika ditemukan `bug` atau `error` oleh user.


## Tech Stack

- **Language** = Python
- **Database** = MySQL
