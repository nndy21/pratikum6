data_mahasiswa = []

def tambah(): 
    nama = input("Masukkan Nama: ")
    nilai = input("Masukkan Nilai (contoh: A, B, C): ")
    data_mahasiswa.append({'nama': nama, 'nilai': nilai})
    print(f"Data {nama} berhasil ditambahkan.")

def tampilkan(): 
    if not data_mahasiswa:
        print("Daftar nilai mahasiswa kosong.")
        return
    print("\n--- DAFTAR NILAI MAHASISWA ---")
    for i, data in enumerate(data_mahasiswa):
        print(f"{i+1}. Nama: {data['nama']}, Nilai: {data['nilai']}")
    print("------------------------------")

def hapus(nama): 
    global data_mahasiswa
    data_mahasiswa = [data for data in data_mahasiswa if data['nama'].lower() != nama.lower()]
    print(f"Data dengan nama {nama} (jika ada) telah dihapus.")

def ubah(nama): 
    for data in data_mahasiswa:
        if data['nama'].lower() == nama.lower():
            nilai_baru = input(f"Masukkan Nilai baru untuk {data['nama']}: ")
            data['nilai'] = nilai_baru
            print(f"Nilai {data['nama']} berhasil diubah menjadi {nilai_baru}.")
            return
    print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

def main_menu():
    while True:
        print("\n=== MENU MANAJEMEN NILAI ===]")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu 1-5: ")

        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama_hapus = input("Masukkan Nama yang akan dihapus: ")
            hapus(nama_hapus)
        elif pilihan == '4':
            nama_ubah = input("Masukkan Nama yang akan diubah: ")
            ubah(nama_ubah)
        elif pilihan == '5':
            print("Program selesai. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main_menu()