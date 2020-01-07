# -*- coding: utf-8 -*-
"""
Created on Fri Dec  29 13:35:20 2019

@author: somex.gupta
"""
import pandas as pd

# input
input_string="Machine learning will automate jobs that most people thought could only be done by people. ~Dave Waters."


# ------------------------  method 1 : using pandas buildin function value_count --------
input_series=pd.Series(list(input_string))
val=input_series.value_counts()
duplicate_values = val[val>1] # series of value
print("----------------\nMethod 1 : \n",duplicate_values)


# ------------------------  method 2 : using counter from collections library ------------
from collections import Counter
val = Counter(input_string) # counter object of key value pair
duplicate_values=[]
for x,y in val.items(): # iterate over the items
    if y>1:
        duplicate_values.append((x,y))
print("----------------\nMethod 2 : \n",duplicate_values) # list of tuples


# ------------------------ method 3: without using buildin funtion ------------------------ 
dic_value={}
for x in input_string:
    if x in dic_value.keys():
        dic_value[x]=dic_value.get(x)+1
    else:
        dic_value[x]=+1

duplicate_values=[]
for x,y in dic_value.items():
    if y>1:
        duplicate_values.append((x,y))
print("----------------\nMethod 3 : \n",duplicate_values) # list of tuples


# ---------------------------- output ----------------------------------------------------

# =============================================================================
#----------------
# Method 1 : 
#       16
# e    11
# o     9
# t     8
# a     7
# l     7
# n     5
# h     4
# p     4
# u     3
# b     3
# i     3
# s     3
# c     2
# g     2
# r     2
# m     2
# .     2
# d     2
# y     2
# dtype: int64
# ----------------
# Method 2 : 
#  [('a', 7), ('c', 2), ('h', 4), ('i', 3), ('n', 5), ('e', 11), (' ', 16), ('l', 7), ('r', 2), ('g', 2), ('u', 3), ('t', 8), ('o', 9), ('m', 2), ('b', 3), ('s', 3), ('p', 4), ('d', 2), ('y', 2), ('.', 2)]
# ----------------
# Method 3 : 
#  [('a', 7), ('c', 2), ('h', 4), ('i', 3), ('n', 5), ('e', 11), (' ', 16), ('l', 7), ('r', 2), ('g', 2), ('u', 3), ('t', 8), ('o', 9), ('m', 2), ('b', 3), ('s', 3), ('p', 4), ('d', 2), ('y', 2), ('.', 2)]
# =============================================================================
