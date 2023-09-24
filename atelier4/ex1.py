from random import *

def gen_list_random_int (int_binf=0,int_bsup=9):
         
         int_nbr = [randint(int_binf, int_bsup) for i in range(5)]
         return int_nbr
    
resultat = gen_list_random_int(78,500)       

print(resultat)
