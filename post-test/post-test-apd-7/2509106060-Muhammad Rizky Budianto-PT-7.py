data={}
user= {
    'admin':{'pass':'dewa'},
    'user':{'pass':'rakyat'},
}
line = '=' * 25
import os

def tampil_data(n):
    if len(n)==0:
        print('data masih belum ada')
    else : 
        for key, value in n.items():
            print(f'\nNama = {key}\nNISN = {value['nisn']}\nAngkatan = {value['angkatan']}\nTim = {value['tim']}')

def register():
    usr=input('masukkan username = ')
    pas=input('masukkan password = ')
    if usr in user:
        print('Username sudah ada, silahkan coba lagi')
    else:
        user[usr] = {'pass': pas}
        print('Selamat akun berhasil didaftarkan!')

def login():
    usr=input('masukkan username = ')
    pas=input('masukkan password = ')
    if usr in user and user[usr]['pass']==pas:
        print('=====login berhasil=====')
        if usr == 'admin':
            menu_admin()
        else : menu_user()
    else : print('username atau password salah silahkan coba lagi')

def menu_login():
    while True:
        os.system('cls') 
        print(line)
        print('HALAMAN LOGIN')
        print(line)
        print('1. REGISTER')
        print('2. LOGIN')
        print('3. KELUAR')
        print(line)

        try:
            pilih = int(input('> ')) 
            if pilih == 1:
                register() 
            elif pilih == 2:
                login()    
            elif pilih == 3:
                os.system('cls')
                print('Baik! Selamat tinggal')
                break
            else:
                print('Pilihan tidak tersedia!')
                input('Tekan Enter untuk lanjut...')
        except ValueError:
                print('(ERROR) Masukkan angka, bukan huruf/kosong/simbol!')
                input('Tekan Enter untuk lanjut...')

def menu_admin():
        print(line)
        print('SELAMAT DATANG! APA YANG INGIN ANDA LAKUKAN')
        print(line)
        print('1. TAMBAH DATA')
        print('2. TAMPILKAN DATA')
        print('3. UBAH DATA')
        print('4. HAPUS DATA')
        print('5. KELUAR')
        print(line)
        while True:
            try :
                pilih = int(input('> '))
                if pilih == 1:
                    nama=input('nama = ')
                    nisn=input('nisn = ')
                    angkatan=input('angkatan = ')
                    tim=input('tim = ')
                    data[nama] = {
                        'nisn': nisn, 
                        'angkatan': angkatan, 
                        'tim': tim
                    }

                elif pilih == 2:
                    tampil_data(data)

                elif pilih == 3:
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

                elif pilih == 4: 
                    hapus = input('Nama anggota yang ingin dihapus = ')
                    if hapus in data:
                            del data[hapus]
                            print('Data berhasil dihapus')
                    else:
                        print('Anggota tidak ditemukan.')
                
                elif pilih == 5:
                    print('baik terimakasih telah menggunakan program ini')
                    break
                else:
                    print('Pilihan tidak tersedia!')
                    input('Tekan Enter untuk lanjut...')
            except ValueError:
                print('(ERROR) Masukkan angka, bukan huruf/kosong/simbol!')
                input('Tekan Enter untuk lanjut...')
        
def menu_user():
        print(line)
        print('SELAMAT DATANG! APA YANG INGIN ANDA LAKUKAN')
        print(line)
        print('1. TAMBAH DATA')
        print('2. TAMPILKAN DATA')
        print('3. KELUAR')
        print(line)
        while True:
            try : 
                pilih = int(input('> '))
                if pilih == 1:
                    nama=input('nama = ')
                    nisn=input('nisn = ')
                    angkatan=input('angkatan = ')
                    tim=input('tim = ')
                    data[nama] = {
                        'nisn': nisn, 
                        'angkatan': angkatan, 
                        'tim': tim
                    }

                elif pilih == 2:
                    tampil_data(data)
                
                elif pilih == 3:
                    os.system('cls')
                    print('baik! kembali ke halaman login')
                    break
                else:
                        print('Pilihan tidak tersedia!')
                        input('Tekan Enter untuk lanjut...')
            except ValueError:
                print('(ERROR) Masukkan angka, bukan huruf/kosong/simbol!')
                input('Tekan Enter untuk lanjut...')
                            
menu_login()