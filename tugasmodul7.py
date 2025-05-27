def kecepatan_akhir (v0, a, t) :
    kecepatan_akhir = v0 + a*t
    return kecepatan_akhir
def jarak_tempuh (v0, a, t) :
    jarak_tempuh = v0*t + 0.5*a*t**2
    return jarak_tempuh

n = int(input("Masukkan berapa data yang ingin dimasukkan : "))
data = []

for i in range (n):
    print(f"Data ke-{1+i} :")
    v0 = float(input("Masukkan nilai kecepatan awal(vo) : "))
    a = float(input("Masukkan nilai percepatan(a) : "))
    t = float(input("Masukkan nilai waktu(t) : "))

    vt = kecepatan_akhir(v0, a, t)
    jarak_akhir = jarak_tempuh(v0, a, t) 

    data.append((v0, a, t, vt, jarak_akhir))


print()
print ("                       TABEL HASIL PERHITUNGAN")
def print_data(data_nilai) :
    print ("-" *71)
    print("| n | Kecepatan awal  | Percepatan | Waktu | Kecepatan Akhir | Jarak  |")
    print ("-" *71)
    
    i = 1
    for kecepatan_awal, percepatan, waktu, vt, jarak in data_nilai:
        print(f"| {i:<1} | {kecepatan_awal:<15.0f} | {percepatan:<10.0f} | {waktu:<5.0f} | {vt:<15.1f} | {jarak:<6.0f} |")
        i+=1
    print ("-" *71)
    
print_data(data)


