# halaman login 
user = input("input username anda : ")
nim = input("input password anda : ")
if (user == "budi" and nim == "060"):
    pick = (int(input("""pilih kalkulator mana yang ingin kamu operasikan
------------------------------------------------
          1. kalkulator panjang
          2. kalkulator massa
          3. kalkulator suhu
          4. kalkulator waktu
          
          silahkan ketik nomor yang ingin kamu pilih """)))
elif (user == "budi" and nim != "060"):
    print("password salah")
elif (user != "budi" and nim == "060"):
    print("username salah")
else : print("username dan password salah")

# kalkulator panjang
if pick == 1:
    kalku1 = (int(input("""mau pilih satuan apa?
           
           1. kaki -> meter
           2. kilometer -> meter
           3. centimeter -> meter
           
           silahkan ketik nomor yang ingin kamu pilih """)))
    if kalku1 == 1:
        nilai_p = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_p * 0.3048
        print("hasil =", hasil, "M")
    elif kalku1 == 2:
        nilai_p = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_p * 1000
        print("hasil =", hasil, "M")
    elif kalku1 == 3:
        nilai_p = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_p / 100
        print("hasil =", hasil, "M")
    else : print("pilihan tidak terdaftar")

# kalkulator massa
elif pick == 2:
    kalku2 = (int(input("""mau pilih satuan apa?
           
           1. pound -> kilogram
           2. ton -> kilogram
           3. gram -> kilogram
           
           silahkan ketik nomor yang ingin kamu pilih """)))
    if kalku2 == 1:
        nilai_m = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_m*0.5
        print("hasil =", hasil, "KG")
    elif kalku2 == 2:
        nilai_m = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_m*1000
        print("hasil =", hasil, "KG")
    elif kalku2 == 3:
        nilai_m = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_m/1000
        print("hasil =", hasil, "KG")
    else : print("pilihan tidak terdaftar")

# kalkulator suhu
elif pick == 3:
    kalku3 = (int(input("""mau pilih satuan apa?
           
           1. celcius -> kelvin
           2. fahrenheit -> kelvin
           3. reamur -> kelvin
           
           silahkan ketik nomor yang ingin kamu pilih """)))
    if kalku3 == 1:
        nilai_s = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_s+273.15
        print("hasil =", hasil, "K")
    elif kalku3 == 2:
        nilai_s = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_s+459.67
        print("hasil =", hasil, "K")
    elif kalku3 == 3:
        nilai_s = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = (5/4)*nilai_s+ 273.15
        print("hasil =", hasil, "K")
    else : print("pilihan tidak terdaftar")

# kalkulator waktu
elif pick == 4:
    kalku4 = (int(input("""mau pilih satuan apa?
           
           1. menit -> detik
           2. jam -> detik
           
           silahkan ketik nomor yang ingin kamu pilih """)))
    if kalku4 == 1:
        nilai_w = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_w*60
        print("hasil =", hasil, "detik")
    elif kalku4 == 2:
        nilai_w = (float(input("masukkan nilai yang ingin kamu konversi = ")))
        hasil = nilai_w*3600
        print("hasil =", hasil, "detik")
    else : print("pilihan tidak terdaftar")

# pilihan selain 1-4
else : print("pilihan tidak terdaftar")