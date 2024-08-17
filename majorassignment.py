# -*- coding: utf-8 -*-
'''
Created on Sun Mar 31 09:24:51 2024
@author: lenovo
Name: Pooja Ghosh
Regd No: 2141007065
Branch:CSE
Section:'Z'-26
S.No:14

'''
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean, median, mode
from numpy import cov

students = [
    {"student id": 1, "Math": 50, "Computer Science": 60, "Science": 73},
    {"student id": 2, "Math": 40, "Computer Science": 50, "Science": 55},
    {"student id": 3, "Math": 90, "Computer Science": 70, "Science": 95},
    {"student id": 4, "Math": 80, "Computer Science": 62, "Science": 72},
    {"student id": 5, "Math": 80, "Computer Science": 90, "Science": 45},
    {"student id": 6, "Math": 84, "Computer Science": 90, "Science": 50},
    {"student id": 7, "Math": 90, "Computer Science": 95, "Science": 55},
    {"student id": 8, "Math": 89, "Computer Science": 93, "Science": 53},
    {"student id": 9, "Math": 88, "Computer Science": 92, "Science": 58},
    {"student id": 10, "Math": 90, "Computer Science": 95, "Science": 55},
    {"student id": 11, "Math": 70, "Computer Science": 65, "Science": 39},
    {"student id": 12, "Math": 65, "Computer Science": 60, "Science": 35},
    {"student id": 13, "Math": 60, "Computer Science": 55, "Science": 30},
    {"student id": 14, "Math": 55, "Computer Science": 57, "Science": 25},
    {"student id": 15, "Math": 49, "Computer Science": 54, "Science": 22},
    {"student id": 16, "Math": 10, "Computer Science": 30, "Science": 11},
    {"student id": 17, "Math": 50, "Computer Science": 40, "Science": 16},
    {"student id": 18, "Math": 90, "Computer Science": 45, "Science": 80},
    {"student id": 19, "Math": 70, "Computer Science": 50, "Science": 39},
    {"student id": 20, "Math": 70, "Computer Science": 80, "Science": 75}
]

#Question  1. Group student ids based on Science marks
science_marks = [student["Science"] for student in students]
less_equal_30 = [student["student id"] for student in students if student["Science"] <= 30]
between_30_and_70 = [student["student id"] for student in students if 30 < student["Science"] <= 70]
more_than_70 = [student["student id"] for student in students if student["Science"] > 70]


# Question 2. Create a line chart for student ids and Computer Science marks
student_ids = [student["student id"] for student in students]
computer_science_marks = [student["Computer Science"] for student in students]

plt.plot(student_ids, computer_science_marks, marker='o')
plt.xlabel('Student IDs')
plt.ylabel('Computer Science Marks')
plt.title('Computer Science Marks vs Student IDs')
plt.show()


#Question 3. Create vectors and find sum and average
vectors: List[List[int]] = [[student['Math'], student['Computer Science'], student['Science']] for student in students]
sum_of_vectors = np.sum(vectors, axis=0)
average_marks = [mean(mark) for mark in zip(*vectors)]

print("Sum of vectors:", sum_of_vectors)
print("Average marks:", average_marks)

#Question 4. Find mean, median, and mode of Computer Science marks
computer_science_marks = [student["Computer Science"] for student in students]
cs_mean = mean(computer_science_marks)
cs_median = median(computer_science_marks)
cs_mode = mode(computer_science_marks)

print("Mean of Computer Science marks:", cs_mean)
print("Median of Computer Science marks:", cs_median)
print("Mode of Computer Science marks:", cs_mode)

#Question 5. Find the covariance of Math and Science marks
math_marks = [student["Math"] for student in students]
science_marks = [student["Science"] for student in students]
covariance = cov(math_marks, science_marks)[0][1]

print("Covariance of Math and Science marks:", covariance)

#Question 6. Find the correlation between Computer Science and Math marks using type annotations
def correlation(cs_marks: List[int], math_marks: List[int]) -> float:
    return np.corrcoef(cs_marks, math_marks)[0, 1]

cs_math_correlation = correlation(computer_science_marks, math_marks)
print("Correlation between Computer Science and Math marks:", cs_math_correlation)
