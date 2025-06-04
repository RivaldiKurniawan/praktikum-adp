# Data cakoor
data_calon = [
    ("Dicky Rivaldi Kurniawan", "2410432031", "A", "Acara:Ketua; Pubdok:anggota; Humas:Anggota", 85, "Acara"),
    ("Raditya Irawan", "3410432003", "A", "Acara:Anggota; Perlengkapan:Anggota", 80, "Perlengkapan"),
    ("Zhafran Ariella", "2410433009", "A", "Perlengkapan:Ketua; Acara:Anggota", 75, "Perlengkapan"),
    ("Shalsya Adina Marsya", "2410432009", "A", "Humas:Anggota;Acara:Anggota", 85, "Pubdok"),
    ("Rivaldo Nofrizal", "2410432043", "A", "Humas:Ketua;Acara:Anggota", 90, "Perlengkapan"),
    ("Lala Abdillah Batubara", "2410431031", "A", "Humas:Anggota;Perlengkapan:Anggota", 85, "Danus"),
    ("M. Akbar Putra P. Asaki", "2410432023", "A", "Humas:Anggota", 82, "Pubdok"),
    ("Mufli Diash Putra", "2410432001", "A", "Humas:Anggota", 78, "Danus"),
    ("Danda Ahmad Dzaky", "2410432030", "C", "Danus:Ketua", 90, "Perlengkapan"),
    ("Gibran Ramadhan", "2410431032", "B", "Danus:Anggota;Pubdok:Anggota", 78, "Danus"),
    ("Yazid Riyanda Putra", "2410431005", "C", "Acara:Ketua", 90, "Acara"),
    ("Dinda Rahma Mulyana", "2410431034", "B", "Acara:Anggota;Danus:Anggota", 75, "Pubdok"),
    ("Melda Afrilia", "2410432042", "A", "Perlengkapan:Ketua", 85, "Danus"),
    ("Wahyu Andani", "2410432004", "B", "Perlengkapan:Anggota;Danus:Anggota", 79, "Pubdok"),
    ("Lexania Nazila", "2410431019", "A", "Pubdok:Ketua;Acara:Anggota", 80, "Acara"),
    ("Mutiara Aviva", "2410432045", "KBI", "Pubdok:Anggota", 80, "Acara")
] # berupa list

# Simpan data ke file teks "OrPSB22.txt" di awal program
#menyimpan data yang yang telah tersedia ke dalam file text orPSB22.txt
with open("OrPSB22.txt", 'w') as f:
    for calon in data_calon:
        baris = f"{calon[0]},{calon[1]},{calon[2]},{calon[3]},{calon[4]},{calon[5]}\n" # Format: nama,nim,kelas,pengalaman,nilai_wawancara,bidang
        f.write(baris)


# Fungsi parsing pengalaman
def pengalaman_calon(pengalaman_kepanitiaan): #fungsi pengalaman_calon
    pengalaman = {} # mengubah string menjadi dictionary
    for item in pengalaman_kepanitiaan.split(';'):
        if ":" in item:
            bidang, peran = item.split(':')
            pengalaman[bidang.strip()] = peran.strip()
    return pengalaman

# Fungsi hitung skor total calon
def hitung_nilai(pengalaman, pilihan_bidang, nilai_wawancara): #fungsi hitung_nilai(pengalaman, pilihan_bidang, nilai_wawancara)
    nilai_pengalaman = 0
    nilai_pengalaman += len(pengalaman)
    if any(peran.lower() == "ketua" for peran in pengalaman.values()):
        nilai_pengalaman += 2
    if pilihan_bidang in pengalaman:
        nilai_pengalaman += 3
    return nilai_wawancara + nilai_pengalaman

# Fungsi utama pemrosesan file
def proses_file(nama_file):
    with open("OrPSB22.txt", 'r') as f:
        baris = f.readlines()

    data_bidang = {}

    for line in baris:  #menyimpan cakoor dikelompokkan sesuai bidang
        nama, nim, kelas, pengalaman_kepanitiaan, nilai_wawancara_calon, bidang = line.strip().split(',')
        pengalaman = pengalaman_calon(pengalaman_kepanitiaan)
        nilai_wawancara = int(nilai_wawancara_calon)
        skor = hitung_nilai(pengalaman, bidang, nilai_wawancara)

        if bidang not in data_bidang:
            data_bidang[bidang] = []

        data_bidang[bidang].append({
            'nama': nama,
            'nim': nim,
            'kelas': kelas,
            'bidang': bidang,
            'nilai': skor
        })

    for bidang, peserta in data_bidang.items():
        if len(peserta) < 4:
            print(f"\nCakoor dari bidang {bidang} minimal harus 4")
        print(f"\nTop 2 Cakoor untuk Bidang {bidang.upper()}:")
        peserta_sorted = sorted(peserta, key=lambda x: x['nilai'], reverse=True) #mengurutkan dari tertinggi ke terendah
        for i, p in enumerate(peserta_sorted[:2], 1):  # mengambil atau menampilkan outputnya 2 tertinggi sesuai yang diminta soal
            print(f"{i}. Nama : {p['nama']} (NIM : {p['nim']}, Kelas: {p['kelas']}) - Nilai: {p['nilai']}")

# Proses_data dari file dan menampilkan outputnya
proses_file("OrPSB22.txt")

print()