print ("")
M = int(input(" Masukkan modal awal             : "))
r = float(input(" Masukkan suku bunga tahunan (%) : "))
T = int(input(" Masukkan target investasi       : "))

i = 1

print ("")

while M <= T :
    M += M *(r/100)
    print(f" Tahun ke-{i} : modal {M}")

    i = i+1

print ("")
print(f" Target tercapai dalam {i-1} tahun")
print ("")






