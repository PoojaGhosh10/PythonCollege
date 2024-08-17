# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:36:17 2024

@author: lenovo
"""

#probability
def uniform_pdf(x:float)->float:
    return 1 if 0<=x<1 else 0

def uniform_cdf(x:float)-> float:
    if x<0: return 0
    elif x<1: return x
    else: return 1
    
    
print(uniform_pdf(0.2))  
print(uniform_cdf(0.2))   
import matplotlib.pyplot as plt
import math
math_sqrt_pi=math.sqrt(2*math.pi)
def normal_pdf(x:float, mu:float=0, sigma:float=1)->float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (math_sqrt_pi * sigma))

xs=[x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1)for x in xs],"r-", label="mu=0 sigma=1" )
plt.plot(xs, [normal_pdf(x, sigma=2)for x in xs],"g-.", label="mu=0 sigma=2" )
plt.plot(xs, [normal_pdf(x, sigma=0.5)for x in xs],"b:", label="mu=0 sigma=0.5" )
plt.plot(xs, [normal_pdf(x, mu=-1)for x in xs],"b-", label="mu=0 sigma=-1" )


def normal_cdf(x:float, mu:float=0, sigma:float=1)->float:
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2
    
    
    
xs=[x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1)for x in xs],"r-", label="mu=0 sigma=1" )
plt.plot(xs, [normal_cdf(x, sigma=2)for x in xs],"g-.", label="mu=0 sigma=2" )
plt.plot(xs, [normal_cdf(x, sigma=0.5)for x in xs],"b:", label="mu=0 sigma=0.5" )
plt.plot(xs, [normal_cdf(x, mu=-1)for x in xs],"b-", label="mu=0 sigma=-1" )


def inverse_normal_cdf(p:float, mu:float=0, sigma:float=1, tolerance=0.000001)->float:
    if mu!=0 and sigma!=1:
        return mu+sigma*inverse_normal_cdf(p, tolerance= tolerance)
    
    low_z=-10.0
    high_z=10.0
    while high_z-low_z>tolerance:
        mid_z= (low_z+high_z)/2
        mid_p=normal_cdf(mid_z)
        
        if mid_p<p:
            low_z= mid_z
        else:
            high_z=mid_z
            
    return mid_z        

import random
def bernoulli_trial(p:float)-> float:
    return 1 if random.random()< p else 0


def binomial(n:int, p:float)->float:
    return sum(bernoulli_trial(p) for _ in range(n))


def binomial_histogram(p:float, n:float, num_points:int)->None:
    
