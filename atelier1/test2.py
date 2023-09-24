def fuct(L):
    LES = []
    for num in L:
        if num <0 :
            LES.insert(0,num)
            
    for num in L:
        if num ==0:
            LES.append(num)
            
    for num in L:
        if num > 0:
            LES.append(num)
            
    return LES


L=[-1,-2,0,1,5,-4,0,7]
LS = fuct(L)
print (LS)


    