data={}
while True:
    c = input('tambah? tampilkan? hapus? ubah?: ')
    if c == ('tambah'):
        def tambah():
            print('tambah mahasiswa: ')
            nama = input("masukan nama: ")
            nim = input('masukan nim: ')
            nilaitugas = int(input('masukan nilai tugas: '))
            nilaiuts = int(input('masukan nilai uts: '))
            nilaiuas = int(input('masukan nilai uas: '))
            nilaiakhir = (0.30 * nilaitugas) + (0.35 * nilaiuts) + (0.35 * nilaiuas)
            data[nama]= nim,nilaitugas,nilaiuts,nilaiuas,nilaiakhir
        tambah()
        print("data berhasil ditambahkan")
    elif c == ('tampilkan'):
        if data.items():
            def tampilkan():
             print("\n                      DAFTAR NILAI MAHASISWA                    ")
             print("==================================================================")
             print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
             print("==================================================================")
             i = 0
             for x in data.items():
                 i += 1
                 print(f"""| {i}  |     {x[0]}    | {x[1][0]} |   {x[1][1]}  |  {x[1][2]}  |  {x[1][3]}    |  {x[1][4]}  |""")
            tampilkan()
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")
    elif c == ("hapus"):
        def hapus():
         nama = input('masukan nama yang akan dihapus: ')
         if nama in data.keys():
             del data[nama]
             print('data telah dihapus!')
         else:
             print("data mahasiswa tidak terdaftar")
        hapus()
    elif c == ('ubah'):
        def ubah():
         print('mengubah data mahasiswa')
         nama = input('masukan nama: ')
         if nama in data.keys():
             nim = input('masukan nim baru')
             nilaitugas = int(input('masukan nilai tugas: '))
             nilaiuts = int(input('masukan nilai uts: '))
             nilaiuas = int(input('masukan nilai uas: '))
             nilaiakhir = (0.30 * nilaitugas) + (0.35 * nilaiuts) + (0.35 * nilaiuas)
             data[nama]= nim,nilaitugas,nilaiuts,nilaiuas,nilaiakhir
             print("data berhasil di perbarui!")
         else:
             print('data tidak ditemukan!')
        ubah()
    else:
        print("masukan input dengan benar")