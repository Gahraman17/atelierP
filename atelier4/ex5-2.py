from random import *
import time
from ex4 import extract_elements_list

def perf_mix(extract_elements_list : callable, sample:callable, list_sizes,int_nbr_of_element_to_extract )-> (int, int):
    tot_extract =0 
    tot_sample =0 
    for i in list_sizes:
         list=[i for i in range(i)]
    start_pc = time.perf_counter()
    extract_elements_list(list,int_nbr_of_element_to_extract)
    end_pc = time.perf_counter()
    tot_extract += end_pc-start_pc
    
    start_pc = time.perf_counter()
    sample(list,int_nbr_of_element_to_extract)
    end_pc = time.perf_counter()
    tot_sample += end_pc-start_pc
    return (tot_extract,tot_sample)

print(perf_mix(extract_elements_list,sample,[1,2,3,5,6,40],10)) 
    