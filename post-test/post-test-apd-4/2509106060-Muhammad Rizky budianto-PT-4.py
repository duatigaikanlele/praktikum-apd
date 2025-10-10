#halaman login
username_benar = "budi"
password_benar = "060"

while True:
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()

    if username == username_benar and password == password_benar:
        print("Login berhasil!\n")
        break
    elif username != username_benar and password != password_benar:
        print("Username dan Password salah, Silakan coba lagi\n")
    elif username != username_benar:
        print("Username salah!\n")
    elif password != password_benar:
        print("Password salah!\n")

# deklarasi golongan darah
Aplus = 0
Aminus = 0
Bplus = 0
Bminus = 0
ABplus = 0
ABminus = 0
Oplus = 0
Ominus = 0

while True:
    # Input golongan darah
    golongan = input("Masukkan golongan darah anda A/B/AB/O : ").strip().upper()
    # input rhesus
    rhesus = input("Masukkan rhesusnya +/- : ").strip()
    # Input jumlah kantong
    kantong = int(input("Masukkan jumlah kantong darah : "))
    # konversi
    ml = kantong * 500
    # Simpan sesuai golongan dan rhesus
    if golongan == "A":
        if rhesus == "+":
            Aplus += ml
        else:
            Aminus += ml
    elif golongan == "B":
        if rhesus == "+":
            Bplus += ml
        else:
            Bminus += ml
    elif golongan == "AB":
        if rhesus == "+":
            ABplus += ml
        else:
            ABminus += ml
    elif golongan == "O":
        if rhesus == "+":
            Oplus += ml
        else:
            Ominus += ml

    # [perulangan]
    ulang = input("Apakah anda masih mau input lagi (Y/T)? ").strip().upper()
    if ulang == "T":
        break
    print("")

# hasil data
print("""\nHASIL DATA
==========""")
print(f"A+ : {Aplus} ml")
print(f"A- : {Aminus} ml")
print(f"B+ : {Bplus} ml")
print(f"B- : {Bminus} ml")
print(f"AB+: {ABplus} ml")
print(f"AB-: {ABminus} ml")
print(f"O+ : {Oplus} ml")
print(f"O- : {Ominus} ml")
print("==========")