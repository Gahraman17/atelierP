from operator import index
import numpy as np
from numpy import *

def my_searchsorted(table, elemt):
    if not table:
        return 0
    elif elemt <= table[0]:
        return 0
    else:
        index = my_searchsorted(table[1:], elemt)
        return index

table = [1, 2, 3, 5, 6, 6]
print("Index:", my_searchsorted(table, 6))
