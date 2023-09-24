def sort_list(lst):
    
    sorted_lst = lst.copy()
    n = len(sorted_lst)

    # Parcourez la liste
    for i in range(n - 1):
        # La variable swapped indique si des échanges ont eu lieu pendant cette passe.
        swapped = False

        # Parcourez la liste jusqu'à l'avant-dernier élément.
        for j in range(0, n - 1):
            # Comparez les éléments adjacents.
            if sorted_lst[j] > sorted_lst[j + 1]:
                # Échangez les éléments s'ils ne sont pas dans l'ordre croissant.
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True

        # Si aucune inversion n'a eu lieu pendant cette passe, la liste est déjà triée.
        if not swapped:
            break

    return sorted_lst

list = [5, 2, 9, 1, 5]
sorted_result = sort_list(list)

# Vérifiez si la liste triée est correcte.
assert sorted_result == [1, 2, 5, 5, 9], "Le tri a échoué"

print("Le test a réussi ! La liste triée est :", sorted_result)