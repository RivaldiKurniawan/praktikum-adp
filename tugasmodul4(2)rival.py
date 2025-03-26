print("=" *90)
print("         ----------------------VALIDASI PASSWORD ANDA DISINI----------------------")
print("=" *90)

while True:
    password = input("Masukkan password Anda: ")

    minimal_panjang = False
    karakter_khusus = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`"
    huruf_kecil = False
    kapital = False
    angka = False
    simbol = False

    if len(password) >= 8 :
        minimal_panjang = True

    else :
        print("Password Tidak Valid")
        print("Minimal harus 8 karakter")
        print("-" *90)
        continue
    
        
    for kode in password :
        if "A" <= kode <= "Z" :
            kapital = True

        elif "a" <= kode <= "z" :
            huruf_kecil = True 

        elif "0" <= kode <= "9" :
            angka = True 

        elif kode in karakter_khusus :
            simbol = True
        
        
    
    if minimal_panjang and huruf_kecil and kapital and simbol and angka :
        print(" Password Anda Valid! Selamat, akses diterima")
        break
    else :
        if not huruf_kecil :
            print("Setidaknya ada 1 huruf kecil dalam password anda")

        if not kapital :
            print("Setidaknya ada 1 huruf kapital dalam password anda")

        if not angka :
            print("Setidaknya ada 1 angka ( dari 0 sampai 9) dalam password anda")

        if not simbol :
            print("Setidaknya ada 1 karakter khusus (!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~) dalam password anda")
        
        print("-" *90)

        
print("=" *50)
    

    



