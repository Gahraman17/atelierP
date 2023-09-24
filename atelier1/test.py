nombres = [1, 3, -3, 4, -5, -1]

nombre_plus_proche_de_zero = None  # Initialisez la variable à None pour le moment
distance_minimale = float('inf')    # Initialisez la distance minimale à l'infini

for nombre in nombres:
    # Comparez directement la valeur absolue de nombre avec la distance minimale
    if nombre * nombre < distance_minimale * distance_minimale:
        distance_minimale = nombre  # Mettez à jour la distance minimale
        nombre_plus_proche_de_zero = nombre  # Mettez à jour le nombre le plus proche de zéro

print("Le nombre le plus proche de zéro est :", nombre_plus_proche_de_zero)
