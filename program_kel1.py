import matplotlib.pyplot as plt
from tabulate import tabulate
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext, Toplevel, StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def status_indeks_massa_tubuh(imt):
    """
    Menentukan status Indeks Massa Tubuh (IMT).
    """
    if imt < 18.5:
        return "Berat Badan Kurang"
    elif 18.5 <= imt < 25:
        return "Normal"
    elif 25 <= imt < 30:
        return "Berat Badan Berlebih"
    else:
        return "Obesitas"

def status_detak_jantung_per_menit(dj):
    """
    Menentukan status detak jantung per menit.
    """
    if dj < 60:
        return "Rendah"
    elif 60 <= dj <= 100:
        return "Normal untuk orang dewasa"
    elif 101 <= dj <= 120:
        return "Sedikit tinggi (mild tachycardia)"
    else:
        return "Tinggi (tachycardia)"

def hitung_denyut_nadi_saat_olahraga(umur):
    """
    Menghitung detak jantung maksimum dan zona denyut nadi saat olahraga.
    """
    dj_maks = 220 - umur
    zona_moderat_bawah = int(dj_maks * 0.5)
    zona_moderat_atas = int(dj_maks * 0.7)
    zona_intens_bawah = int(dj_maks * 0.7)
    zona_intens_atas = int(dj_maks * 0.85)
    return dj_maks, (zona_moderat_bawah, zona_moderat_atas), (zona_intens_bawah, zona_intens_atas)

def hitung_rasio_pinggang_panggul(pinggang, panggul, jenis_kelamin):
    """
    Menghitung Rasio Pinggang-Panggul (RPP) dan menentukan statusnya.
    """
    if panggul == 0: # Mencegah pembagian dengan nol
        return 0.0, "Tidak Valid"
    rpp = pinggang / panggul
    status = "Normal"
    if (jenis_kelamin.lower() == "pria" and rpp > 0.90) or (jenis_kelamin.lower() == "wanita" and rpp > 0.85):
        status = "Tinggi"
    return rpp, status

def simpan_data_ke_berkas(data):
    """
    Menyimpan data kesehatan ke dalam berkas teks.
    """
    try:
        with open("data_kesehatan.txt", "a") as berkas:
            berkas.write(f"Nama               : {data['nama_pengguna']}\n")
            berkas.write(f"Umur               : {data['umur']} tahun\n")
            berkas.write(f"Tinggi Badan       : {data['tinggi_badan']:.1f} cm\n")
            berkas.write(f"Berat Badan        : {data['berat_badan']:.1f} kg\n")
            berkas.write(f"IMT                : {data['imt']:.1f} ({data['status_imt']})\n")
            berkas.write(f"Detak Jantung      : {data['detak_jantung']} bpm ({data['status_detak_jantung']})\n")
            berkas.write(f"RPP                : {data['rpp']:.2f} ({data['status_rpp']})\n")
            berkas.write(f"Merokok            : {'Ya' if data['merokok'] == 'ya' else 'Tidak'}\n")
            berkas.write(f"Olahraga           : {'Ya' if data['olahraga'] == 'ya' else 'Tidak'}\n")
            berkas.write(f"Penyakit Bawaan    : {data['riwayat'] if data['riwayat'] in ['jantung', 'diabetes', 'hipertensi'] else '-'}\n")
            berkas.write(f"Sakit hari ini     : {'Ya' if data['sakit'] == 'ya' else 'Tidak'}\n")
            berkas.write(f"Minum hari ini     : {'Ya' if data['minum'] == 'ya' else 'Tidak'}\n")
            berkas.write(f"Alergi makan       : {'Ya' if data['alergi'] == 'ya' else 'Tidak'}\n")
            berkas.write(f"Asma               : {'Ya' if data['asma'] == 'ya' else 'Tidak'}\n")
            berkas.write(f"DJ Maks            : {data['Detak_Jantung_Maks']} bpm\n")
            berkas.write(f"Zona Moderat       : {data['zona_moderat_bawah']} - {data['zona_moderat_atas']} bpm\n")
            berkas.write(f"Zona Intensif      : {data['zona_intens_bawah']} - {data['zona_intens_atas']} bpm\n")
            berkas.write("=" * 50 + "\n")
    except Exception as e:
        messagebox.showerror("Gagal Menyimpan Data", f"Gagal menyimpan data: {e}")

