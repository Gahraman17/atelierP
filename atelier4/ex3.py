from random import *
def choose_element_list(list_in_which_to_choose):
    list_c =0
    j= randint(0, len(list_in_which_to_choose)-1)
    list_c =list_in_which_to_choose[j]
    return list_c

lst_sorted=[i for i in range(10)]
print(lst_sorted)
print('Liste triée de départ',lst_sorted)
e1 = choose_element_list(lst_sorted)
print('A la première exécution',e1,'a été sélectionné')
e2 = choose_element_list(lst_sorted)
print('A la deuxième exécution',e2,'a été sélectionné')
#assert e1 != e2