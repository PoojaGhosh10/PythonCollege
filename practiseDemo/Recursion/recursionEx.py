'''#RECURSION EXAMPLES:

#Recursion on numbers:

#ex1: print factorial of a number n.
def printFactorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*printFactorial(num-1)

num= int(input("Enter the number: "))
fact= printFactorial(num)
print("The factorial of a number :" , fact) 


#ex2: sum of the first n natural numbers.
def sumofNnum(num):
    if num==1:
        return 1
    else: 
        return num+sumofNnum(num-1)
    
num= int(input("Enter the number: "))
sum= sumofNnum(num)
print("The sum of n natural number :" , sum)

#ex3: reverse a number.
def revNum(num, rev):
    revN=0
    digit=0
    if num==0:
         return rev 
    else:
         return revNum(num//10, rev*10 + num%10) 
  
num= int(input("Enter the number: "))
rev=0
print("The reverse of a number is :" , revNum(num, rev))


#ex4: gcd of two numbers.
#for calculating gcd a>b(dividend, divisor )to divide, if not then convert

def gcdNum(dividend, divisor):
    if(divisor==0):
        return dividend    
    else:
        return gcdNum(divisor, dividend%divisor)
        

dividend=int(input("Enter the dividend: "))
divisor=int(input("Enter the divisor: "))
if(divisor>dividend):
        print("Performing swapping.")
        temp= dividend
        dividend= divisor
        divisor=temp
print("The gcd of two number is :", gcdNum(dividend, divisor))




#ex5: Recursion for finding nth fibonacci number (starting from 1 to n) 
def fib(num):
    if num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fib(num-1)+fib(num-2)
    
num=int(input("Enter the number:"))
print("The nth fibonacci number is:" , fib(num))

#Recursion on strings:

#ex1: Reverse a string.


def revStr(sen):
    if sen=="":
        return sen
    else:
        return revStr(sen[1:]) + sen[0]
    
sen=input("Enter the string:")
print("Reversed string: ", revStr(sen))

#2nd method
def revStr(sen):
    if sen=="":
        return sen
    else:
        return sen[-1]+ revStr(sen[:-1])  
    
sen=input("Enter the string:")
print("Reversed string: ", revStr(sen))


#ex2: recursion to find the length of the string.

def findLen(sen):
    if sen=='':
        return 0
    else:
        return 1+ findLen(sen[1:])
    

sen=input("Enter the string:")
print("Length of the string: ", findLen(sen))

#ex4: to check palindrome or not

def isPalindrome(sen):
    if sen=='':
        return True
    else:
        return (sen[0]==sen[-1] and isPalindrome(sen[1:-1]))
    

sen=input("Enter the string:")
print("Length of the string: ", isPalindrome(sen))
'''
