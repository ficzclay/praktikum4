import random

n = int(input("Masukkan jumlah n: "))

if n <= 0:
    print("n harus lebih besar dari 0")
else:
    for _ in range(n):
        while True:
            rand_num = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
            if rand_num < 0.5:
                print(rand_num)
                break