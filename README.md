🇮🇩 NIK Generator Indonesia (16-Digit Standard)

Tools sederhana berbasis Python untuk menghasilkan data dummy Nomor Induk Kependudukan (NIK) Indonesia secara massal. Script ini menggunakan algoritma standar pembentukan NIK KTP (16 Digit) dan terintegrasi dengan API data wilayah Indonesia secara real-time.

Cocok untuk kebutuhan Data Seeding, Testing Database, Penetration Testing (Recon), atau simulasi aplikasi.
✨ Fitur Utama

    Valid Logic 16-Digit: Menggunakan struktur YY pada tahun lahir (bukan YYYY) agar sesuai standar KTP elektronik.

    Real-time Wilayah Data: Mengambil data Provinsi, Kabupaten/Kota, hingga Kecamatan langsung dari repositori ibnux/data-indonesia, tanpa perlu database lokal.

    Smart Date & Gender:

        Otomatis menghitung logika tanggal lahir perempuan (Tanggal + 40).

        Menangani tahun kabisat dan validasi tanggal.

    Flexible Mode:

        Mode Spesifik: Pilih Provinsi > Kota > Kecamatan melalui menu interaktif.

        Mode Acak: Generate NIK dari wilayah random di seluruh Indonesia.

    Multi-Format Export: Simpan hasil generate ke:

        JSON

        TXT

        XLSX (Excel Native - butuh library tambahan)

        CSV (Excel Compatible - tanpa library tambahan)

🛠️ Persyaratan (Requirements)

    Python 3.x

    Koneksi Internet (Untuk fitur Load Data Indonesia)

Library Tambahan (Opsional)

Script ini bisa berjalan tanpa instalasi library apa pun (menggunakan standard library Python). Namun, jika Anda ingin output format .xlsx (Excel asli), install:
Bash

pip install pandas openpyxl

Catatan: Jika library ini tidak ada, script otomatis akan menyimpan ke format .CSV yang tetap bisa dibuka di Excel.
🚀 Cara Penggunaan

    Clone atau Download script ini.

    Jalankan melalui terminal:
    Bash

    python nik_generator.py

    Ikuti Menu Interaktif:

        Pilih Wilayah: Ketik Y untuk memilih wilayah spesifik (Load data online) atau A untuk acak.

        Input Tahun: Masukkan tahun kelahiran spesifik (misal: 1995) atau tekan Enter untuk acak.

        Jumlah Data: Masukkan jumlah NIK yang ingin dibuat (misal: 100).

    Simpan Data: Pilih format penyimpanan di akhir proses (JSON/TXT/XLSX/Tanpa Simpan).

🧩 Struktur Logika NIK

Script ini menyusun 16 digit NIK berdasarkan aturan resmi:

[AA][BB][CC][DD][MM][YY][NNNN]

    AA : Kode Provinsi (2 digit)

    BB : Kode Kabupaten/Kota (2 digit)

    CC : Kode Kecamatan (2 digit)

    DD : Tanggal Lahir (2 digit). Khusus wanita: Tanggal + 40.

    MM : Bulan Lahir (2 digit).

    YY : Tahun Lahir (2 digit terakhir).

    NNNN : Nomor Urut Registrasi (4 digit, acak 0001-9999).

⚠️ Disclaimer

Aplikasi ini dibuat untuk tujuan edukasi dan pengujian sistem (Testing/Development) semata.

    Data NIK yang dihasilkan adalah Data Sintetis (Dummy) yang disusun berdasarkan algoritma matematika NIK.

    Penulis tidak bertanggung jawab atas penyalahgunaan script ini untuk tindakan ilegal, penipuan, atau pemalsuan identitas.

    Gunakan dengan bijak dan etis.
