#2
A = [18,2673,62333,452221]
B = [1297,683468,2248]

C = A+B
for i in range(len(C)): 
    min_idx = i 
    for j in range(i+1, len(C)): 
        if C[min_idx] > C[j]: 
            min_idx = j 
    
    C[i], C[min_idx] = C[min_idx], C[i]

print (C)
