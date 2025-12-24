# 🇮🇩 Indo Dummy ID Generator

**Indo Dummy ID Generator** adalah alat berbasis Python CLI (Command Line Interface) untuk membuat data dummy nomor identitas (mirip format KTP/NIK) Indonesia secara massal.

Alat ini dirancang untuk keperluan **testing aplikasi**, **populasi database**, atau keperluan **edukasi**. Script ini menghasilkan ID 20 digit dengan logika validasi wilayah dan jenis kelamin yang dapat disesuaikan.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Fitur Unggulan

* **Pencarian Wilayah Teks:** Cukup ketik nama wilayah (misal: "Jakarta", "Bali", "Jabar"), tidak perlu menghapal kode angka.
* **Data Wilayah Riil:** Menggunakan kode provinsi resmi Indonesia (BPS).
* **Filter Tahun Lahir:** Bisa menentukan tahun kelahiran spesifik atau acak.
* **Validasi Gender:**
    * Digit terakhir Ganjil = Laki-laki
    * Digit terakhir Genap = Perempuan
* **Tampilan Estetik:** Output tabel rapi dengan pewarnaan terminal (CLI) yang nyaman dipandang.
* **Export File:** Opsi untuk menyimpan hasil generate ke dalam file `.txt`.

## 📋 Prasyarat

Pastikan komputer Anda sudah terinstall **Python 3**.
Cek dengan mengetik perintah ini di terminal/CMD:

```bash
python --version
