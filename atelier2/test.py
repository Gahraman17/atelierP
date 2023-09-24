def histo(f):
    
    MAXVALEUR = max(f)
    H = [0] * (MAXVALEUR +1)
    i=0
    j=0
    for i in range(len(f)):
        for j in range(len(f)+1):
         if f[i] == j:
            H[j] +=1  
    return H



f = [1,1,1,5,8,9,9,5,2]
t = histo(f)
print(t)  
           
           
    