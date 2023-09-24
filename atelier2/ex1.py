# Fonction somme avec boucle for basée sur les indices
def somme_indices(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return total

# Fonction somme avec boucle for basée sur les éléments
def somme_elements(L):
    total = 0
    for element in L:
        total += element
    return total

# Fonction somme avec boucle while
def somme_while(L):
    total = 0
    i = 0
    while i < len(L):
        total += L[i]
        i += 1
    return total

# Fonction moyenne
def moyenne(L):
    if len(L) == 0:
        return 0
    return sum(L) / len(L)

# Fonction nb_sup avec boucle for basée sur les indices
def nb_sup_indices(L, e):
    count = 0
    for i in range(len(L)):
        if L[i] > e:
            count += 1
    return count

# Fonction nb_sup avec boucle for basée sur les éléments
def nb_sup_elements(L, e):
    count = 0
    for element in L:
        if element > e:
            count += 1
    return count

# Fonction moy_sup
def moy_sup(L, e):
    valeurs_sup = [x for x in L if x > e]
    if len(valeurs_sup) == 0:
        return 0
    return sum(valeurs_sup) / len(valeurs_sup)

# Fonction val_max
def val_max(L):
    if len(L) == 0:
        return None
    return max(L)

# Fonction ind_max
def ind_max(L):
    if len(L) == 0:
        return None
    max_val = max(L)
    return L.index(max_val)

# Fonction de test
def test_exercice1():
    print("TEST SOMME")
    # Test liste vide
    print("Test liste vide : ", somme_indices([]))
    
    # Test somme 11111
    lst2test1 = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 : ", somme_indices(lst2test1))

    # Test moyenne
    lst2test2 = [2, 4, 6, 8]
    print("Test moyenne : ", moyenne(lst2test2))

    # Test nb_sup avec boucle for basée sur les indices
    lst2test3 = [1, 2, 3, 4, 5, 6, 7]
    e = 3
    print(f"Test nb_sup_indices pour e={e} : ", nb_sup_indices(lst2test3, e))

    # Test nb_sup avec boucle for basée sur les éléments
    e = 3
    print(f"Test nb_sup_elements pour e={e} : ", nb_sup_elements(lst2test3, e))

    # Test moy_sup
    e = 3
    print(f"Test moy_sup pour e={e} : ", moy_sup(lst2test3, e))

    # Test val_max
    lst2test4 = [10, 5, 30, 8, 15]
    print("Test val_max : ", val_max(lst2test4))

    # Test ind_max
    print("Test ind_max : ", ind_max(lst2test4))

# Appeler la fonction de test
test_exercice1()
