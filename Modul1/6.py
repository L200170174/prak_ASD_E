def cetakbilanganprima():
    prima=list()
    for i in range(2,1000):
        a = True
        for iter in prima:
            if(i%iter==0):
                a=False
                break
        if(a):
            print(i)
            prima.append(i)
cetakbilanganprima()