def baca_data_dari_berkas():
    """
    Membaca data kesehatan dari berkas teks.
    """
    try:
        if not os.path.exists("data_kesehatan.txt"):
            return "❌ Berkas data_kesehatan.txt tidak ditemukan!"
        with open("data_kesehatan.txt", "r") as berkas:
            return "    DATA DARI BERKAS    \n" + berkas.read()
    except Exception as e:
        return f"❌ Terjadi kesalahan saat membaca berkas: {e}"

# KELAS UTAMA APLIKASI GUI
class AplikasiKesehatan:
    def __init__(self, master):
        self.master = master
        master.title("APLIKASI DATA KESEHATAN")
        master.geometry("1000x750")
        master.resizable(True, True)

        self.nama_pengguna = ""
        self.bingkai_saat_ini = None
        self.buat_layar_masuk()

    def bersihkan_bingkai_saat_ini(self):
        """
        Menghapus bingkai (frame) yang sedang aktif.
        """
        if self.bingkai_saat_ini:
            self.bingkai_saat_ini.destroy()
        self.bingkai_saat_ini = None

    def buat_layar_masuk(self):
        """
        Membuat layar masuk (login/registrasi) aplikasi.
        """
        self.bersihkan_bingkai_saat_ini()
        self.bingkai_masuk = tk.Frame(self.master, padx=50, pady=50, bg="#13dfe2")
        self.bingkai_masuk.pack(expand=True)
        self.bingkai_saat_ini = self.bingkai_masuk

        tk.Label(self.bingkai_masuk, text="   SELAMAT DATANG DI APLIKASI DATA KESEHATAN    ",
                 font=("Helvetica Neue", 18, "bold"), fg="#333", bg="#13dfe2").pack(pady=(0, 30))

        tk.Label(self.bingkai_masuk, text="PILIH OPSI MASUK", font=("Helvetica Neue", 14, "bold"), bg="#f0f0f0").pack(pady=(10, 5))
        self.opsi_masuk = StringVar(value="masuk")
        tk.Radiobutton(self.bingkai_masuk, text="Sudah punya akun", variable=self.opsi_masuk, value="masuk", font=("Helvetica Neue", 12), bg="#f0f0f0").pack(anchor="w", padx=50, pady=5)
        tk.Radiobutton(self.bingkai_masuk, text="Belum punya akun", variable=self.opsi_masuk, value="daftar", font=("Helvetica Neue", 12), bg="#f0f0f0").pack(anchor="w", padx=50, pady=5)

        tk.Label(self.bingkai_masuk, text="Nama Pengguna:", font=("Helvetica Neue", 12), bg="#f0f0f0").pack(pady=(20, 5))
        self.entri_nama_pengguna = tk.Entry(self.bingkai_masuk, font=("Helvetica Neue", 12), width=30, bd=2, relief="groove")
        self.entri_nama_pengguna.pack(pady=5)

        tk.Label(self.bingkai_masuk, text="Kata Sandi:", font=("Helvetica Neue", 12), bg="#f0f0f0").pack(pady=(10, 5))
        self.entri_kata_sandi = tk.Entry(self.bingkai_masuk, font=("Helvetica Neue", 12), width=30, show="*", bd=2, relief="groove")
        self.entri_kata_sandi.pack(pady=5)

        tk.Button(self.bingkai_masuk, text="Masuk / Daftar", command=self.masuk_atau_daftar, font=("Helvetica Neue", 14, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white", relief="raised", bd=3).pack(pady=30)

    def masuk_atau_daftar(self):
        """
        Menangani proses masuk atau pendaftaran pengguna.
        """
        opsi = self.opsi_masuk.get()
        input_nama_pengguna = self.entri_nama_pengguna.get().strip()
        input_kata_sandi = self.entri_kata_sandi.get().strip()

        if not input_nama_pengguna or not input_kata_sandi:
            messagebox.showerror("Error Masuk/Daftar", "Nama pengguna dan kata sandi tidak boleh kosong!")
            return

        if opsi == "masuk":
            self.nama_pengguna = input_nama_pengguna
            messagebox.showinfo("Login Berhasil", f"✅ Masuk berhasil! Selamat datang, {self.nama_pengguna}!")
            self.buat_layar_menu_utama()
        elif opsi == "daftar":
            self.tampilkan_dialog_daftar(input_nama_pengguna)

    def tampilkan_dialog_daftar(self, input_nama_pengguna):
        """
        Menampilkan dialog pendaftaran akun baru.
        """
        dialog_daftar = Toplevel(self.master)
        dialog_daftar.title("Daftar Akun Baru")
        dialog_daftar.geometry("400x200")
        dialog_daftar.transient(self.master)
        dialog_daftar.grab_set()

        tk.Label(dialog_daftar, text="Masukkan Email Anda (contoh: nama@gmail.com):", font=("Helvetica Neue", 10)).pack(pady=10)
        entri_email = tk.Entry(dialog_daftar, font=("Helvetica Neue", 10), width=40)
        entri_email.pack(pady=5)

        def selesaikan_pendaftaran():
            input_email = entri_email.get().strip()
            if "@gmail.com" in input_email and input_email.endswith("@gmail.com") and len(input_email.split("@")[0]) > 0:
                self.nama_pengguna = input_nama_pengguna
                messagebox.showinfo("Akun Berhasil Dibuat", f"✅ Akun untuk {self.nama_pengguna} berhasil dibuat!")
                dialog_daftar.destroy()
                self.buat_layar_menu_utama()
            else:
                messagebox.showerror("Email Tidak Valid", "Masukkan email yang valid (contoh: nama@gmail.com) !!")

        tk.Button(dialog_daftar, text="Daftar Sekarang", command=selesaikan_pendaftaran, font=("Helvetica Neue", 12), bg="#2196F3", fg="white").pack(pady=20)

    def buat_layar_menu_utama(self):
        """
        Membuat layar menu utama aplikasi.
        """
        self.bersihkan_bingkai_saat_ini()
        self.bingkai_menu = tk.Frame(self.master, padx=50, pady=50, bg="#e6f7ff")
        self.bingkai_menu.pack(expand=True)
        self.bingkai_saat_ini = self.bingkai_menu

        tk.Label(self.bingkai_menu, text=f"Hallooo.... selamat datang di program cek kesehatan {self.nama_pengguna} !!",
                 font=("Helvetica Neue", 16, "bold"), fg="#0056b3", bg="#e6f7ff").pack(pady=(0, 40))

        opsi_menu = [
            ("1. Cek Kesehatan", self.buat_layar_cek_kesehatan, "#007bff"),
            ("2. Buka Berkas Data Kesehatan", self.tampilkan_layar_data_berkas, "#6c757d"),
            ("3. Selesai / Keluar", self.master.quit, "#dc3545")
        ]
        for teks, perintah, warna_latar in opsi_menu:
            tk.Button(self.bingkai_menu, text=teks, command=perintah,
                      font=("Helvetica Neue", 14), bg=warna_latar, fg="white",
                      activebackground=warna_latar.replace("7b", "56").replace("c7", "5a").replace("dc3", "c82"),
                      activeforeground="white", relief="raised", bd=3, width=25, height=2).pack(pady=15)

    def buat_layar_cek_kesehatan(self):
        """
        Membuat layar formulir input data kesehatan.
        """
        self.bersihkan_bingkai_saat_ini()
        self.bingkai_cek_kesehatan = tk.Frame(self.master, padx=30, pady=30, bg="#ffffff")
        self.bingkai_cek_kesehatan.pack(fill="both", expand=True)
        self.bingkai_saat_ini = self.bingkai_cek_kesehatan

        tk.Label(self.bingkai_cek_kesehatan, text="Formulir Data Kesehatan Anda",
                 font=("Helvetica Neue", 16, "bold"), fg="#333").grid(row=0, columnspan=2, pady=(0, 20))

        # Konfigurasi input yang digabungkan
        konfigurasi_input = [
            ("Usia (tahun):", "umur", int),
            ("Tinggi badan (cm):", "tinggi_badan", float),
            ("Berat badan (kg):", "berat_badan", float),
            ("Detak jantung istirahat (bpm):", "detak_jantung", int),
            ("Lingkar pinggang (cm):", "pinggang", float),
            ("Lingkar panggul (cm):", "panggul", float)
        ]

        self.entri_input = {}
        baris_idx = 1
        for teks_label, kunci, tipe_nilai in konfigurasi_input:
            tk.Label(self.bingkai_cek_kesehatan, text=teks_label, font=("Helvetica Neue", 10), anchor="w").grid(row=baris_idx, column=0, sticky="w", pady=2, padx=5)
            entri = tk.Entry(self.bingkai_cek_kesehatan, font=("Helvetica Neue", 10), width=40, bd=1, relief="solid")
            entri.grid(row=baris_idx, column=1, sticky="ew", pady=2, padx=5)
            self.entri_input[kunci] = (entri, tipe_nilai)
            baris_idx += 1

        # Jenis Kelamin
        tk.Label(self.bingkai_cek_kesehatan, text="Jenis kelamin (pria/wanita):", font=("Helvetica Neue", 10), anchor="w").grid(row=baris_idx, column=0, sticky="w", pady=2, padx=5)
        self.variabel_jenis_kelamin = StringVar(value="pria")
        tk.Radiobutton(self.bingkai_cek_kesehatan, text="Pria", variable=self.variabel_jenis_kelamin, value="pria", font=("Helvetica Neue", 10)).grid(row=baris_idx, column=1, sticky="w", padx=5)
        baris_idx += 1
        tk.Radiobutton(self.bingkai_cek_kesehatan, text="Wanita", variable=self.variabel_jenis_kelamin, value="wanita", font=("Helvetica Neue", 10)).grid(row=baris_idx, column=1, sticky="w", padx=5)
        baris_idx += 1

        # Input Ya/Tidak
        pertanyaan_ya_tidak = [
            ("Apakah kamu merokok?", "merokok"),
            ("Apakah kamu berolahraga rutin?", "olahraga"),
            ("Apakah kamu merasa sakit hari ini?", "sakit"),
            ("Apakah kamu sudah minum 8 gelas air putih hari ini?", "minum"),
            ("Apakah kamu mempunyai alergi tertentu?", "alergi"),
            ("Apakah kamu pernah mengalami sesak napas atau napas berbunyi?", "asma")
        ]
        self.variabel_ya_tidak = {}
        for teks_pertanyaan, kunci in pertanyaan_ya_tidak:
            tk.Label(self.bingkai_cek_kesehatan, text=teks_pertanyaan + " (ya/tidak):", font=("Helvetica Neue", 10), anchor="w").grid(row=baris_idx, column=0, sticky="w", pady=2, padx=5)
            var = StringVar(value="tidak")
            tk.Radiobutton(self.bingkai_cek_kesehatan, text="Ya", variable=var, value="ya", font=("Helvetica Neue", 10)).grid(row=baris_idx, column=1, sticky="w", padx=5)
            tk.Radiobutton(self.bingkai_cek_kesehatan, text="Tidak", variable=var, value="tidak", font=("Helvetica Neue", 10)).grid(row=baris_idx, column=1, padx=5, sticky="e")
            self.variabel_ya_tidak[kunci] = var
            baris_idx += 1

        tk.Label(self.bingkai_cek_kesehatan, text="Riwayat penyakit bawaan (jantung/diabetes/hipertensi/-):", font=("Helvetica Neue", 10), anchor="w").grid(row=baris_idx, column=0, sticky="w", pady=2, padx=5)
        self.entri_riwayat = tk.Entry(self.bingkai_cek_kesehatan, font=("Helvetica Neue", 10), width=40, bd=1, relief="solid")
        self.entri_riwayat.grid(row=baris_idx, column=1, sticky="ew", pady=2, padx=5)
        baris_idx += 1

        tk.Button(self.bingkai_cek_kesehatan, text="Cek Kesehatan", command=self.lakukan_cek_kesehatan,
                  font=("Helvetica Neue", 13, "bold"), bg="#28a745", fg="white", activebackground="#218838", activeforeground="white", relief="raised", bd=3).grid(row=baris_idx, columnspan=2, pady=20)
        tk.Button(self.bingkai_cek_kesehatan, text="Kembali ke Menu Utama", command=self.buat_layar_menu_utama,
                  font=("Helvetica Neue", 10), bg="#007bff", fg="white", activebackground="#0056b3", activeforeground="white", relief="raised", bd=2).grid(row=baris_idx + 1, columnspan=2, pady=5)

    def dapatkan_semua_input(self):
        """
        Mengambil semua input dari formulir dan mengembalikan sebagai kamus.
        """
        data = {}
        for kunci, (widget_entri, fungsi_tipe) in self.entri_input.items():
            try:
                data[kunci] = fungsi_tipe(widget_entri.get().strip())
            except ValueError:
                raise ValueError(f"Input '{kunci.replace('_', ' ').title()}' harus berupa angka.")

        data['jenis_kelamin'] = self.variabel_jenis_kelamin.get()
        for kunci, var in self.variabel_ya_tidak.items():
            data[kunci] = var.get()
        data['riwayat'] = self.entri_riwayat.get().strip().lower()
        return data

    def lakukan_cek_kesehatan(self):
        """
        Melakukan perhitungan kesehatan berdasarkan input pengguna dan menampilkan hasilnya.
        """
        try:
            input_data = self.dapatkan_semua_input()

            if input_data['riwayat'] not in ["jantung", "diabetes", "hipertensi", "-"]:
                messagebox.showwarning("Input Tidak Valid", "Riwayat penyakit harus 'jantung', 'diabetes', 'hipertensi', atau '-'.")
                return

            # Jalankan logika perhitungan Anda
            rpp, status_rpp = hitung_rasio_pinggang_panggul(input_data['pinggang'], input_data['panggul'], input_data['jenis_kelamin'])
            dj_maks, zona_moderat, zona_intens = hitung_denyut_nadi_saat_olahraga(input_data['umur'])
            imt = input_data['berat_badan'] / ((input_data['tinggi_badan'] / 100) ** 2)
            status_imt = status_indeks_massa_tubuh(imt)
            status_detak_jantung = status_detak_jantung_per_menit(input_data['detak_jantung'])

            # Siapkan data untuk diteruskan ke fungsi tampilan dan penyimpanan
            data_hasil = {
                "nama_pengguna": self.nama_pengguna,
                "umur": input_data['umur'],
                "tinggi_badan": input_data['tinggi_badan'],
                "berat_badan": input_data['berat_badan'],
                "imt": imt,
                "status_imt": status_imt,
                "detak_jantung": input_data['detak_jantung'],
                "status_detak_jantung": status_detak_jantung,
                "rpp": rpp,
                "status_rpp": status_rpp,
                "merokok": input_data['merokok'],
                "olahraga": input_data['olahraga'],
                "riwayat": input_data['riwayat'],
                "sakit": input_data['sakit'],
                "minum": input_data['minum'],
                "alergi": input_data['alergi'],
                "asma": input_data['asma'],
                "Detak_Jantung_Maks": dj_maks,
                "zona_moderat_bawah": zona_moderat[0],
                "zona_moderat_atas": zona_moderat[1],
                "zona_intens_bawah": zona_intens[0],
                "zona_intens_atas": zona_intens[1]
            }

            self.tampilkan_layar_hasil_kesehatan(data_hasil)

        except ValueError as e:
            messagebox.showerror("Error Input", f"Kesalahan input: {e}\nPastikan semua nilai yang dimasukkan sesuai format (angka untuk numerik, 'ya'/'tidak' untuk pilihan).")
        except Exception as e:
            messagebox.showerror("Terjadi Kesalahan", f"Terjadi kesalahan tak terduga: {e}")

    def tampilkan_layar_hasil_kesehatan(self, data):
        """
        Menampilkan layar hasil pemeriksaan kesehatan.
        """
        self.bersihkan_bingkai_saat_ini()
        wadah_hasil = tk.Frame(self.master, padx=20, pady=20, bg="#f8f8f8")
        wadah_hasil.pack(fill="both", expand=True)
        self.bingkai_saat_ini = wadah_hasil

        tk.Label(wadah_hasil, text="Hasil Pemeriksaan Kesehatan Anda",
                 font=("Helvetica Neue", 16, "bold"), fg="#333", bg="#f8f8f8").pack(pady=(0, 20))

        bingkai_teks = tk.Frame(wadah_hasil, bg="#f8f8f8")
        bingkai_teks.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        area_teks_hasil = scrolledtext.ScrolledText(bingkai_teks, wrap=tk.WORD, font=("Consolas", 10), width=70, height=25, bd=1, relief="solid")
        area_teks_hasil.pack(fill="both", expand=True)

        data_tabel = [
            ["Umur", f"{data['umur']} tahun"], ["Tinggi Badan", f"{data['tinggi_badan']:.1f} cm"],
            ["Berat Badan", f"{data['berat_badan']:.1f} kg"], ["IMT", f"{data['imt']:.1f} ({data['status_imt']})"],
            ["Detak Jantung", f"{data['detak_jantung']} bpm ({data['status_detak_jantung']})"], ["RPP", f"{data['rpp']:.2f} ({data['status_rpp']})"],
            ["Merokok", "Ya" if data['merokok'] == "ya" else "Tidak"], ["Olahraga", "Ya" if data['olahraga'] == "ya" else "Tidak"],
            ["Penyakit Bawaan", data['riwayat'] if data['riwayat'] in ["jantung", "diabetes", "hipertensi"] else "-"],
            ["Sakit", "Ya" if data['sakit'] == "ya" else "Tidak"], ["Minum Hari Ini", "Ya" if data['minum'] == "ya" else "Tidak"],
            ["Alergi", "Ya" if data['alergi'] == "ya" else "Tidak"], ["Asma", "Ya" if data['asma'] == "ya" else "Tidak"],
            ["Detak Jantung Maks", f"{data['Detak_Jantung_Maks']} bpm"],
            ["Zona Moderat", f"{data['zona_moderat_bawah']} - {data['zona_moderat_atas']} bpm"],
            ["Zona Intens", f"{data['zona_intens_bawah']} - {data['zona_intens_atas']} bpm"]
        ]
        area_teks_hasil.insert(tk.END, tabulate(data_tabel, headers=["Parameter", "Nilai"], tablefmt="grid") + "\n\n")

        catatan_dan_saran = [
            ("CATATAN:\n", "bold"),
            ("Untuk indeks massa tubuh:\n", None),
            (" - <18.5: Berat Badan Kurang\n", "orange"),
            (" - 18.5 - 25: Normal\n", "green"),
            (" - 25 - 30: Berat Badan Berlebih\n", "red"),
            (" - >30: Obesitas\n", "red"),
            ("\nDetak jantung:\n", None),
            (" - <60 bpm: Rendah (Normal untuk atlet)\n", "orange"),
            (" - 60 - 100 bpm: Normal untuk orang dewasa\n", "green"),
            (" - 101 - 120 bpm: Sedikit tinggi (takikardia ringan)\n", "red"),
            (" - >120 bpm: Tinggi (takikardia)\n", "red"),
            ("\n📚 Penjelasan RPP:\n", None),
            ("- WHO: RPP yang tinggi dikaitkan dengan peningkatan risiko penyakit jantung, diabetes tipe 2, dan sindrom metabolik.\n", None),
            ("- Untuk pria: RPP > 0.90 → risiko meningkat\n", None),
            ("- Untuk wanita: RPP > 0.85 → risiko meningkat\n", None),
            ("➡️ Sebaiknya konsultasikan ke dokter, lakukan diet seimbang, rutin olahraga, dan hindari gaya hidup sedentary.\n", "red") if data['status_rpp'] == "Tinggi" else ("➡️ RPP normal. Tetap pertahankan pola hidup sehat!\n", "green"),
            ("\n💡 Saran untuk kamu:\n", "bold"),
            ("- 🚭 Merokok dapat meningkatkan risiko penyakit jantung dan paru-paru.\n", "red") if data['merokok'] == "ya" else ("- ✅ Tidak merokok sangat baik untuk kesehatan.\n", "green"),
            ("- 🏃 Olahraga secara teratur sangat bagus untuk kesehatan.\n", "green") if data['olahraga'] == "ya" else ("- ⚠️ Kamu sebaiknya mulai rutin berolahraga.\n", "orange"),
            ("- ‼️ Anda memiliki risiko terkena penyakit jantung lebih besar, sebaiknya anda banyak melakukan aktivitas fisik, menjaga pola makan, dan kurangi stres berlebihan.\n", "red") if data['riwayat'] == "jantung" else \
            ("- ‼️ Anda memiliki risiko diabetes lebih besar, sebaiknya jaga pola makan anda dan kurangi makanan dengan gula yang tinggi, perbanyaklah berolahraga !!\n", "red") if data['riwayat'] == "diabetes" else \
            ("- ‼️ Atur emosi anda dan jangan stres berlebihan !!\n", "red") if data['riwayat'] == "hipertensi" else \
            ("- 😁 Tetap jaga kesehatan ya...\n", "green"),
            ("- Istirahat yang cukup 😴. Jangan lupa minum obat dan minum air putih juga untuk menjaga hidrasi.\n", "orange") if data['sakit'] == "ya" else ("- Pertahankan kehidupan bugar dan sehat kamu ya, jaga pola makan dan hindari hal yang dapat memicu kamu sakit 💪.\n", "green"),
            ("- Bagus, pertahankan kebiasaan minum 8 gelas dalam sehari 😁👍.\n", "green") if data['minum'] == "ya" else ("- ⚠️ Waaahhh, tubuh kamu butuh cairan agar bisa fokus. Cobalah minum air putih sekarang.\n", "orange"),
            ("- Pastikan selalu memeriksa bahan makanan dan selalu bawa obat kamu kemana kamu pergi.\n", "red") if data['alergi'] == "ya" else ("- Tetap berhati-hati pada makanan yang kamu makan, apalagi mencoba makanan baru.\n", "green"),
            ("- Mungkin itu adalah gejala asma. Coba kamu konsultasikan ke dokter dan hindari lingkungan yang berdebu dan berasap 😣.\n", "red") if data['asma'] == "ya" else ("- Tetap jaga kualitas udara kamu ya dan hindari asap rokok.\n", "green")
        ]
        for teks, tag in catatan_dan_saran:
            area_teks_hasil.insert(tk.END, teks, tag)

        area_teks_hasil.config(state=tk.DISABLED)
        area_teks_hasil.tag_config("bold", font=("Consolas", 10, "bold"))
        area_teks_hasil.tag_config("red", foreground="red")
        area_teks_hasil.tag_config("green", foreground="green")
        area_teks_hasil.tag_config("orange", foreground="orange")

        # Grafik Matplotlib
        bingkai_grafik = tk.Frame(wadah_hasil, bg="#f8f8f8")
        bingkai_grafik.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        fig, ax = plt.subplots(figsize=(6, 4))
        label_grafik = ['IMT', 'Detak Jantung', 'RPP', 'Detak Jantung Maks']
        nilai_grafik = [data['imt'], data['detak_jantung'], data['rpp'], data['Detak_Jantung_Maks']]
        warna = ["#0CDBC7", "#1A29C8FF", "#A3A234", "#A14984"]
        batang = ax.bar(label_grafik, nilai_grafik, color=warna) 
        ax.set_title("Hasil Pemeriksaan Kesehatan")
        ax.set_ylabel("Nilai")
        for bar in batang:
            tinggi = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, tinggi + 0.5, f'{tinggi:.1f}', ha='center', va='bottom', fontsize=9)
        ax.set_ylim(bottom=0)

        kanvas = FigureCanvasTkAgg(fig, master=bingkai_grafik)
        widget_kanvas = kanvas.get_tk_widget()
        widget_kanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        kanvas.draw()
        plt.close(fig) # Penting: Tutup figur untuk mencegah kebocoran memori Matplotlib

        # Simpan data menggunakan fungsi yang sudah disederhanakan
        simpan_data_ke_berkas(data)

        tk.Button(wadah_hasil, text="Kembali ke Menu Utama", command=self.buat_layar_menu_utama,
                  font=("Helvetica Neue", 12), bg="#007bff", fg="white", activebackground="#0056b3", activeforeground="white", relief="raised", bd=2).pack(pady=15)

    def tampilkan_layar_data_berkas(self):
        """
        Menampilkan layar untuk melihat data kesehatan yang tersimpan di berkas.
        """
        self.bersihkan_bingkai_saat_ini()
        bingkai_data_berkas = tk.Frame(self.master, padx=30, pady=30, bg="#f8f8f8")
        bingkai_data_berkas.pack(fill="both", expand=True)
        self.bingkai_saat_ini = bingkai_data_berkas

        tk.Label(bingkai_data_berkas, text="Data Kesehatan Tersimpan",
                 font=("Helvetica Neue", 16, "bold"), fg="#333", bg="#f8f8f8").pack(pady=(0, 20))

        teks_konten_berkas = scrolledtext.ScrolledText(bingkai_data_berkas, wrap=tk.WORD, font=("Consolas", 10), width=80, height=30, bd=1, relief="solid")
        teks_konten_berkas.pack(fill="both", expand=True, pady=10)

        teks_konten_berkas.insert(tk.END, baca_data_dari_berkas())
        teks_konten_berkas.config(state=tk.DISABLED)

        tk.Button(bingkai_data_berkas, text="Kembali ke Menu Utama", command=self.buat_layar_menu_utama,
                  font=("Helvetica Neue", 12), bg="#007bff", fg="white", activebackground="#0056b3", activeforeground="white", relief="raised", bd=2).pack(pady=15)

if __name__ == "__main__":
    awal = tk.Tk()
    aplikasi = AplikasiKesehatan(awal)
    awal.mainloop()