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

daftar = [c0.no, c1.no, c2.no, c3.no, c4.no, c5.no, c6.no, c7.no, c8.no, c9.no, c10.no]

def quickSort(L, ascending = True): 
    quicksorthelp(L, 0, len(L), ascending)
    
def quicksorthelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += quicksorthelp(L, low, pivot_location, ascending)  
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low] 
    return i - 1, result

def median_of_three(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

print(daftar)
quickSort(daftar)
print(daftar)
