def iterasi():
    for i in range(1,100):
        if (i%3)!=0 and (i%5)!=0:
            print(i)
        else:
            if (i%15)==0:
                print("Pyton UMS")
            elif (i%3)==0:
                print("Python")
            elif (i%5)==0:
                print("UMS")
iterasi()
