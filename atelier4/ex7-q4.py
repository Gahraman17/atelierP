def bubble_sort(lst_to_sort):
    # Créez une copie de la liste pour ne pas la modifier.
    sorted_list = lst_to_sort.copy()
    
    # Parcourez le tableau de la fin vers le début.
    for i in range(len(sorted_list) - 1, 0, -1):
        # Un indicateur pour vérifier si le tableau est trié lors de cette itération.
        tableau_trié = True
        
        # Parcourez le tableau de gauche à droite.
        for j in range(i):
            if sorted_list[j] > sorted_list[j + 1]:  # Tri croissant, utilisez < pour tri décroissant.
                # Échangez les éléments s'ils ne sont pas dans l'ordre.
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                # Le tableau n'est pas trié lors de cette itération.
                tableau_trié = False
        
        # Si le tableau est trié à la fin de cette itération, inutile de continuer.
        if tableau_trié:
            break
    
    return sorted_list

my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
sorted_lst = bubble_sort(my_lst_to_sort)

print('Avant tri :', my_lst_to_sort)
print('Résultat du tri :', sorted_lst)
print("Après le tri, la liste d'origine n'a pas été modifiée :", my_lst_to_sort)
