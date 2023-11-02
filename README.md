## Struktur Kondisi
- Pada Latihan 1, kita membuat program sederhana dengan input 2 buah bilangan, kemudian
tentukan bilangan terbesar dari kedua bilangan tersebut
menggunakan statement if.

1. Kode ini menggunakan input(), kode meminta pengguna untuk memasukkan dua bilangan bulat.
2. Kode kemudian membandingkan kedua bilangan menggunakan pernyataan if. Jika bilangan1 lebih besar dari bilangan2, maka bilangan_terbesar diatur menjadi bilangan1, jika tidak, maka diatur menjadi bilangan2.
Terakhir, kode mencetak bilangan terbesar ke konsole / terminal.
3. Hasil akhirnya adalah kode ini akan menampilkan bilangan terbesar dari dua bilangan yang dimasukkan oleh pengguna.
![Screenshot_20231102_222910](https://github.com/ficzclay/praktikum4/assets/148204078/2d5bd01e-3e34-4539-8250-256af1bd307c)


- Lalu pada latihan 2, kita membuat program untuk mengurutkan data berdasarkan input sejumlah
data (minimal 3 variable input atau lebih), kemudian tampilkan
hasilnya secara berurutan mulai dari data terkecil.

1. Program ini meminta pengguna memasukkan jumlah data, kemudian pengguna memasukkan data tersebut. Setelah mengumpulkan semua data, program mengurutkan data dari yang terkecil hingga yang terbesar.
2. Hasil akhirnya adalah kode ini akan menerima input dari pengguna, mengurutkan data yang dimasukkan, dan kemudian mencetak hasil pengurutan tanpa desimal.
![Screenshot_20231102_223357](https://github.com/ficzclay/praktikum4/assets/148204078/8b57b119-4e54-45ec-b8b2-0d46f133fb65)

## Perulangan
- Pada latihan 1, kita membuat program dengan perulangan bertingkat (nested) for yang
menghasilkan output sebagai berikut:
![Screenshot_20231102_221441](https://github.com/ficzclay/praktikum4/assets/148204078/d235ee7e-0c84-4704-bde3-e61e693fc389)
1. Kode ini mencetak pola tabel 10x10 dengan angka yang dihasilkan dari penjumlahan variabel i dan j dalam loop. Setiap baris mencetak hasil penjumlahan i + j, dengan angka-angka tersebut dipisahkan oleh tab ("\t"), dan kemudian mencetak baris baru untuk mengawali baris baru.
![Screenshot_20231102_224842](https://github.com/ficzclay/praktikum4/assets/148204078/dfcaea86-cffe-4faa-a4f9-11758b3b3f4b)

- Pada latihan 2, kita membuat program<br>
  ```Tampilkan n bilangan acak yang lebih kecil dari 0.5.```<br>
  ```nilai n diisi pada saat runtime```<br>
  ```anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya```

1. Kode tersebut meminta pengguna memasukkan jumlah n. Jika n lebih besar dari 0, maka kode akan menghasilkan dan mencetak n bilangan acak yang kurang dari 0.5. Jika n tidak lebih besar dari 0, maka kode akan memberi pesan bahwa n harus lebih besar dari 0.
2. Hasil akhirnya adalah kode ini akan mencetak bilangan acak yang kurang dari 0.5 sebanyak n kali sesuai dengan jumlah yang dimasukkan oleh pengguna.
![Screenshot_20231102_231157](https://github.com/ficzclay/praktikum4/assets/148204078/3541c7ef-035a-496f-b167-b778c0cac37e)

## Tugas Praktikum 2
- Buat program sederhana dengan input tiga buah bilangan, dari ketiga bilangan
tersebut tampilkan bilangan terbesarnya. Gunakan statement if.
1. Program akan meminta pengguna untuk memasukkan tiga bilangan: bilangan1, bilangan2, dan bilangan3.
2. Tentukan sebuah variabel bernama "bilangan_terbesar" untuk menyimpan bilangan terbesar.
3.Gunakan pernyataan if dan elif untuk memeriksa kondisi berikut:<br>
Jika bilangan1 lebih besar dari bilangan2 dan bilangan1 lebih besar dari bilangan3, maka bilangan1 adalah bilangan terbesar.<br>
Jika bilangan2 lebih besar dari bilangan1 dan bilangan2 lebih besar dari bilangan3, maka bilangan2 adalah bilangan terbesar.<br>
Jika kedua kondisi di atas tidak terpenuhi, maka bilangan terbesar adalah bilangan3.
4. program akan mencetak bilangan terbesar ke terminal / konsole.
![Screenshot_20231102_232636](https://github.com/ficzclay/praktikum4/assets/148204078/6939e0bd-c1ba-459c-a1a1-71eafadb9539)

- Berikut flowchart-nya<br>
  ![Screenshot_20231103_004139](https://github.com/ficzclay/praktikum4/assets/148204078/66d0de9c-26da-4a73-9282-dc7c8dac54c3)

## Tugas Praktikum 3

### Latihan 1
- Tampilkan n bilangan acak yang lebih kecil dari 0.5.<br>
nilai n diisi pada saat runtime<br>
anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya<br>
gunakan fungsi random() yang dapat diimport terlebih dahulu<br>

1. Pengguna diminta untuk memasukkan nilai n, yang merupakan jumlah bilangan acak yang akan dihasilkan dan dicetak.
2. Program menggunakan perulangan while untuk menghasilkan bilangan acak. Dalam setiap iterasi perulangan:<br>
random_number diisi dengan nilai bilangan acak yang dihasilkan oleh random.random(). Fungsi ini menghasilkan bilangan acak dalam rentang dari 0 hingga kurang dari 1.<br>
Kemudian, program memeriksa apakah random_number kurang dari 0.5. Jika benar, maka random_number akan dicetak.<br>
Variabel count digunakan untuk menghitung berapa kali bilangan acak telah dicetak.
3. Proses ini diulangi hingga jumlah bilangan acak yang lebih kecil dari 0.5 yang telah dicetak mencapai n, sesuai dengan jumlah yang dimasukkan oleh pengguna.
![Screenshot_20231103_012324](https://github.com/ficzclay/praktikum4/assets/148204078/5f0811df-9cbd-41d1-bc3f-5cb8d641d770)

### Latihan 2
- Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan. Masukkan angka 0 untuk berhenti.
1. Program ini meminta pengguna untuk memasukkan sejumlah bilangan. Selama proses tersebut, program akan menyimpan bilangan terbesar yang telah dimasukkan. Ketika pengguna memasukkan "0" atau memutuskan untuk berhenti, program akan mencetak bilangan terbesar yang telah dimasukkan, jika ada. Tujuannya adalah untuk menemukan bilangan terbesar di antara bilangan yang dimasukkan oleh pengguna.
![Screenshot_20231103_013634](https://github.com/ficzclay/praktikum4/assets/148204078/a6a6f640-8f44-491f-bafe-b3abd3c45ea4)

### program.py
- Buat program sederhana dengan perulangan: program1.py
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
bulan berjalan usahanya.
1. Program ini menghitung total keuntungan selama 8 bulan dengan modal awal 100 juta rupiah. Kode tersebut:
Menginisialisasi modal awal dan total keuntungan.<br>
Menggunakan perulangan untuk menghitung keuntungan pada bulan tertentu, yaitu pada bulan ke-3, ke-5, dan ke-8.<br>
Menambahkan keuntungan tersebut ke total keuntungan.<br>
Menampilkan total keuntungan setelah 8 bulan berjalan usahanya.
![Screenshot_20231103_020712](https://github.com/ficzclay/praktikum4/assets/148204078/46b51996-5836-4987-901e-ec2793b32862)



## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir praktikum4
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# praktikum4” >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add README.md
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
   contoh: praktikum4
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository


- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```




## Berikut bukti pengerjaan-nya
![Screenshot_20231102_215038](https://github.com/ficzclay/praktikum4/assets/148204078/bf5eec4d-b879-45f0-81fb-25db6905b5d8)

![Screenshot_20231102_215047](https://github.com/ficzclay/praktikum4/assets/148204078/03737632-1d06-49a6-9fd8-9e22a4e06a68)


