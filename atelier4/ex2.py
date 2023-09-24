from random import *
def mix_list(list_to_mix):
    i=0
    mix_list = []
    n=len(list_to_mix)
    while i < n:
        j= randint(0, len(list_to_mix)-1)
        if list_to_mix[j] not in mix_list:
            mix_list.append(list_to_mix[j])
            i+=1
    
    return mix_list

lst_sorted=[i for i in range(10)]
print(lst_sorted)
print('Liste triée de départ',lst_sorted)
mixed_list=mix_list(lst_sorted)
print('Liste mélangée obtenue',mixed_list)
print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted)
