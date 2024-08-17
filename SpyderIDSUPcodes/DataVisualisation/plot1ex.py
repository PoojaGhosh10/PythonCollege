# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:01:17 2024

@author: lenovo

creating a line plot using just plot method
"""

import matplotlib.pyplot as plt

"""years=[1950, 1960, 1970,1980,1990, 2000,2010]
nominal_gdp=[300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, nominal_gdp, color="green", marker="o",linestyle="solid")

plt.title("Nominal Gdp")
plt.xlabel("years")
plt.ylabel("Billions of $")

plt.show()"""

'''movies=["Qala", "Dhoom","Kick","Race", "Dunki"]
ratings=[4.5, 3, 4, 2, 3.5]

plt.bar(range(len(movies)), ratings)

plt.title("Movie Ratings")
plt.xticks(range(len(movies)), movies)
plt.ylabel("Ratings")
plt.xlabel("Movies")

plt.show()'''
'''
values_y=[2,3,4,5,2,3,4]
years=[2017,2018,2019,2020, 2021,2022,2023]

plt.bar(years,values_y, 0.9)
plt.axis([2016, 2024, 0, 10])

plt.xticks(years)
plt.ticklabel_format(useOffset=False)
plt.xlabel("Years")
plt.ylabel("Y axis")
plt.title("bar chart")
plt.show()'''


variance=[1,2,4,8,16,32,64,138,256]
bias_squared=[256, 128, 64, 32, 16, 8, 4,2, 1]

total_error= [x+y for x, y in zip(variance, bias_squared)]
xs=[i for i,_ in enumerate(variance)]

plt.plot(xs, variance, "g-", label="variance")
plt.plot(xs, bias_squared,"r-", label="bias^2")
plt.plot(xs, bias_squared,"b:", label="total_error")

plt.legend()
plt.xlabel("model complexity")
plt.ylabel("range")
plt.xticks([])
plt.title("The bias-Variance Tradeoff")
plt.show()


