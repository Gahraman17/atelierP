def selection_sort(lst_to_sort):
    # Créez une copie de la liste pour ne pas la modifier.
    sorted_list = lst_to_sort.copy()
    
    # Parcourez la liste jusqu'à l'avant-dernier élément.
    for i in range(len(sorted_list) - 1):
        min_idx = i  # Supposons que le minimum soit à l'index i.
        
        # Recherchez le minimum dans la partie non triée de la liste.
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_idx]:
                min_idx = j
        
        # Si le minimum n'est pas à l'index i, échangez les éléments.
        if min_idx != i:
            sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
    
    return sorted_list

my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
sorted_lst = selection_sort(my_lst_to_sort)

print('La liste avant tri :', my_lst_to_sort)
print('Le tri par sélection donne :', sorted_lst)
