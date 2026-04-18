def cek_prima(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def cek_megaprima(n):
    if not cek_prima(n):
        return False
    digit_prima = {"2","3","5","7"}
    for digit in str(n):
        if digit not in digit_prima:
            return False
    return True

while True :
    Kiri =int(input("Masukkan Bilangan Kiri  : "))
    Kanan =int(input("Masukkan Bilangan Kanan : "))

    if Kiri < Kanan:
        break
    else:
        print("Bilangan Kiri Harus Lebih Kecil Dari Bilangan Kanan!")

print("Bilangan Megaprima : ")
jumlah = 0

for n in range(Kiri, Kanan+1):
    if cek_megaprima(n):
        digit = " , ".join(list(str(n)))
        print(f"{n} -> digitnya : {digit} ")
        jumlah+=1

print(f"Jumlah Bilangan Megaprima Adalah : {jumlah}")
