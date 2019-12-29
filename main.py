from view.view_nilai import pilihan, lihat_data, hasil_pencarian, false

from view.input_data import input_nilai, ubahdata, caridata, hapusdata

while True:
    pilihan()
    c = input("\nPilih Menu :")
    if c.lower() == 'k':
        break

    elif c.lower() == 't':
        input_nilai()

    elif c.lower() == 'u':
        ubahdata()

    elif c.lower() == 'h':
        hapusdata()

    elif c.lower() == 'c':
        hasil_pencarian()

    elif c.lower() == 'l':
        lihat_data()

    else:
        false()