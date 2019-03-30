def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []

    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

list = [1,2,4,5,6,8,11,12,20,23]
target = 12
print(binSe(list,target))

list = [1,2,4,5,6,8,11,12,20,23]
target = 13
print(binSe(list,target))
