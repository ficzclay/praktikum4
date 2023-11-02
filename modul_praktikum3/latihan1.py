import random

# Meminta pengguna untuk memasukkan nilai n
n = int(input("Masukkan nilai n: "))

# Menggunakan for loop untuk menghasilkan n bilangan acak
count = 0
while count < n:
    random_number = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    if random_number < 0.5:
        print(random_number)
        count += 1

# Output n bilangan acak yang lebih kecil dari 0.5
