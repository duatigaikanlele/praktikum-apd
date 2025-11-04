import inquirer
import os
from prog_adser import menu_admin, menu_user
data={}
user= {
    'admin':{'pass':'dewa'},
    'user':{'pass':'rakyat'},
}

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
            menu_admin(data)
        else : menu_user(data)
    else : print('username atau password salah silahkan coba lagi')

def menu_login():
    while True:
        os.system('cls') 
        pertanyaan = [
            inquirer.List('pilihan',
                          message="Pilih opsi:",
                          choices=['1. REGISTER', '2. LOGIN', '3. KELUAR'],
                          )
        ]

        try:
            answers = inquirer.prompt(pertanyaan)
            pilih = int(answers['pilihan'].split('.')[0])
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

                            
menu_login()