# Inisialisasi variabel untuk menyimpan bilangan terbesar
bilangan_terbesar = None

while True:
    try:
        # Meminta pengguna memasukkan bilangan
        bilangan = float(input("Masukkan sebuah bilangan (0 untuk berhenti): "))

        # Memeriksa apakah pengguna memasukkan 0 untuk berhenti
        if bilangan == 0:
            break

        # Memeriksa apakah bilangan yang dimasukkan lebih besar dari bilangan_terbesar saat ini
        if bilangan_terbesar is None or bilangan > bilangan_terbesar:
            bilangan_terbesar = bilangan

    except ValueError:
        print("Masukkan tidak valid. Masukkan angka atau 0 untuk berhenti.")

if bilangan_terbesar is not None:
    # Menggunakan format string untuk mencetak bilangan terbesar tanpa koma
    print("Bilangan terbesar adalah: {:.0f}".format(bilangan_terbesar))
else:
    print("Tidak ada bilangan yang dimasukkan.")
