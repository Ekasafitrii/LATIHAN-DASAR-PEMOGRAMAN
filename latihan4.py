while (True):
    nama_barang = input ('masukan nama barang : ')
    harga_barang1 = int (input('masukan harga barang : '))
    persen = input ("Masukan persen :")
    hargapersen = int(harga_barang1) * int (persen)/ 100
    jual = int (harga_barang1 + hargapersen)
    print ("Nama barang : ", nama_barang)
    print ("Harga barang :", harga_barang1)
    print (nama_barang, "dijual dengan harga : ", jual)
    apakahlanjut = input('apakah_ingin_lanjut_barang_yang_lain?_Y_lanjut_N_berhenti  ')
    if(apakahlanjut !='Y'):
        break