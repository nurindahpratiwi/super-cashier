
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

- _Function_ untuk **mengecek total bayar dan diskon** barang belanja
```python
def total_price(self):
    try:
        # query untuk melakukan penjumlahan jumlah item dikali dengan harga
        price_query = """SELECT SUM(jumlah_item*harga) AS total_harga FROM transaction"""

        #eksekusi query penjumlahan dengan perintah execute
        cursor.execute(price_query)

        #variabel untuk menyimpan seluruh data yang diambil dari query
        result = cursor.fetchall()[0][0]
        result = float(result)

        #condition ini untuk mengecek apakah total belanja eligible untuk diberikan diskon atau tidak
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

```



## Flowchart
<img src="https://user-images.githubusercontent.com/22311240/203033408-7d8a75b1-1354-4c43-b979-66efffbfaab1.jpg" width=70% height=70%>

## How to Start Program
- Clone project ini ke dalam direktori lokal Anda.
- Definisikan variabel-variabel di module **user_db.py** dan simpan.
- Buka terminal dan sesuaikan lokasi direktori lokal.
- Jalankan module python **main.py** di terminal.
## Test Case
- Penambahan keranjang belanja
<img src="https://user-images.githubusercontent.com/22311240/203088435-c4cc597a-7516-43b3-98c0-606e57e51631.jpg" width=50% height=50%>
<img src="https://user-images.githubusercontent.com/22311240/203089285-c6050cbc-96f4-4ae0-b6b8-0fbfb0510bc3.jpg" width=50% height=50%>

- Cek keranjang belanja
<img src="https://user-images.githubusercontent.com/22311240/203089475-772b1c79-5868-46e6-ad88-dbc11efeb83a.jpg" width=50% height=50%>

- Hapus salah satu item di keranjang belanja
<img src="https://user-images.githubusercontent.com/22311240/203088804-9e56a0c3-3a1f-42ff-bd9d-80e74c2d3c28.jpg" width=50% height=50%>

- Hapus seluruh keranjang belanja
<img src="https://user-images.githubusercontent.com/22311240/203089613-bbe0c57c-a12d-422c-b4ba-abca92192c06.jpg" width=50% height=50%>

- Cek  keranjang belanja (setelah reset)
<img src="https://user-images.githubusercontent.com/22311240/203089745-34ee1cf8-5c4e-427f-ae35-516a2bc2cab5.jpg" width=50% height=50%>

- Cek total barang (input barang sesuai test case)
<img src="https://user-images.githubusercontent.com/22311240/203090166-f1c571bf-ac41-473f-b259-27dfa89f3b83.jpg" width=50% height=50%>

- Cek total diskon
<img src="https://user-images.githubusercontent.com/22311240/203177963-42f15130-50d0-43d3-9afd-e76fea0d0976.jpg" width=50% height=50%>

- Ubah salah satu item di keranjang belanja
    - Ubah nama item
    <img src="https://user-images.githubusercontent.com/22311240/203090219-39def103-52af-40e4-b0d7-c355de6b4817.jpg" width=50% height=50%>

    - Ubah jumlah item
    <img src="https://user-images.githubusercontent.com/22311240/203090231-a6dabae3-5a48-49b8-beef-d19cfe69ec83.jpg" width=50% height=50%>

    - Ubah harga per item
    <img src="https://user-images.githubusercontent.com/22311240/203090246-faa3ef86-4505-482f-99c1-ba59832a5417.jpg" width=50% height=50%>

- Cek keranjang belanja (setelah ubah data)
<img src="https://user-images.githubusercontent.com/22311240/203090260-2578fdbf-3170-4b11-b502-ea4cb86b5fb5.jpg" width=50% height=50%>



## Conclusion

- Super cashier ini telah sukses melewati test case, diharapkan kedepannya dapat diubah menjadi program yang berbasis class/objek
- Saran/perbaikan program sangat terbuka jika ditemukan `bug` atau `error` oleh user.


## Tech Stack

- **Language** = Python
- **Database** = MySQL
