# Meminta input dari pengguna
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))

# Menentukan bilangan terbesar menggunakan statement if
if bilangan1 > bilangan2:
    bilangan_terbesar = bilangan1
else:
    bilangan_terbesar = bilangan2

# Menampilkan hasil
print("Bilangan terbesar adalah:", bilangan_terbesar)
