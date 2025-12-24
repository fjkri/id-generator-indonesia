import json
import urllib.request
import random
import datetime
import csv
import sys

# --- KONFIGURASI API ---
BASE_URL = "https://ibnux.github.io/data-indonesia"

def fetch_data(endpoint):
    """Mengambil data JSON dari URL tanpa library eksternal"""
    try:
        url = f"{BASE_URL}/{endpoint}"
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return data
    except Exception as e:
        print(f"[Error Koneksi] Gagal mengambil data: {e}")
        return []
    return []

# --- FITUR WILAYAH ---
def menu_pilih_wilayah_lengkap():
    print("\nSedang mengambil data Provinsi se-Indonesia...", end="\r")
    provinsi_list = fetch_data("propinsi.json")
    
    if not provinsi_list:
        print("\nGagal terhubung. Cek internet.")
        return None

    # 1. PILIH PROVINSI
    print("\n" + "="*40)
    print("   PILIH PROVINSI")
    print("="*40)
    for p in provinsi_list:
        print(f"[{p['id']}] {p['nama']}")
    
    id_prov = input("\n>> Masukkan Kode Provinsi: ")
    nama_prov = next((p['nama'] for p in provinsi_list if p['id'] == id_prov), None)
    if not nama_prov: return None

    # 2. PILIH KABUPATEN
    print(f"\nMengambil data Kabupaten di {nama_prov}...", end="\r")
    kab_list = fetch_data(f"kabupaten/{id_prov}.json")
    
    print("\n" + "="*40)
    print(f"   PILIH KAB/KOTA (PROV: {nama_prov})")
    print("="*40)
    for k in kab_list:
        print(f"[{k['id']}] {k['nama']}")

    id_kab_full = input("\n>> Masukkan Kode Kab/Kota: ")
    nama_kab = next((k['nama'] for k in kab_list if k['id'] == id_kab_full), None)
    if not nama_kab: return None

    # 3. PILIH KECAMATAN
    print(f"\nMengambil data Kecamatan di {nama_kab}...", end="\r")
    kec_list = fetch_data(f"kecamatan/{id_kab_full}.json")
    
    print("\n" + "="*40)
    print(f"   PILIH KECAMATAN (KAB: {nama_kab})")
    print("="*40)
    for c in kec_list:
        print(f"[{c['id']}] {c['nama']}")

    id_kec_full = input("\n>> Masukkan Kode Kecamatan: ")
    nama_kec = next((c['nama'] for c in kec_list if c['id'] == id_kec_full), None)
    if not nama_kec: return None

    kode_final = f"{id_prov}{id_kab_full[2:4]}{id_kec_full[4:6]}"
    
    print(f"\n[SUKSES] Wilayah: {nama_prov}, {nama_kab}, {nama_kec}")
    return kode_final, f"{nama_prov}, {nama_kab}, {nama_kec}"

# --- GENERATOR LOGIC ---
def generate_nik_batch(jumlah, input_wilayah=None, nama_wilayah="Acak", input_tahun=None):
    daftar_nik = []
    
    for i in range(jumlah):
        # 1. Wilayah
        if input_wilayah:
            kode_wilayah = input_wilayah
        else:
            prov = random.randint(11, 90)
            kab = random.randint(1, 99)
            kec = random.randint(1, 99)
            kode_wilayah = f"{prov}{kab:02d}{kec:02d}"

        # 2. Tanggal
        if input_tahun and len(input_tahun) == 4:
            tahun = int(input_tahun)
        else:
            tahun = random.randint(1970, 2005)
        
        start_date = datetime.date(tahun, 1, 1)
        end_date = datetime.date(tahun, 12, 31)
        days_between = (end_date - start_date).days
        tgl_lahir_obj = start_date + datetime.timedelta(days=random.randint(0, days_between))

        # 3. Gender
        jenis_kelamin = random.choice(['L', 'P'])
        hari_final = tgl_lahir_obj.day + 40 if jenis_kelamin == 'P' else tgl_lahir_obj.day
            
        str_hari = f"{hari_final:02d}"
        str_bulan = f"{tgl_lahir_obj.month:02d}"
        str_tahun = str(tgl_lahir_obj.year)[-2:] 

        kode_tanggal = f"{str_hari}{str_bulan}{str_tahun}"
        str_urut = f"{random.randint(1, 9999):04d}"

        nik = f"{kode_wilayah}{kode_tanggal}{str_urut}"
        
        daftar_nik.append({
            'NO': i+1,
            'NIK': nik,
            'GENDER': jenis_kelamin,
            'TGL_LAHIR': tgl_lahir_obj.strftime('%d-%m-%Y'),
            'WILAYAH': nama_wilayah
        })

    return daftar_nik

