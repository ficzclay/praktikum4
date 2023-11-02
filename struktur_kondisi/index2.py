# Meminta pengguna untuk memasukkan jumlah data
jumlah_data = int(input("Masukkan jumlah data: "))

# Membuat list untuk menyimpan data
data = []

# Mengisi list dengan data yang diinputkan
for i in range(1, jumlah_data + 1):
    bilangan = float(input(f"Bilangan ke-{i}: "))
    data.append(bilangan)

# Mengurutkan data
data.sort()

# Menampilkan hasil pengurutan tanpa angka di belakang titik desimal
print("Urutan bilangan:", end=" ")
for bilangan in data:
    print(int(bilangan), end=" ")
