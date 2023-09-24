import matplotlib.pyplot as plt
import time
from random import shuffle
from ex2 import mix_list

def perf_mix(mix_list_callable, shuffle_callable, list_sizes, num_executions):
    execution_times_mix = []
    execution_times_shuffle = []

    for size in list_sizes:
        mix_times = []
        shuffle_times = []

        for _ in range(num_executions):
            # Créer une liste de taille 'size'
            my_list = list(range(size))

            # Mesurer le temps d'exécution pour mix_list
            start_time = time.perf_counter()
            mix_list_callable(my_list)
            end_time = time.perf_counter()
            mix_times.append(end_time - start_time)

            # Mesurer le temps d'exécution pour shuffle
            start_time = time.perf_counter()
            shuffle_callable(my_list)
            end_time = time.perf_counter()
            shuffle_times.append(end_time - start_time)

        # Calculer la moyenne des temps d'exécution
        avg_mix_time = sum(mix_times) / num_executions
        avg_shuffle_time = sum(shuffle_times) / num_executions

        execution_times_mix.append(avg_mix_time)
        execution_times_shuffle.append(avg_shuffle_time)

    return execution_times_mix, execution_times_shuffle

list_sizes = [10, 100, 1000]
num_executions = 10

mix_times, shuffle_times = perf_mix(mix_list, shuffle, list_sizes, num_executions)

# Créer le graphe
plt.plot(list_sizes, mix_times, label='mix_list')
plt.plot(list_sizes, shuffle_times, label='shuffle')
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.title('Temps d\'exécution en fonction de la taille de la liste')
plt.show()
