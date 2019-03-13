class Manusia(object):
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us, lk = []):
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        self.listkuliah = lk

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def hapusListKuliah(self, hapus):
        for x in self.listkuliah:
            if hapus in self.listkuliah:
                self.listkuliah.remove(hapus)
            else:
                print("Maaf mata kuliah tidak ada dalam list mata kuliah yang diambil")

m1 = Mahasiswa('Joko', 177, 'Surakarta', 250000)
m2 = Mahasiswa('Toni', 172, 'Papua', 275000)
m3 = Mahasiswa('Sulaiman', 179, 'Bekasi', 240000)
