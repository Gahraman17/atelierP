def position(lst, elt):
    for i in range(len(lst)):
        if lst[i] == elt:
            return i
    return -1

# Fonction position avec boucle while :
def position_while(lst, elt):
    i = 0
    while i < len(lst):
        if lst[i] == elt:
            return i
        i += 1
    return -1

def nb_occurrences(lst, e):
    count = 0
    for element in lst:
        if element == e:
            count += 1
    return count

def est_triee(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Fonction est_triee avec boucle while :
def est_triee_while(lst):
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False
        i += 1
    return True

def position_tri(lst, e):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == e:
            return mid
        elif lst[mid] < e:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def a_repetitions(lst):
    seen = []
    i = 0
    while i < len(lst):
        if lst[i] in seen:
            return True
        seen.append(lst[i])
        i += 1
    return False

def test_functions():
    # Test de la fonction position
    lst1 = [1, 2, 3, 4, 5]
    elt1 = 3
    print(f"Position de {elt1} dans {lst1}: {position(lst1, elt1)}")  # Doit renvoyer 2

    lst2 = [10, 20, 30, 40, 50]
    elt2 = 25
    print(f"Position de {elt2} dans {lst2}: {position(lst2, elt2)}")  # Doit renvoyer -1

    # Test de la fonction nb_occurrences
    lst3 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    elt3 = 3
    print(f"Occurrences de {elt3} dans {lst3}: {nb_occurrences(lst3, elt3)}")  # Doit renvoyer 3

    # Test de la fonction est_triee
    lst4 = [1, 2, 3, 4, 5]
    print(f"Est triée? {lst4}: {est_triee(lst4)}")  # Doit renvoyer True

    lst5 = [5, 4, 3, 2, 1]
    print(f"Est triée? {lst5}: {est_triee(lst5)}")  # Doit renvoyer False

    # Test de la fonction position_tri
    lst6 = [1, 2, 3, 4, 5]
    elt6 = 3
    print(f"Position de {elt6} dans {lst6}: {position_tri(lst6, elt6)}")  # Doit renvoyer 2

    # Test de la fonction a_repetitions
    lst7 = [1, 2, 3, 4, 5]
    print(f"A des répétitions? {lst7}: {a_repetitions(lst7)}")  # Doit renvoyer False

    lst8 = [1, 2, 2, 3, 3, 4]
    print(f"A des répétitions? {lst8}: {a_repetitions(lst8)}")  # Doit renvoyer True

test_functions()
