a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = [[1,2,3],[4,5,6],[7,8,9]]
#1
def konsistenTidak(n):
    x = len(n[0])
    z = 0
    for i in range(len(n)):
        if (len(n[i]) == x):
           z+=1
    if(z == len(n)):
        print("konsisten")
    else:
        print("tidak konsisten")

konsistenTidak(a)
konsistenTidak(b)

#2
def ukuran(n):
    print("Ukuran Matrix = "+str(len(n))+" x "+str(len(n[0])))

ukuran(a)
ukuran(b)
ukuran(c)

#3
def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("Tidak memenuhi syarat")

jumlah(a,b)
jumlah(a,c)

#4
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("Tidak memenuhi syarat")

kali(a,b)
kali(a,c)

#5
def determinan(n):
    if len(n) == len(n[0]):
        bil = [x for x in range(len(n))]
        jum = 0
        for i in range(len(n)):
            total = 1
            for x in range(len(n)):
                total *= n[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(n))]
        bil.reverse()
        jum2 = 0
        for i in range(len(n)):
            total2 = 1
            for x in range(len(n)):
                total2 *= n[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks Harus Bujursangkar")

determinan(a)
determinan(b)
determinan(c)
