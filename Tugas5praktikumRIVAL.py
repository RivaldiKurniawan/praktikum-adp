import math 

ex = "Y"
while (ex.upper() == "Y"): # menggunakan upper() untuk mengubah semua karakter dalam y/n menjadi huruf kapital
    print("Berikut adalah tabel fungsi yang digunakan untuk menghitung sebuah nilai.") # output 1 yang menampilkan struktur fungsi matematika
    print("1. Jika x = 0, f(x) = 4x^3 + 7x - 5")
    print("   Jika x > 0, f(x) = 4x^3 + 7x - 5")
    print("   Jika x < 0, f(x) = 3x^2 - 5x + 1")
    print("2. g(x) = (f(x))^2 - (f(x)")
    print("3. h(x) = f(x) * g(x)")
    print()

    n = int(input("Masukkan banyak data n yang ingin dihitung = "))
    x = []
    for i in range(n):
        x.append(float(input(f"Input nilai x ke-{i+1} = ")))
    print()

    print("|---------------------------------------------------------------|") # membuat tabel supaya memperlihatkan dan membuat output 2
    print("| No.   || (x)     || f(x)      || g(x)        || h(x)          |")
    print("|---------------------------------------------------------------|")

    for i in range(n):
        # mengitung f(x)
        if x[i] == 0:
            f_x = 4 * x[i] ** 3 + 7 * x[i] - 5
        
        elif x[i] > 0:
            f_x = 4 * x[i] ** 3 + 7 * x[i] - 5

        else:
            f_x = 3 * x[i] ** 2 - 5 * x[i] + 1
    
        # mengitung g(x)
        g_x = f_x ** 2 - f_x
        # menghitung h(X)
        h_x = f_x * g_x
        
        print("| {:<6}|| {:<8}|| {:<10.2f}|| {:<11.2f} || {:<13.2f} |".format(i + 1, x[i], f_x, g_x, h_x)) # .format
    
    print("|---------------------------------------------------------------|")
   
    
    ex = input("Apakah anda ingin memasukkan nilai x lagi ? (Y/N)\n")# memilih apa menjutkan (input "y" atau "Y") atau tidak (menginput "N" atau "n")
    print()