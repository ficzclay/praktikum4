# Minta tiga bilangan dari pengguna
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

# Tentukan bilangan terbesar menggunakan statement if
if bilangan1 >= bilangan2 and bilangan1 >= bilangan3:
    bilangan_terbesar = bilangan1
elif bilangan2 >= bilangan1 and bilangan2 >= bilangan3:
    bilangan_terbesar = bilangan2
else:
    bilangan_terbesar = bilangan3

# Tampilkan bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar)
