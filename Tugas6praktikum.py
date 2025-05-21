# program membuat nama dan ip secara berurutan lalu ouputnya berupa tabel 


indeks_nilai = ["A", "A-", "B+", "B", "B-", "C+", "C", "D", "E"]
nilai_ip =    [4.00, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0.00]

# menginput jumlah dari mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Array 2D untuk data mahasiswa
data_mahasiswa = []

for i in range(jumlah_mahasiswa):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ").strip() #strip() menghilangkan spasi di awal/akhir.
    
    while True:
        indeks = input("Masukkan indeks nilai (A, A-, B+, B, B-, C+, C, D, E): ").strip().upper()
        if indeks in indeks_nilai:
            # mengambil IP dari list/array berdasarkan posisi indeks
            posisi = indeks_nilai.index(indeks)
            ip_angka = nilai_ip[posisi]
            break
        else:
            print("Indeks nilai tidak valid")

    # Simpan ke array 2D
    data_mahasiswa.append([nama, indeks, ip_angka])

# mengurutkan data mahasiswa berdasarkan IP dari terbesar ke terkecil
data_mahasiswa.sort(key=lambda x: x[2], reverse=True) # menggunakan fungsi .sort() dan parameter key, disisni supaya berurut berdasarkan IP, bukan berurut berdasarkan yang pertama di input
print() # menggunakan nilai x[2] (yaitu nilai IP mahasiswa) sebagai kunci untuk pengurutan

# menampilkan output tabel
print("            Data Mahasiswa")
print()


# Header tabel
print("-" * 40)
print(f"| {"Nama":<8} || {"Indeks Nilai":<14} || {"IP  ":>6} |")
print("-" * 40)

# Isi tabel
for row in data_mahasiswa:
    nama, indeks, ip_angka = row
    print(f"| {nama:<8} || {indeks:<14} || {ip_angka:>6.2f} |")
    print("-" * 40)

