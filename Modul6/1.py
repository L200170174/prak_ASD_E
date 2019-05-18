class MhsTIF(object):
    def __init__(self, nama, no, kota, us):
        self.nama = nama
        self.no = no
        self.kota = kota
        self.uangSaku = us

c0 = MhsTIF('Adul', 10, 'Sukoharjo', 4000000)
c1 = MhsTIF('Handoko', 31, 'Sragen', 1300000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 15000000)
c3 = MhsTIF('Chika', 28, 'Surakarta', 3500000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 3200000)
c5 = MhsTIF('Doni', 11, 'Salatiga', 3000000)
c6 = MhsTIF('Maya', 13, 'Klaten', 1450000)
c7 = MhsTIF('Husni', 5, 'Wonogiri', 2950000)
c8 = MhsTIF('Lily', 23, 'Klaten', 2550000)
c9 = MhsTIF('Parjo', 44, 'Karanganyar', 1700000)
c10 = MhsTIF('Kamto', 9, 'Purwodadi', 3650000)

daftar1 = [c0.no, c1.no, c2.no, c3.no, c4.no, c5.no, c6.no, c7.no, c8.no, c9.no, c10.no]

daftar2 = [c0.uangSaku, c1.uangSaku, c2.uangSaku, c3.uangSaku, c4.uangSaku, c5.uangSaku, c6.uangSaku, c7.uangSaku, c8.uangSaku, c9.uangSaku, c10.uangSaku]

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        Kiri = A[:mid]
        Kanan = A[mid:]

        mergeSort(Kiri)
        mergeSort(Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(Kiri) and j < len(Kanan):
            if Kiri[i] < Kanan[j]:
                A[k] = Kiri[i]
                i += 1
            else:
                A[k] = Kanan[j]
                j += 1
            k += 1

        while i < len(Kiri):
            A[k] = Kiri[i]
            i += 1
            k += 1

        while j < len(Kanan):
            A[k] = Kanan[j]
            j += 1
            k += 1

        return A

print(daftar1)
mergeSort(daftar1)
print(daftar1)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)
    return A

print('\n')
print(daftar2)
quickSort(daftar2)
print(daftar2)
