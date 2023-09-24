from numpy import integer


def somme_recursive(liste):
    
    if liste == []:
        return 0
    else:  
     return liste[0] + somme_recursive(liste[1:])
    
def factorielle_recursive(nbr)->integer:
    if nbr ==0 : 
        return 1
    else:
     return nbr *factorielle_recursive(nbr - 1)

def longeur(lst : list)->integer:
    if not lst:
        return 0
    else:
        return 1+longeur(lst[1:])
    
def findMin(lst:list )-> integer:
    if not lst:
        return 0
    else: 
        min = findMin(lst[1:])
        if lst[0] < min:
            return lst[0]
        
        elif len(lst)==1:
            return lst[0]
        
        else:
            return min
        
def listPaire(lst:list)->list:
    if not lst:
        return 0
    elif lst[0]%2==0:
     return [lst[0]]+ [listPaire(lst[1:])]
    else: 
        return listPaire(lst[1:])


def concat_list(lst):
    resultat = []  
    if lst !=[]:
        resultat=lst[0]+concat_list(lst[1:])
    
    return resultat
        




ma_liste = [[1,2],[2, 3],[5, 6]]
print ("",ma_liste)
resultat = concat_list(ma_liste)
print(resultat)  
    
  





list=[123,1,2,3,4]
print("",listPaire(list))
    
        
        
        
        
        
        
list =[5,4,6]
print("",findMin(list))





lst =[1,2,3,4]
print("la longeur de liste est",longeur(lst))
    
nbr = 8    
print("factorielle est",factorielle_recursive(nbr))   
    
    
    
ma_liste = [1, 2, 3, 4, 5]
print("La somme des éléments de la liste est :", somme_recursive(ma_liste))

