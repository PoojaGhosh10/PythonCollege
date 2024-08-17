# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:03:15 2024

@author: lenovo
"""

#Statistics
from typing import List
Vector=List[float]

def mean(v:Vector)->float:
    return (sum(v)/len(v))
print(mean([1,2,3]))

def median(v:Vector)->float:
    return even(v) if len(v)%2==0 else odd(v)

def even(v)->float:
    mid_hi_pt=len(v)//2
    return (sorted(v)[mid_hi_pt]+sorted(v)[mid_hi_pt-1])/2

def odd(v)->float:
    return sorted(v)[len(v)//2]

print(median([1,2,3,4,5,6]))

from collections import Counter

def mode(v:Vector):
    count=Counter(v)
    max_val=max(count.values())
    return[(m,c) for m,c in count.items() if c==max_val]


print(mode([1,2,2,3,4,5,5,5,5]))  

def range(v:Vector)->float:
    return max(v)-min(v)

print(range([1,2,3,4,5,6]))

def quartile(p:float, v:Vector)->float:
    p_index=int(p*len(v))
    return sorted(v)[p_index]
print(quartile(0.2,[1,2,3,4,5,6,7]))


from add import sum_of_squares
def de_mean(v: Vector)-> List[float]:
    mean_bar= mean(v)
    return[v_i - mean_bar for v_i in v]
def variance(v:Vector)->float:
    assert len(v)>2, "variance requires atleast two elements"
    return sum_of_squares(de_mean(v))/(len(v)-1)

print(variance([1,2,3,4,5,6]))

import math
def std_deviation(v:Vector)-> float:
    return math.sqrt(variance(v))

print(std_deviation([1,2,3,4,5,6]))

from add import dot
def covariance(v: Vector, w: Vector)-> float:
    assert len(v)==len(w)
    return (dot(de_mean(v),de_mean(w)))/(len(v)-1)

print(covariance([1,2,3],[4,5,6]))

def correlation(v:Vector, w: Vector)->float:
    assert len(v)==len(w)
    std_dev_x=std_deviation(v)
    std_dev_y=std_deviation(w)
    if std_dev_x > 0 and std_dev_y > 0: 
        return covariance(v, w)/std_dev_x/std_dev_y
    else:
        return 0