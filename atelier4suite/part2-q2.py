import numpy as np
from numpy import *
index = []
def my_where(table : object, elm : integer )-> list:
    if not table:
        return 0
    elif elm <=table[0]:
        return 0
    else:
       index = my_where(table[1:],elm)
