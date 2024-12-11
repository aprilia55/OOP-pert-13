from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

data_mahasiswa = DataMahasiswa()

def menu():
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Tampilkan Daftar Mahasiswa")
        print("5. Cari Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            m = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(m)
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama = input("Masukkan Nama baru: ")
            jurusan = input("Masukkan Jurusan baru: ")
            data_mahasiswa.ubah_mahasiswa(nim, nama, jurusan)
        elif pilihan == "4":
            ViewMahasiswa.tampilkan_daftar(data_mahasiswa.daftar_mahasiswa)
        elif pilihan == "5":
            nim = input("Masukkan NIM yang dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            ViewMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")
