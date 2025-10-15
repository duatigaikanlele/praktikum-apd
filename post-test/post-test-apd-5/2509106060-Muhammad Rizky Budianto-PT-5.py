user= {
    'admin':{'pass':'dewa'},
    'user':{'pass':'rakyat'},
}
import os
data=[]

while True:
    pilih=input("""
                    |===============================|
                    |        halaman login          |
                    |===============================|
                    |1. register                    |
                    |2. login                       |
                    |3. keluar                      |
                    |===============================|
                    > """)
    if pilih == '1':
        os.system('cls')
        usr=input('masukkan username = ')
        pas=input('masukkan password = ')
        if usr in user:
            print("Username sudah ada, silahkan coba lagi")
        else:
            user[usr] = {"pass": pas}
            print(f"Selamat akun berhasil didaftarkan!")
    elif pilih == '2':
        os.system('cls')
        usr=input('masukkan username = ')
        pas=input('masukkan password = ')
        if usr in user and user[usr]["pass"]==pas:
            print('=====login berhasil=====')
            if usr == 'admin':
                print('''
                    |===============================|
                    |pilih opsi yang ingin dilakukan|
                    |===============================|
                    |1. tambah data                 |
                    |2. tampilkan data              |
                    |3. ubah data                   |
                    |4, hapus data                  |
                    |5. keluar                      |
                    |===============================|
                    ''')
                while True:
                    pilih = input('> ')
                    if pilih == '1':
                        nama=input('nama = ')
                        nisn=input('nisn = ')
                        angkatan=input('angkatan = ')
                        tim=input('tim = ')
                        data.append([nama, nisn, angkatan, tim])

                    elif pilih == '2':
                        if len(data)==0:
                            print('data masih belum ada')
                        else : 
                            for i in range(len(data)):
                                print(f'\nAnggota ke-{i+1}\nNama = {data[i][0]}\nNisn = {data[i][1]}\nAngkatan = {data[i][2]}\nTim = {data[i][3]}')

                    elif pilih == '3':
                        data_lama = input('Nama anggota yang akan diubah = ')
                        for i in range(len(data)):
                            if data[i][0] == data_lama:
                                nama_baru = input('Nama = ')
                                nisn_baru = input('NISN = ')
                                angkatan_baru = input('Angkatan = ')
                                tim_baru = input('Tim = ')
                                data[i] = [nama_baru, nisn_baru, angkatan_baru, tim_baru]
                                print('Data anggota berhasil diubah.')
                                break
                        else:
                            print('Nama tidak ditemukan.')

                    elif pilih == '4': 
                        hapus = input('Nama anggota yang ingin dihapus = ')
                        for i in range(len(data)):
                            if data[i][0] == hapus:
                                del data[i]
                                print(f'Data {hapus} berhasil dihapus.')
                                break
                        else:
                            print('Anggota tidak ditemukan.')
                    
                    elif pilih == '5':
                        print('baik terimakasih telah menggunakan program ini')
                        break
                
            else: 
                print("""
                    |===============================|
                    |pilih opsi yang ingin dilakukan|
                    |===============================|
                    |1. tambah data                 |
                    |2. tampilkan data              |
                    |3. keluar                      |
                    |===============================|
                    """)
                while True:
                    pilih = input('> ')
                    if pilih == '1':
                        nama=input('nama = ')
                        nisn=input('nisn = ')
                        angkatan=input('angkatan = ')
                        tim=input('tim = ')
                        data.append([nama, nisn, angkatan, tim])

                    elif pilih == '2':
                        if len(data)==0:
                            print('data masih belum ada')
                        else : 
                            for i in range(len(data)):
                                print(f'\nAnggota ke-{i+1}\nNama = {data[i][0]}\nNisn = {data[i][1]}\nAngkatan = {data[i][2]}\nTim = {data[i][3]}')
                    
                    elif pilih == '3':
                        print('baik! kembali ke halaman login')
                        break
                    
                    else:
                        print('pilihan tidak ada')
                    
        else : print('username atau password salah silahkan coba lagi')

    elif pilih == '3':
        print('baik! selamat tinggal')
        break

    else : print('pilihan tidak ada')