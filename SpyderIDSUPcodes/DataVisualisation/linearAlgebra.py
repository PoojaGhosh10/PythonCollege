# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:56:42 2024

@author: lenovo
"""

#Linear Algebra

#vector: list containing elements i.e List[float]
from typing import List
Vector= List[float]

#vector addition
def add_vec(v:Vector, w:Vector)-> List[float]:
    #assert to check if both have the same length or not to further proceed
    assert len(v)==len(w),"Enter both vectors of same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]


assert add_vec([1,2,3], [1,2,3])==[2,4,6]
print(add_vec([1,2,3], [1,2,3]))


#vector subtraction
def sub_vec(v:Vector, w:Vector)-> List[float]:
    assert len(v)==len(w),"Enter both vectors of same length"
    return [v_i - w_i for v_i, w_i in zip(v,w)]

assert sub_vec([1,2,3], [1,2,3])==[0,0,0]
print(sub_vec([1,2,3], [1,2,3]))


#vector scalar multiplication
def scal_mul(v:Vector, c:int)->List[float]:
    assert v,"Enter the vector with certain length"
    return [c*v_i for v_i in v]


assert scal_mul([1,2,3],2)==[2,4,6]
print(scal_mul([1,2,3],2))


#vector dot product
def multiply(v:Vector, w:Vector)->List[float]:
    assert len(v)==len(w),"Enter both vectors of same length"
    return [v_i * w_i for v_i, w_i in zip(v,w)]

def dot_product(v:Vector, w:Vector)->float:
    assert len(v)==len(w),"Enter both vectors of same length"
    return sum(multiply(v, w))#can even directly write multiply in this

assert dot_product([1, 2, 3], [4, 5, 6]) == 32
print(dot_product([1,2,3],[1,2,3]))

#vector sum where a more than 2 vectors are added
#later


#sum of squares
def sum_of_squares(v:Vector)->float:
    assert v,"Empty Vector"
    return dot_product(v,v)

assert sum_of_squares([1, 2, 3]) == 14
print(sum_of_squares([1,2,3]))


#magnitude(length)
import math
def cal_magnitude(v:Vector)->float:
    assert v,"Empty Vector"
    return math.sqrt(sum_of_squares(v))

assert cal_magnitude([1, 2, 3]) == 3.7416573867739413
print(cal_magnitude([1,2,3]))


#squared distance
def sqrd_dist(v:Vector, w:Vector)-> float:
    assert len(v)==len(w),"Enter both vectors of same length"
    return math.sqrt(sum_of_squares(sub_vec(v, w)))
assert sqrd_dist([1,2,3], [4,5,6])==5.196152422706632
print(sqrd_dist([1,2,3], [4,5,6]))
    





    

