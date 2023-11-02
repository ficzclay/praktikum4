modal_awal = 100000000  # Modal awal 100 juta
total_keuntungan = 0

for bulan in range(1, 9):
    if bulan in [3, 4]:
        keuntungan = modal_awal * 1 / 100  # Laba 1% pada bulan ke-3 dan ke-4
    elif bulan == 5:
        keuntungan = modal_awal * 5 / 100  # Laba 5% pada bulan ke-5
    elif bulan == 8:
        keuntungan = modal_awal * 2 / 100  # Penurunan laba 2% pada bulan ke-8
    else:
        keuntungan = 0  # Bulan lainnya belum mendapatkan laba

    total_keuntungan += keuntungan
    modal_awal += keuntungan

modal_awal = 100000000  # Modal awal sebesar 100 juta
total_laba = 0  # Inisialisasi total laba

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0  # Bulan 1 dan 2, laba 0%
    elif bulan == 3:
        laba = 0.01 * modal_awal  # Bulan 3, laba 1%
    elif bulan == 5:
        laba = 0.05 * modal_awal  # Bulan 5, laba 5%
    elif bulan == 8:
        laba = 0.03 * modal_awal  # Bulan 8, laba 3%
    else:
        laba = 0.02 * modal_awal  # Bulan-bulan lain, laba 2%

    total_laba += laba  # Menambahkan laba bulan ini ke total laba
    print(f'laba bulan ke- {bulan} sebesar: {laba}')

print(f'Total laba adalah: {total_laba}')
