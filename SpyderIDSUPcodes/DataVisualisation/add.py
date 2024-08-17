# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:13:33 2024

@author: lenovo
"""

from typing import List
import math
Vector=List[float]

def vector_add(v:Vector, w:Vector)-> Vector:
    assert len(v)==len(w), 'Unequal length of vectors'
    
    return [v_i + w_i for v_i, w_i in zip(v,w)]

assert vector_add([1,2,3],[4,5,6])==[5,7,9]
print(vector_add([1,2,3],[4,5,6]))

def vector_sub(v:Vector, w:Vector)->Vector:
    assert len(v)==len(w), "Unequal length"
    
    return [v_i-w_i for v_i, w_i in zip(v,w)]

print(vector_sub([1,2,3],[4,5,6]))

def scalar_multiply(n:int, v:Vector)-> Vector:
    return [v_i * n for v_i in v]

print(scalar_multiply(2,[1,2,3]))


def vector_add2(v:List[Vector])->Vector:
    assert len(v)
    vec_len=len(v[0])
    assert all(len(v_i)==vec_len for v_i in v)
    
    
    return [sum(v_i[j] for v_i in v) for j in range(vec_len)]

assert vector_add2([[1,2,3],[4,5,6]])==[5,7,9]
print(vector_add2([[1,2,3],[4,5,6]]))


def dot(v:Vector, w:Vector)->float:
    assert len(v)==len(w)
    
    return sum(v_i*w_i for v_i, w_i in zip(v,w))

print(dot([1,2,3],[1,2,3]))


def sum_of_squares(v:Vector)-> float:
    return dot(v,v)

print(sum_of_squares([1,2,3]))

def magnitude(v:Vector)->float:
    return math.sqrt(sum_of_squares(v))

print(magnitude([1,2,3]))

def distance_bw(v:Vector, w:Vector)->float:
    return magnitude(vector_sub(v,w))
print(distance_bw([1,2,3], [4,5,6]))

from typing import Callable, Tuple
#Matrices
Matrix=List[Vector]

def getRow(i:int, A:Matrix)->Vector:
    return(A[i])

def getCol(j:int , A: Matrix)->Vector:
    return [A_i[j] for A_i in A]

def make_matrix(f:Callable[[int, int], float],row:int, col:int)->Matrix:
    return [[f(i,j)for j in range(col)] for i in range(row)]

def iden_mat(row, col,f):
    return make_matrix(f, row, col)

def id01(row,col):
    return 1 if row==col else 0

print(iden_mat(4, 4, id01))

def get_shape(A:Matrix)-> Tuple[int, int]:
    num_row=len(A)
    num_col=len(A[0]) if A else 0
    
    return num_row, num_col

print(get_shape([[1,2,3],[4,5,6]]))