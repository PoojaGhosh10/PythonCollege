'''
#ass8:
# ques1: take a string of numbers and convert it to type int.
def str_to_num(str):
    size=len(str)
    if size==0:
        return 0
    
    else:
        return str_to_num(str[:-1])*10 + (ord(str[-1])-48)

    
num= input("Enter the number:")
print("The number obtained is : ", str_to_num(num)) 

#ques2: take a string of numbers and find the sum of all digits.

def sum_of_num(str):
    size=len(str)
    if size==0:
        return 0
    
    else:
        return (ord(str[0])-48) + sum_of_num(str[1:])
    
num= input("Enter the number:")
print("The number obtained is : ", sum_of_num(num))   

#ques3: to print the power of a raise to b
def powerNum(a,b):
    if a==0:
        return 0
    elif b==0:
        return 1
    else:
        return a*powerNum(a, b-1)

num= int(input("Enter the number:"))
powB= int(input("Enter the number:"))
print("The number obtained is : ", powerNum(num, powB)) 

#Ques 4: Write a recursive function to calculate the harmonic sum of first n terms. Note: Theharmonic sum is the sum of reciprocals of the positive integers. For example, if n = 4, the output should be (1+1/2+1/3+1/4 ) = 2.0833

def harmonicSum(num):
    if num==1:
        return 1
    else:
        return 1/num + harmonicSum(num-1)
    
num= int(input("Enter the number: "))
print("The harmonic sum is: ", harmonicSum(num))  

#Ques 5: Write a recursive function to calculate the geometric sum of first n terms with constant ration r, where r lies in the interval (0,1). Note: In mathematics, a geometric series is a series with a constant ratio between successive terms. For example, if n = 4 and r = (1/2) then output should be (1+1/2+1/4+ 1/8 ) = 1.875


def geometricSum(num, r):
    if num==0:
        return 1
    else:
        return pow(r, num)+ geometricSum(num-1, r)
    

num1= int(input("Enter the number: "))
'''
'''#########def check_interval(r):
    assert 0 < r < 1, "r should be in the interval (0, 1)"
    # Rest of your code here

# Example usage
try:
    r_value = 0.5  # Replace this with your desired value for r
    check_interval(r_value)
    # Continue with your code if the assertion passes
except AssertionError as e:
    print(f"AssertionError: {e}")'''
'''
num2= float(input("Enter the number: "))
print("The geometric sum is: ", geometricSum(num1, num2))


#ques6: Write a recursive function to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x ≤ 0).For example, if n=6, then output should be 6+(6-2)+(6-4)+(6-6) = 12
def sum_series(n,x):
    if n ==x:
        return 0
    else:
        return n + sum_series(n - x, x+1) if n - 2 > 0 else n

# Example usage
n_value = 6
result = sum_series(n_value)
print(f"The sum of the series for n={n_value} is: {result}")


ques11:
def isSubset(i, n, lst2):
    if i== n:
        return lst2
    else:
        lst2.append(0)
        isSubset(i+1,n, lst2)
        lst2.append(1)
        isSubset(i+1,n, lst2)

n=4
lst2=[]
isSubset(0, 4, lst2)   

'''
