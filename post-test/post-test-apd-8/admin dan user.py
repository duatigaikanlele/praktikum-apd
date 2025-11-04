import inquirer
import os
from prettytable import PrettyTable

def tampil_data(n):
    tabel = PrettyTable()
    tabel.field_names = ['NAMA', 'NISN', 'ANGKATAN', 'TIM']
    if len(n)==0:
        print('data masih belum ada')
    else : 
        for key, value in n.items():
            tabel.add_row([key, value['nisn'], value['angkatan'], value['tim']])
        tabel.title = "DATA ANGGOTA"
        print(tabel)

def menu_admin(data):
            while True :
                pertanyaan = [
                    inquirer.List('pilihan',
                                  message="Pilih opsi:",
                                  choices=['1. TAMBAH DATA', '2. TAMPILKAN DATA', '3. UBAH DATA', '4. HAPUS DATA', '5. KELUAR'],
                                  )
                ]
                try:
                    answers = inquirer.prompt(pertanyaan)
                    pilih = int(answers['pilihan'].split('.')[0])
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

def menu_user(data):
            while True :
                pertanyaan = [
                    inquirer.List('pilihan',
                                  message="Pilih opsi:",
                                  choices=['1. TAMBAH DATA', '2. TAMPILKAN DATA', '3. KELUAR'],
                                  )
                ]
                try:
                    answers = inquirer.prompt(pertanyaan)
                    pilih = int(answers['pilihan'].split('.')[0])
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
                        continue

                    elif pilih == 2:
                        tampil_data(data)
                        continue
                    
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
                    continue
            return data