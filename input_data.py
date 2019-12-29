def input_nilai():
    from model.daftar_nilai import tambah_data
    while (True):
        nama = input("Nama Mahasiswa   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("Masukan NIM      : "))
            if nim == '':
                print('Masukan Nim dengan Angka')
        except ValueError:
            print('Masukan Nim dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("Nilai Tugas      : "))
            if tugas == '':
                print('Masukan Nilai Tugas dengan Angka')
        except ValueError:
            print('Masukan Nilai Tugas dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("Nilai UTS        : "))
            if uts == '':
                print('Masukan Nilai UTS dengan Angka')
        except ValueError:
            print('Masukan Nilai UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("Nilai UAS        : "))
            if uas == '':
                print('Masukan Nilai UAS dengan Angka')
        except ValueError:
            print('Masukan Nilai UAS dengan Angka')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)

def ubahdata():
    from model.daftar_nilai import ubah_data
    ubah_data(nama=input("Masukan Nama untuk mengubah data : "))

def hapusdata():
    from model.daftar_nilai import hapus_data
    hapus_data(nama=input("Masukan Nama untuk menghapus Daftar Nilai : "))

def caridata():
    from model.daftar_nilai import cari_data
    cari_data(nama=input("Masukan Nama yang dicari : "))