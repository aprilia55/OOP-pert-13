class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"{self.nim} - {self.nama} ({self.jurusan})"

class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.daftar_mahasiswa = [m for m in self.daftar_mahasiswa if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama, jurusan):
        for m in self.daftar_mahasiswa:
            if m.nim == nim:
                m.nama = nama
                m.jurusan = jurusan

    def cari_mahasiswa(self, nim):
        for m in self.daftar_mahasiswa:
            if m.nim == nim:
                return m
        return None
