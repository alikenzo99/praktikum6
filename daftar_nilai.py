daftar = {}


def tambah_data(nama, nim, tugas, uts, uas):
    akhir = round((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
    daftar[nama] = nim, tugas, uts, uas, akhir


def ubah_data(nama):
    if nama in daftar.keys():
        del daftar[nama]
        print("\n===Masukan Pembaruan Data===")
        from view.input_data import input_data
        input_data()
    else:
        print("=============================================")
        print("| Data {} tidak ditemukan |".format(nama))
        print("=============================================")


def cari_data():
    print("Cari Daftar Nilai Mahasiswa")
    nama = input("Nama Mahasiswa : ")
    if nama in daftar.keys():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("====================================================================================================")
        print("Data {0} adalah ('Nim',Tugas,UTS,UAS,Akhir) => {1}" \
              .format(nama, daftar[nama]))
        print("====================================================================================================")
        print("")
    else:
        print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
        print("=================================================================")
        print("               Daftar Nilai {0} tidak ada                      " \
              .format(nama))
        print("=================================================================")
        print("")


def hapus_data(nama):
    if nama in daftar.keys():
        del daftar[nama]
        print("Daftar Nilai {} berhasil dihapus".format(nama))
        return True
    else:
        print("===========================")
        print("| Daftar Nilai {} tidak ditemukan |".format(nama))
        print("===========================")
        return False
