modal_awal = 100000000  # Modal awal 100 juta
keuntungan = 0  # Inisialisasi keuntungan

for bulan in range(1, 9):
    if bulan == 3:
        keuntungan += modal_awal * 0.01  # Laba 1% pada bulan ke-3
    elif bulan == 5:
        keuntungan += modal_awal * 0.05  # Laba 5% pada bulan ke-5
    elif bulan == 8:
        keuntungan += modal_awal * 0.03  # Laba 3% pada bulan ke-8

total_keuntungan = modal_awal + keuntungan

print("Total keuntungan selama 8 bulan adalah:", total_keuntungan)