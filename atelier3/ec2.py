# 1. 
def mots_Nlettres(lst_mot, n):
    return [mot for mot in lst_mot if len(mot) == n]

# 2. 
def commence_par(mot, prefixe):
    return mot.startswith(prefixe)

# 3. 
def finit_par(mot, suffixe):
    return mot.endswith(suffixe)

# 4. 
def finissent_par(lst_mot, suffixe):
    return [mot for mot in lst_mot if mot.endswith(suffixe)]

# 5. 
def commencent_par(lst_mot, prefixe):
    return [mot for mot in lst_mot if mot.startswith(prefixe)]

# 6. 
def liste_mots(lst_mot, prefixe, suffixe, n):
    return [mot for mot in lst_mot if mot.startswith(prefixe) and mot.endswith(suffixe) and len(mot) == n]


