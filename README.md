# 🇮🇩 NIK Generator Indonesia (16-Digit Standard)

**NIK Generator Indonesia** adalah *tools* berbasis Python untuk menghasilkan data dummy **Nomor Induk Kependudukan (NIK)** secara massal. Script ini dirancang untuk keperluan *data seeding*, *testing database*, simulasi aplikasi, atau pengujian sistem informasi (Quality Assurance).

Script ini terintegrasi dengan **API Data Wilayah Indonesia** secara *real-time*, sehingga kode wilayah (Provinsi, Kota/Kab, Kecamatan) yang dihasilkan valid dan sesuai dengan data pemerintahan terbaru.

## ✨ Fitur Utama

* **Valid Logic 16-Digit:** Menggunakan struktur tahun `YY` (2 digit) pada blok tanggal lahir, memastikan total panjang NIK tepat 16 digit sesuai standar KTP-el.
* **Real-time Region Data:** Mengambil data wilayah langsung dari repositori [ibnux/data-indonesia](https://github.com/ibnux/data-indonesia). Tidak perlu setup database lokal.
* **Smart Date & Gender Logic:**
    * **Laki-laki:** Tanggal lahir 01-31.
    * **Perempuan:** Tanggal lahir ditambahkan 40 (41-71).
    * Menangani validasi jumlah hari dalam bulan dan tahun kabisat.
* **Dual Mode:**
    * **Mode Spesifik:** Pilih Provinsi > Kota > Kecamatan melalui menu interaktif.
    * **Mode Acak:** Generate NIK dari wilayah random di seluruh Indonesia.
* **Multi-Format Export:** Simpan hasil generate ke:
    * `JSON` (Data terstruktur)
    * `TXT` (Plain text report)
    * `XLSX` (Excel Native - *requires pandas*)
    * `CSV` (Excel Compatible - tanpa library tambahan)

## 🛠️ Persyaratan Sistem

* **Python 3.x** terinstall di komputer.
* **Koneksi Internet** (Diperlukan untuk fitur pemilihan wilayah spesifik).

### Instalasi Library (Opsional)
Script ini menggunakan *Standard Library* Python sehingga bisa berjalan **tanpa instalasi tambahan**. Namun, jika Anda ingin fitur simpan ke **Excel (.xlsx)** asli, jalankan perintah ini:

```bash
pip install pandas openpyxl

```

*> Catatan: Jika library di atas tidak diinstall, script otomatis akan menyimpan dalam format .CSV yang tetap bisa dibuka di Excel.*

## 🚀 Cara Penggunaan

1. **Clone atau Download** repository ini.
2. Buka terminal/command prompt di folder script.
3. Jalankan script:
```bash
python main.py

```


4. **Ikuti instruksi di layar:**
* **Pilih Wilayah:** Ketik `Y` untuk memuat data wilayah Indonesia (pilih Provinsi -> Kab/Kota -> Kecamatan), atau `A` untuk mode acak.
* **Input Tahun:** Masukkan tahun kelahiran (contoh: `1995`) atau tekan `ENTER` untuk tahun acak (range 1970-2005).
* **Jumlah Data:** Masukkan jumlah NIK yang ingin digenerate.


5. **Simpan Data:** Di akhir proses, pilih format penyimpanan yang diinginkan (1-4).

## 🧩 Struktur Logika NIK

Script ini menyusun 16 digit NIK berdasarkan aturan resmi administrasi kependudukan:

`[AA][BB][CC][DD][MM][YY][NNNN]`

| Kode | Deskripsi | Keterangan |
| --- | --- | --- |
| **AA** | Kode Provinsi | 2 Digit |
| **BB** | Kode Kab/Kota | 2 Digit |
| **CC** | Kode Kecamatan | 2 Digit |
| **DD** | Tanggal Lahir | 2 Digit (Jika wanita: Tgl + 40) |
| **MM** | Bulan Lahir | 2 Digit |
| **YY** | Tahun Lahir | 2 Digit Terakhir (Misal 1995 -> 95) |
| **NNNN** | Nomor Urut | 4 Digit (Acak 0001 - 9999) |

## ⚠️ Disclaimer

Aplikasi ini dibuat semata-mata untuk **tujuan edukasi, penelitian, dan pengujian sistem (Development/Testing)**.

* Data NIK yang dihasilkan adalah **Data Sintetis (Dummy)** yang disusun secara matematis menyerupai struktur asli.
* Penulis **tidak bertanggung jawab** atas penyalahgunaan alat ini untuk tindakan ilegal, penipuan, atau pemalsuan dokumen negara.
* Harap gunakan dengan bijak dan etis.

---
