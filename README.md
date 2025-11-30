# praktikum 6

## program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa.

## flowchart 
<img src="output/flowchart.png">

## penjelasan flowchart
- Alur Awal dan Loop: Program dimulai dan langsung masuk ke [Lingkaran] LOOP MENU UTAMA. Ini adalah perulangan tak terbatas (while True) yang memastikan program selalu siap menerima perintah.

- Keputusan Utama (Pilihan): Setelah menerima input Pilihan, alur program akan masuk ke serangkaian [Belah Ketupat] Keputusan. Ini adalah struktur percabangan (if-elif-else) yang menentukan aksi selanjutnya.

- Pemanggilan Fungsi: Ketika sebuah pilihan valid (1, 2, 3, atau 4) dipilih, alur program diarahkan ke [Persegi Panjang Bergaris], yang berarti terjadi pemanggilan fungsi (misalnya, tambah() atau ubah()). Fungsi ini kemudian menjalankan logikanya di cabang terpisah.

- Pengakhiran: Jika pengguna memilih Pilihan 5 (Keluar), alur program keluar dari loop dan berakhir di [Oval] SELESAI.

- Prinsip Modular: Struktur akar ini sangat efektif menunjukkan bahwa logika inti setiap operasi (seperti mencari dan menghapus data) diisolasi di Cabang Fungsi masing-masing, sementara Akar Utama hanya bertugas mengarahkan alur kendali.

## kode pemerograman python (praktikum6.py)
```py
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
        print("\n=== MENU MANAJEMEN NILAI ===")
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
```
## penjelasan kode python
1. Struktur Data (List of Dictionaries)
Program ini menggunakan sebuah List global bernama data_mahasiswa ([]). List ini bertindak sebagai database sementara yang menampung data. Setiap mahasiswa disimpan sebagai Dictionary di dalam List tersebut, yang memiliki pasangan key: value seperti 'nama' dan 'nilai'.

2. Fungsi Utama
Seluruh logika program dijalankan melalui lima bagian utama:

- main_menu(): Ini adalah fungsi pengendali utama yang menampilkan menu interaktif dan terus berulang (loop) sampai pengguna memilih keluar. Ia hanya bertugas menerima pilihan dan memanggil fungsi lain yang sesuai.

- tambah(): Fungsi ini menerima input nama dan nilai dari pengguna. Data tersebut kemudian dikemas dalam bentuk dictionary baru dan ditambahkan ke akhir data_mahasiswa menggunakan metode .append().

- tampilkan(): Fungsi ini memeriksa apakah data_mahasiswa kosong. Jika tidak, ia akan melakukan perulangan (loop) untuk menampilkan semua data nama dan nilai yang tersimpan secara terstruktur.

- hapus(nama): Fungsi ini menerima nama sebagai argumen. Ia kemudian menyaring (filter) atau mencari data di dalam data_mahasiswa yang namanya cocok dengan argumen yang diberikan, lalu menghapus data tersebut dari list.

- ubah(nama): Fungsi ini juga menerima nama sebagai argumen. Ia mencari data yang cocok. Jika ditemukan, ia meminta input nilai_baru dari pengguna, kemudian mengubah (update) nilai lama di dictionary tersebut dengan nilai yang baru.

- Intinya, pemrograman ini menekankan pada penggunaan fungsi untuk membuat kode yang rapi, mudah dikelola, dan setiap fungsi hanya melakukan satu tugas (misalnya, tambah() hanya menambah, tidak menampilkan).

## output
<img src="/output/output6.1.png">
