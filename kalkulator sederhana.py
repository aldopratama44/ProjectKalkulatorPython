def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b  # Diperbaiki: sebelumnya tidak ada return

print("== Kalkulator Sederhana Python ==")
print("Pilih salah satu Operasi Bilangan")
print("1. tambah")
print("2. kurang")
print("3. kali")
print("4. bagi")

pilihan = input("Masukkan pilihan operasi bilangan 1/2/3/4: ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    hasil = tambah(angka1, angka2)
    operasi = "+"
elif pilihan == "2":
    hasil = kurang(angka1, angka2)
    operasi = "-"
elif pilihan == "3":
    hasil = kali(angka1, angka2)
    operasi = "*"
elif pilihan == "4":
    if angka2 != 0:
        hasil = bagi(angka1, angka2)
        operasi = "/"
    else:
        hasil = "Tak Terdefinisi (pembagian dengan nol)"
        operasi = "/"
else:
    hasil = "Pilihan tidak valid"
    operasi = "?"

print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")