# --- FUNGSI SIMPAN DATA ---
def simpan_data(data_list):
    print("\n" + "="*40)
    print("   MENU PENYIMPANAN DATA")
    print("="*40)
    print("1. Simpan sebagai JSON (.json)")
    print("2. Simpan sebagai TEXT (.txt)")
    print("3. Simpan sebagai EXCEL (.xlsx)")
    print("4. Tidak Disimpan (Keluar)")
    
    pilihan = input("Pilih format (1-4): ")
    nama_file = "hasil_generate_nik"

    if pilihan == '1':
        with open(f"{nama_file}.json", "w") as f:
            json.dump(data_list, f, indent=4)
        print(f"\n[BERHASIL] Data disimpan di: {nama_file}.json")

    elif pilihan == '2':
        with open(f"{nama_file}.txt", "w") as f:
            f.write("DAFTAR GENERATE NIK\n")
            f.write("===================\n")
            for item in data_list:
                f.write(f"{item['NO']}. {item['NIK']} | {item['GENDER']} | {item['TGL_LAHIR']} | {item['WILAYAH']}\n")
        print(f"\n[BERHASIL] Data disimpan di: {nama_file}.txt")

    elif pilihan == '3':
        try:
            import pandas as pd
            df = pd.DataFrame(data_list)
            df.to_excel(f"{nama_file}.xlsx", index=False)
            print(f"\n[BERHASIL] Data disimpan di: {nama_file}.xlsx")
        except ImportError:
            print("\n[INFO] Library 'pandas' tidak ditemukan.")
            print("Mengalihkan penyimpanan ke format CSV (Excel Compatible).")
            
            with open(f"{nama_file}.csv", "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=data_list[0].keys())
                writer.writeheader()
                writer.writerows(data_list)
            print(f"[BERHASIL] Data disimpan di: {nama_file}.csv (Bisa dibuka di Excel)")

    else:
        print("\nProgram selesai tanpa menyimpan.")

# --- MAIN ---
def main():
    print("="*60)
    print("   GENERATOR NIK INDONESIA")
    print("="*60)

    # 1. Wilayah
    print("\n1. Tentukan Wilayah:")
    print("   [Y] Ya, load data Indonesia")
    print("   [A] Acak / Random saja")
    
    opsi = input("Pilihan (Y/A): ").upper()
    kode_wilayah = None
    nama_wilayah = "Acak / Random"

    if opsi == 'Y':
        hasil_wilayah = menu_pilih_wilayah_lengkap()
        if hasil_wilayah:
            kode_wilayah, nama_wilayah = hasil_wilayah
        else:
            print("Mode ACAK aktif.")
    
    # 2. Parameter Lain
    thn_input = input("\n2. Tahun Kelahiran (YYYY) [Enter untuk Acak]: ")
    try:
        jml_input = input("3. Jumlah NIK: ")
        jumlah = int(jml_input)
    except:
        jumlah = 1

    # 3. Eksekusi
    hasil = generate_nik_batch(jumlah, kode_wilayah, nama_wilayah, thn_input)

    # 4. TAMPILKAN SEMUA DATA (MODIFIED)
    print("\n" + "="*60)
    print(f"{'NO':<4} | {'NIK (16 DIGIT)':<20} | {'GENDER':<4} | {'TGL LAHIR'}")
    print("-" * 60)
    
    # Loop ini akan menampilkan SEMUA data tanpa dipotong
    for item in hasil:
        print(f"{item['NO']:<4} | {item['NIK']:<20} | {item['GENDER']:<4} | {item['TGL_LAHIR']}")
        
    print("-" * 60)
    print(f"Total {len(hasil)} data ditampilkan.")

    # 5. Simpan
    simpan_data(hasil)

if __name__ == "__main__":
    main()
