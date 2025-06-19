def cari_nama(daftar, nama):
    """Mencari nama dalam daftar kontak (case-insensitive)."""
    for kontak in daftar:
        if kontak["nama"].lower() == nama.lower():
            return kontak["telepon"]
    return None

def tampilkan_daftar_kontak(daftar):
    """Menampilkan daftar nama kontak yang tersedia."""
    print("Daftar nama kontak yang tersedia: ", end="")
    print(", ".join(k["nama"] for k in daftar))

def main():
    # Daftar kontak
    kontak = [
        {"nama": "Andi", "telepon": "08123"},
        {"nama": "Budi", "telepon": "08234"},
        {"nama": "Citra", "telepon": "08345"},
        {"nama": "Dedi", "telepon": "08456"},
        {"nama": "Eka", "telepon": "08567"},
        {"nama": "Fajar", "telepon": "08678"}
    ]

    print("----- Program Cari Nomor Telepon (Linear Search) -----")
    tampilkan_daftar_kontak(kontak)

    # Input dengan validasi berulang
    while True:
        nama_dicari = input("\nMasukkan nama yang ingin dihubungi: ")
        hasil = cari_nama(kontak, nama_dicari)
        if hasil:
            print(f"Hasil pencarian No. Telp {nama_dicari}: {hasil}")
            break
        else:
            print("Kontak tidak ditemukan, mohon masukkan nama yang tersedia.")

if __name__ == "__main__":
    main()
