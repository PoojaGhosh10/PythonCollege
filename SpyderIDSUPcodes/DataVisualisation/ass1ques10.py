# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:56:47 2024

@author: lenovo
"""


import matplotlib.pyplot as plt
from collections import Counter
male_age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]

counter_male = Counter(min(male_ages // 10 * 10, 90) for male_ages in male_age)
counter_female = Counter(min(female_ages // 10 * 10, 90) for female_ages in female_age)

plt.subplot(1, 2, 1)
plt.bar(counter_male.keys(), counter_male.values(), width=6, edgecolor="black")
plt.title('Male Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks([20*i for i in range(6)])

plt.subplot(1, 2, 2)
plt.bar(counter_female.keys(), counter_female.values(), width=6, edgecolor="black")
plt.title('Female Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks([20*i for i in range(6)])

plt.show()