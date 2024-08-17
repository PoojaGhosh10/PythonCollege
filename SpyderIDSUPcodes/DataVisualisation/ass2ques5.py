# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:26:06 2024

@author: lenovo
"""

import matplotlib.pyplot as plt
from collections import Counter
import random
random_int= [random.randint(0, 100) for _ in range(100)]
counter_num = Counter(min(random_ints // 10 * 10, 90) for random_ints in random_int)
plt.bar(counter_num.keys(), counter_num.values(),width=10, edgecolor='black', color='green')

plt.xticks(20*i for i in range(6))
plt.xlabel("Integers")
plt.ylabel("Frequency")
plt.title("labelf")
plt.show()