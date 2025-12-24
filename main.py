import random
import os
import sys
import time

# --- PENGATURAN WARNA & TAMPILAN ---
class Col:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(str_text):
    for char in str_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# --- DATA WILAYAH ---
DATA_PROVINSI = {
    '11': 'Aceh', '12': 'Sumatera Utara', '13': 'Sumatera Barat', '14': 'Riau',
    '15': 'Jambi', '16': 'Sumatera Selatan', '17': 'Bengkulu', '18': 'Lampung',
    '19': 'Kep. Bangka Belitung', '21': 'Kep. Riau',
    '31': 'DKI Jakarta', '32': 'Jawa Barat', '33': 'Jawa Tengah', '34': 'DI Yogyakarta',
    '35': 'Jawa Timur', '36': 'Banten',
    '51': 'Bali', '52': 'Nusa Tenggara Barat', '53': 'Nusa Tenggara Timur',
    '61': 'Kalimantan Barat', '62': 'Kalimantan Tengah', '63': 'Kalimantan Selatan',
    '64': 'Kalimantan Timur', '65': 'Kalimantan Utara',
    '71': 'Sulawesi Utara', '72': 'Sulawesi Tengah', '73': 'Sulawesi Selatan',
    '74': 'Sulawesi Tenggara', '75': 'Gorontalo', '76': 'Sulawesi Barat',
    '81': 'Maluku', '82': 'Maluku Utara', '91': 'Papua Barat', '94': 'Papua'
}

# --- LOGIC UTAMA ---
def get_kode_by_name(input_nama):
    if input_nama.lower() in ['all', '', 'semua']:
        return None, "ACAK (Seluruh Indonesia)"
    for kode, nama in DATA_PROVINSI.items():
        if input_nama.lower() in nama.lower():
            return kode, nama
    return None, "Tidak Ditemukan (Default: ACAK)"

def generate_data(jumlah, kode_prov, nama_prov, tahun_kunci=None):
    results = []
    
    print(f"\n{Col.CYAN}[+] Memproses permintaan...{Col.ENDC}")
    time.sleep(0.5) # Efek loading
    
    for i in range(jumlah):
        # 1. PP
        pp = kode_prov if kode_prov else random.choice(list(DATA_PROVINSI.keys()))
        real_prov_name = DATA_PROVINSI.get(pp, "Unknown")
        
        # 2. DD
        dd = f"{random.randint(1, 99):02d}"
        
        # 3. TT
        if tahun_kunci:
            yy = str(tahun_kunci)[-2:]
        else:
            yy = str(random.randint(70, 99))
            if random.random() > 0.8: yy = f"{random.randint(0, 5):02d}"
            
        mm = f"{random.randint(1, 12):02d}"
        dd_tgl = f"{random.randint(1, 28):02d}"
        tt = f"{dd_tgl}{mm}{yy}"
        
        # 4. BB & CCCC
        bb = f"{random.randint(1001, 9999)}"
        cccc = f"{random.randint(1, 9999):04d}"
        
        # 5. XX (Gender)
        val_xx = random.randint(10, 99)
        gender_type = random.choice(['L', 'P'])
        
        if gender_type == 'L':
            if val_xx % 2 == 0: val_xx += 1
            gender_label = "Laki-laki"
        else:
            if val_xx % 2 != 0: val_xx += 1
            if val_xx > 99: val_xx -= 2
            gender_label = "Perempuan"
            
        xx = f"{val_xx}"
        
        full_id = f"{pp}{dd}{tt}{bb}{cccc}{xx}"
        results.append({
            'id': full_id,
            'prov': real_prov_name,
            'gender': gender_label,
            'dob': f"{dd_tgl}/{mm}/{yy}"
        })
        
    return results

# --- INTERFACE ---
def main():
    os.system('color') # Enable ANSI colors on Windows
    clear_screen()
    
    # Banner
    print(f"{Col.HEADER}{'='*60}")
    print(f"   GENERATOR ID DUMMY INDONESIA v2.0   ")
    print(f"{'='*60}{Col.ENDC}")
    
    # Input Section
    print(f"\n{Col.BOLD}[ Langkah 1 ]{Col.ENDC} Pilih Wilayah Target")
    print(f"{Col.WARNING}>> Contoh: Jakarta, Jabar, Bali, Papua (Ketik 'ALL' untuk acak){Col.ENDC}")
    input_wil = input(f"{Col.GREEN}   Masukkan Nama Wilayah : {Col.ENDC}").strip()
    
    kode, nama = get_kode_by_name(input_wil)
    print(f"   {Col.BLUE}-> Terpilih: {nama}{Col.ENDC}")
    
    print(f"\n{Col.BOLD}[ Langkah 2 ]{Col.ENDC} Filter Tahun Lahir")
    input_thn = input(f"{Col.GREEN}   Masukkan Tahun (thn/ALL) : {Col.ENDC}").strip()
    
    thn_fix = None
    if input_thn.lower() not in ['all', '']:
        try:
            thn_fix = int(input_thn)
            print(f"   {Col.BLUE}-> Tahun dikunci: {thn_fix}{Col.ENDC}")
        except:
            print(f"   {Col.FAIL}-> Input invalid, set ke ACAK.{Col.ENDC}")
            
    print(f"\n{Col.BOLD}[ Langkah 3 ]{Col.ENDC} Jumlah Data")
    try:
        jml = int(input(f"{Col.GREEN}   Berapa ID dibuat? : {Col.ENDC}"))
    except:
        jml = 10
        
    # Generate
    data = generate_data(jml, kode, nama, thn_fix)
    
    # Output Table
    clear_screen()
    print(f"{Col.HEADER}=== HASIL GENERATE ({jml} Data) ==={Col.ENDC}\n")
    
    # Table Header
    print(f"{Col.BOLD}{'No':<4} | {'ID DUMMY (20 Digit)':<22} | {'WILAYAH':<20} | {'GENDER':<10}{Col.ENDC}")
    print("-" * 65)
    
    for idx, item in enumerate(data, 1):
        # Warna selang-seling baris agar mudah dibaca
        color_row = Col.CYAN if idx % 2 == 0 else Col.ENDC
        
        print(f"{color_row}{idx:<4} | {item['id']:<22} | {item['prov']:<20} | {item['gender']:<10}{Col.ENDC}")

    print("-" * 65)
    
    # Save Option
    save = input(f"\n{Col.WARNING}[?] Simpan ke file 'hasil_id.txt'? (y/n): {Col.ENDC}").lower()
    if save == 'y':
        with open("hasil_id.txt", "w") as f:
            f.write("ID DUMMY | WILAYAH | GENDER | TANGGAL LAHIR\n")
            for item in data:
                f.write(f"{item['id']} | {item['prov']} | {item['gender']} | {item['dob']}\n")
        print(f"\n{Col.GREEN}[SUCCESS] File berhasil disimpan!{Col.ENDC}")
    else:
        print(f"\n{Col.BLUE}Terima kasih.{Col.ENDC}")

if __name__ == "__main__":
    main()
