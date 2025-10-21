user= {
    'admin':{'pass':'dewa'},
    'user':{'pass':'rakyat'},
}
import os
data={}

while True:
    os.system('cls')
    pilih=input('''
                    |===============================|
                    |        halaman login          |
                    |===============================|
                    |1. register                    |
                    |2. login                       |
                    |3. keluar                      |
                    |===============================|
                    > ''')
    if pilih == '1':
        usr=input('masukkan username = ')
        pas=input('masukkan password = ')
        if usr in user:
            print('Username sudah ada, silahkan coba lagi')
        else:
            user[usr] = {'pass': pas}
            print('Selamat akun berhasil didaftarkan!')
    elif pilih == '2':
        usr=input('masukkan username = ')
        pas=input('masukkan password = ')
        if usr in user and user[usr]['pass']==pas:
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
                        data[nama] = {
                            'nisn': nisn, 
                            'angkatan': angkatan, 
                            'tim': tim
                        }

                    elif pilih == '2':
                        if len(data)==0:
                            print('data masih belum ada')
                        else : 
                            for key, value in data.items():
                                print(f'\nNama = {key}\nNISN = {value['nisn']}\nAngkatan = {value['angkatan']}\nTim = {value['tim']}')

                    elif pilih == '3':
                        nama_lama = input('Nama anggota yang akan diubah = ')
                        if nama_lama in data:
                            nama_baru = input('Nama = ')
                            nisn_baru = input('NISN = ')
                            angkatan_baru = input('Angkatan = ')
                            tim_baru = input('Tim = ')
                            data[nama_baru] = {
                                    'nisn': nisn_baru, 
                                    'angkatan': angkatan_baru, 
                                    'tim': tim_baru
                                }
                            if nama_baru != nama_lama:
                                del data[nama_lama]
                            print('Data anggota berhasil diubah')
                        else:
                                print('Nama tidak ditemukan.')

                    elif pilih == '4': 
                        hapus = input('Nama anggota yang ingin dihapus = ')
                        if hapus in data:
                                del data[hapus]
                                print('Data berhasil dihapus')
                        else:
                            print('Anggota tidak ditemukan.')
                    
                    elif pilih == '5':
                        print('baik terimakasih telah menggunakan program ini')
                        break
                
            else: 
                print('''
                    |===============================|
                    |pilih opsi yang ingin dilakukan|
                    |===============================|
                    |1. tambah data                 |
                    |2. tampilkan data              |
                    |3. keluar                      |
                    |===============================|
                    ''')
                while True:
                    pilih = input('> ')
                    if pilih == '1':
                        nama=input('nama = ')
                        nisn=input('nisn = ')
                        angkatan=input('angkatan = ')
                        tim=input('tim = ')
                        data[nama] = {
                            'nisn': nisn, 
                            'angkatan': angkatan, 
                            'tim': tim
                        }

                    elif pilih == '2':
                        if len(data)==0:
                            print('data masih belum ada')
                        else : 
                            for key, value in data.items():
                                print(f'\nNama = {key}\nNISN = {value['nisn']}\nAngkatan = {value['angkatan']}\nTim = {value['tim']}')
                    
                    elif pilih == '3':
                        os.system('cls')
                        print('baik! kembali ke halaman login')
                        break
                    
                    else:
                        print('pilihan tidak ada')
                    
        else : print('username atau password salah silahkan coba lagi')

    elif pilih == '3':
        os.system('cls')
        print('baik! selamat tinggal')
        break

    else : print('pilihan tidak ada')