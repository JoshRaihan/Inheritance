class Putra(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def berjalan(self):
        print("Berjalan ke depan")

    def berlari(self):
        print("Berlari dengan cepat")


class Putri(Putra):
    pass


b = Putra("Yanto", 170, 68)
print()
print("Nama:", b.nama)
print("Tinggi:", b.tinggi, "cm")
print("Berat:", b.berat, "kg")
b.berjalan()
b.berlari()


a = Putri("Sinta", 150, 59)
print()
print("Nama:", a.nama)
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.berjalan()
a.berlari()