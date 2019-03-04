import random
def permainan():
    a=random.randrange(0, 100)
    print("Permainan tebak angka")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")        
    while(True):
        b=int(input("Masukan tebakan : "))
        if(b>a):
            print("Terlalu besar, Coba lagi")
        elif(b<a):
            print("Terlalu kecil, Coba lagi")
        else:
            print("Benar")
            break
permainan()
