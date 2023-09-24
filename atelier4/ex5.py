from random import *
import matplotlib.pyplot as plt
import numpy as np
import time
from ex2 import mix_list

def perf_mix(mix_list : callable, shuffle:callable, list_sizes, num_executions)-> (int, int):
    moy_mix = []
    moy_shuffle = [] 
    for i in list_sizes:
         mix_times = []
         shuffle_times = []
         
         for j in range(num_executions):
              
             my_list = list(range(i))
             
             start_pc = time.perf_counter()
             mix_list(my_list)
             end_pc = time.perf_counter()
             mix_times.append(end_pc-start_pc)
             
             
             start_pc = time.perf_counter()
             shuffle(my_list)
             end_pc = time.perf_counter()
             shuffle_times.append(end_pc-start_pc)
             
    avg_mix_time = sum(mix_times) / num_executions
    avg_shuffle_time = sum(shuffle_times) / num_executions

    moy_mix.append(avg_mix_time)
    moy_shuffle.append(avg_shuffle_time)

    return moy_mix, moy_shuffle

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