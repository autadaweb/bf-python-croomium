# Panduan Virtual Environment untuk Proyek Python

Dokumen ini menjelaskan cara mengatur Virtual Environment di Linux dan menginstal modul yang diperlukan untuk proyek ini.

## 📌 Prasyarat

- Python 3 harus sudah terinstal di sistem.
- Akses ke terminal.

## 📂 1️⃣ Membuat Virtual Environment

Jalankan perintah berikut di dalam direktori proyek:

```sh
python3 -m venv venv
```

Perintah ini akan membuat folder `venv/` yang berisi lingkungan Python yang terisolasi.

## ▶️ 2️⃣ Mengaktifkan Virtual Environment

Untuk mengaktifkan Virtual Environment, jalankan perintah:

```sh
source venv/bin/activate
```

Jika berhasil, terminal akan menampilkan `(venv)` di awal prompt.

## 📦 3️⃣ Menginstal Modul yang Dibutuhkan

Setelah Virtual Environment aktif, instal modul yang diperlukan:

```sh
pip install -r requirements.txt
```

## 🌍 4️⃣ Menginstal Browser Playwright

Jika menggunakan `playwright` untuk otomatisasi web, jalankan perintah ini:

```sh
playwright install && playwright install chromium
```

## 🔠 5️⃣ Kapitalisasi Awal di Setiap Kombinasi

Jika proyek ini menggunakan wordlist generator, pastikan setiap kombinasi kata memiliki huruf kapital di awal. Hal ini akan membantu variasi kombinasi tetap optimal.

## ▶️ 6️⃣ Menjalankan Skrip Python

Pastikan Virtual Environment aktif, lalu jalankan skrip Python seperti biasa:

```sh
python main.py
```

## ⏳ 7️⃣ Estimasi Waktu Pembuatan Wordlist

Setiap kombinasi membutuhkan sekitar **3 detik** untuk dibuat. Maka estimasi waktu penyelesaian wordlist adalah:

- **1.000 kombinasi** → \~50 menit
- **10.000 kombinasi** → \~8 jam 20 menit
- **100.000 kombinasi** → \~3 hari 11 jam
- **1.000.000 kombinasi** → \~34 hari 17 jam Pastikan Anda mempertimbangkan waktu ini sebelum menjalankan generator dalam skala besar.

### ⏳ Estimasi Waktu Real-Time dalam Progres

Dalam proses brute force, estimasi waktu akan diperbarui secara dinamis berdasarkan jumlah kombinasi yang tersisa. Tampilan progres akan mencantumkan:

- Jumlah kombinasi yang telah dicoba
- Jumlah kombinasi yang tersisa
- Estimasi waktu tersisa dalam format **hari, jam, menit, detik**
- Estimasi penyelesaian secara real-time saat program berjalan

## ❌ 8️⃣ Menonaktifkan Virtual Environment

Jika ingin keluar dari Virtual Environment, gunakan perintah:

```sh
deactivate
```

Setelah itu, terminal akan kembali ke kondisi normal.

## 📘 Cara Menggunakan Repository Ini

1. **Clone Repository Ini**

   ```sh
   https://github.com/autadaweb/bf-python-croomium.git
   cd repository-name
   ```

2. **Buat dan Aktifkan Virtual Environment**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instal Dependensi**

   ```sh
   pip install -r requirements.txt
   ```

4. **Instal Browser Playwright**

   ```sh
   playwright install && playwright install chromium
   ```

5. **Pastikan Kapitalisasi Awal** Jika menggunakan skrip wordlist generator, pastikan setiap kombinasi kata memiliki kapital di awal untuk hasil yang lebih optimal.

6. **Jalankan Aplikasi**

   ```sh
   python main.py
   ```

7. **Keluar dari Virtual Environment**

   ```sh
   deactivate
   ```

## 📌 Catatan

- Pastikan selalu mengaktifkan Virtual Environment sebelum menjalankan proyek.
- Semua modul yang diinstal akan tetap berada di dalam folder `venv/`, menjaga sistem tetap bersih.

Selamat coding! 🚀

