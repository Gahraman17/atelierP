def separer(L):
    LSEP = []  

    # Ajout des nombres négatifs à gauche de LSEP
    for num in L:
        if num < 0:
            LSEP.insert(0, num)

    # Ajout des zéros au milieu de LSEP
    for num in L:
        if num == 0:
            LSEP.append(num)

    # Ajout des nombres positifs à droite de LSEP
    for num in L:
        if num > 0:
            LSEP.append(num)

    return LSEP

# Exemple d'utilisation :
L = [-2, 0, 5, -1, 0, 3, -4, 6]
LSEP = separer(L)
print(LSEP)
