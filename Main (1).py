import member.py
print('1.Tambah Member')
print('2.Ubah Member')
print('3.Hapus Member')
print('4.Tampilkan Member')
menu2 = int(input('[Member]pilih:'))

if(menu2==1):
    nama_barang=input('Nama Barang:')
    jumlah_barang=input('Jumlah_Barang:')
    harga_barang=[nama_barang,jumlah_barang]
    member.add(data)
elif(menu2==2):
    id_member=input('No.Member:')
    nama_barang=input('Nama Barang:')
    harga_barang=input('Nama Barang,Jumlah Barang:')
    data=[nama_barang,jumlah_barang,id_member]
    member.edit(data)
elif(menu2==3):
    id_member=input('No.Member:')
    data=[id_member]
    member.search(data)
    confirm=input('Yakin menghapus member ini? [Y/N]:')
    if(confirm=='Y'):
        member.delete(data)
    else:
        print('Tidak jadi menghapus data member!')
elif(menu2==4):
    member.show()
else:
    print('menu tidak tersedia')
            
