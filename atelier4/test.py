import matplotlib.pyplot as plt
import time
from random import shuffle
from ex2 import mix_list

def perf_mix(mix_list, shuffle, list_sizes, num_executions):
    mix_moy = []
    shuffle_moy = []

    for size in list_sizes:
        mix_times = []
        shuffle_times = []

        for i in range(num_executions):
           
            my_list = list(range(size))

           
            start_time = time.perf_counter()
            mix_list(my_list)
            end_time = time.perf_counter()
            mix_times.append(end_time - start_time)

            
            start_time = time.perf_counter()
            shuffle(my_list)
            end_time = time.perf_counter()
            shuffle_times.append(end_time - start_time)

       
        avg_mix_time = sum(mix_times) / num_executions
        avg_shuffle_time = sum(shuffle_times) / num_executions

        mix_moy.append(avg_mix_time)
        shuffle_moy.append(avg_shuffle_time)

    return mix_moy, shuffle_moy

list_sizes = [5, 10]
num_executions = 1000

mix_times, shuffle_times = perf_mix(mix_list, shuffle, list_sizes, num_executions)


plt.plot(list_sizes, mix_times, label='mix_list')
plt.plot(list_sizes, shuffle_times, label='shuffle')
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.title("title")
plt.show()
