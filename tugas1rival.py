x =input( " Masukkan nama anda : ")
print("=" * 50)
print( " DAFTAR FILM YANG SEDANG TAYANG")
print( " 1. Kode: 1 untuk film Captain America ")
print(" Harga Satuan : Rp. 55.000")
print( " 2. Kode: 2 untuk film Keluarga Cemara")
print(" Harga Satuan : Rp. 40.000")
print( " 3. Kode: 3 untuk film 1 Kakak 7 Ponakan")
print(" Harga Satuan : Rp. 50.000")
print( " 4. Kode: 4 untuk film Petaka Gunung Gede")
print(" Harga Satuan : Rp. 65.000")
print( " 5. Kode: 5 untuk film Attack On Titan")
print(" Harga Satuan : Rp. 45.000")
print( " 6. Kode: 6 untuk film Perayaan Mati Rasa")
print(" Harga Satuan : Rp. 65.000")
print("-" * 50)

kode_film = int(input(" Masukkan kode film yang ingin  ditonton (1-6) : "))
tiket = int(input(" Jumlah tiket : "))

if kode_film == 1 :
    print(" Captain America")
    a = 55000
    print(f' harga tiket          : {a}')
    jumlah_harga = a*tiket
    print(f' harga total          : {jumlah_harga}')

elif kode_film == 2 :
    print(" Keluarga Cemara")
    a = 40000
    print(f' harga tiket          : {a}')
    jumlah_harga = a*tiket
    print(f' harga total          : {jumlah_harga}')

elif kode_film == 3 :
    print(" 1 Kakak 7 Ponakan")
    a = 50000
    print(f' harga tiket          : {a}')
    jumlah_harga = a*tiket
    print(f' harga total          : {jumlah_harga}')

elif kode_film == 4 :
    print(" Petaka Gunung Gede")
    a = 65000
    print(f' harga tiket          : {a}')
    jumlah_harga = a*tiket
    print(f' harga total          : {jumlah_harga}')

elif kode_film == 5 :
    print(" Attack On Titan")
    a = 45000
    print(f' harga tiket          : {a}')
    jumlah_harga = a*tiket
    print(f' harga total          : {jumlah_harga}')

elif kode_film == 6 :
    print(" Perayaan Mati Rasa")
    a = 65000
    print(f' harga tiket          : {a}')
    jumlah_harga = a*tiket
    print(f' harga total          : {jumlah_harga}')

else : 
    print("Tidak Dapat ditemukan")

if jumlah_harga > 250000 :
    diskon = 0.35
    z = jumlah_harga*diskon

elif jumlah_harga > 100000 :
    diskon = 0.15
    z = jumlah_harga*diskon

else :
    diskon = 0
    z = jumlah_harga*diskon

print(f" potongan harga       : {z}")

potongan_harga = jumlah_harga - (z)
print(f' harga setelah diskon : {potongan_harga}')

print(" ")

print("=" * 50)
print( "     ------------STRUK PEMESANAN------------")
print("=" * 50)
print(" Nama           : ", x)
print(" Judul Film     : ", kode_film)
if kode_film == 1:
    print("                   Captain America")
elif kode_film == 2:
    print("                   Keluarga Cemara")
elif kode_film == 3:
    print("                   1 Kakak 7 Ponakan ")
elif kode_film == 4:
    print("                   Petaka Gunung Gede")
elif kode_film == 5:
    print("                   Attack On Titan")
elif kode_film == 6:
    print("                   Perayaan Mati Rasa")
else : 
    print("                   Tidak Ada Film")
print(" Jumlah Tiket   : ", tiket)
print(" Harga Satuan   : ", a )
print(" Potongan Harga : " , z )
print(" Total Harga    : ", potongan_harga )
print("=" * 50)


    



