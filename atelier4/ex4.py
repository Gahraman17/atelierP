from random import *
def extract_elements_list(list_in_which_to_choose,int_nbr_of_element_to_extract):
     list_ret = [0]*int_nbr_of_element_to_extract
     for i in range(len(list_ret)):
          j= randint(0, len(list_in_which_to_choose)-1)
          list_ret[i]= list_in_which_to_choose[j]
        
     return  list_ret
     
lst_sorted=[i for i in range(5)]
print(lst_sorted)
print('Liste de départ',lst_sorted)
sublist = extract_elements_list(lst_sorted,1)
print('La sous liste extraite est',sublist)
print('Liste de départ après appel de la fonction est',lst_sorted)