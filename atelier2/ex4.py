def histo(f):  
    MAXVALEUR = max(f)
    H = [0] * (MAXVALEUR +1) 
    for i in f:
            H[i] +=1
    return H      
  
def  est_injective(F):
    for i in histo(F):
        if i >1:
            return False      
    return True 

def  est_surjective(F):
    for i in histo(F):
        if i <1:
            return False      
    return True 

def est_bijective(F):
    return est_surjective(F) and est_injective(F)

def afficheHisto(F):
    H = histo(F)
    leng = max(histo(F))

    for i in range(leng):
     for index in range(len(H)):
        if H[index] >=1 and leng -i == H[index]:
            print(" # ",end="")
            H[index] -= 1
        else:
            print("   ",end="")
     print("\n",end="")        


F2=[6,5,6,7,4,2,1,5]

afficheHisto(F2)
