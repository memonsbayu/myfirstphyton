import mysql.connector
import connect

db = connect.koneksi()

#menambahkan data
def add(data):
    cursor = db.cursor()
    sql="""INSERT INTO member (nama_barang,jumlah_barang,harga_barang,) VALUES (%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data member berhasil ditambahkan!'.format(cursor.rowcount))

#menaampilkan seluruh data
def show():
    cursor=db.cursor()
    sql="""SELECT*FROM member"""
    cursor.execute(sql)
    result=cursor.fetchall()
    print("+--+------------+---------------+----------------+--------------+")
    print("|ID|member\t|nama_barang\t|","jumlah_barang|","Harga_barang\t|")
    print("+--+------------+---------------+----------------+--------------+")
    for data in result:
        print("|",data[0],"|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"|")
        print("+--+------------+---------------+----------------+--------------+")

#mengubah data dalam tabel
def edit(data):
    cursor = db.cursor()
    sql="""UPDATE alat_olahraga=(%s),nama_barang=(%s),jumlah_barang=(%s),harga_barang=(%s)WHERE id=(%s)"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data barang berhsil dirubah!'.format(cursor.rowcount))

#meghapus data dari tabel member
def delete(data):
    cursor=db.cursor()
    sql="""DELETE FROM barang WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print('{}Data barang berhasil dihapus!'.format(cursor.rowcount))

#mencari data dalam tabel member
def search(data):
    cursor=db.cursor()
    sql="""SELECT*FROM barang WHERE id=%s"""
    cursor.execute(sql,data)
    result=cursor.fetchall()
    print("+--+------------+---------------+----------------+--------------+")
    print("|ID|barang\t|nama_barang\t|","jumlah_barang|","Harga_barang\t|")
    print("+--+------------+---------------+----------------+--------------+")
    for data in result:
        print("|",data[0],"|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"|")
        print("+--+------------+---------------+----------------+--------------+")
    
