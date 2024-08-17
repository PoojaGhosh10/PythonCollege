#Ass7
'''#Ques1:
def remDup(lists1):
    lists2=[]
    for list in lists1:
        if list not in lists2:
            lists2.append(list)
    return lists2

lists1=eval(input("Enter the input in comma-seperated form:"))
lists2= remDup(lists1)
print("The lists obtained is :",lists2)


#Ques2
def sum_of_elements(lists1, size):
    lists2=[]
    for i in range(0, size):
        sum=0
        for j in range(0, i+1):
            sum+=j
        lists2.append(sum)    
    return lists2


lists1= eval(input("Enter the lists in the comma seperated form:"))
lists2= sum_of_elements(lists1, len(lists1))
print("The sum of the elemnts obtained is :",lists2)


#Ques3
def count_freq(sen1):
    sen= sen1.lower()
    countFreq={}
    if sen!='':
        for letter in sen:
            if letter not in countFreq.keys() and letter != ' ':
                countFreq[letter]=1
        else:
                countFreq[letter]+=1
    return countFreq            


sen=input("Enter a sentence:")
countFreq=count_freq(sen)
print("The dictionary of each letter with no.of times it occured: ", countFreq)

#QUES4 ,1:           2:
l1=0,1,2,3,4          l1=3,1, 5, 3, 7
l2=3,4,5,6,7          l2=0,4,2, 6, 4

#QUES 5  1:30   2: 16    3 :omputerc  4: 219 
5:
x=[1,2,4,6,9,10,14,15,17]
for i in range(0, len(x)):
    if x[i]%2==0:
        x[i]= 4*i
    elif x[i]%3==0:
        x[i]= 9*i
    else:
        x[i]*=2
print(x) 
Output: [2, 4, 8, 12, 36, 20, 24, 63, 34]     

#Ques 6
def main():
    n= int(input("Enter the number of lists to be created in a list: "))
    listF= listoflists(n)
    print("The list of lists obtained is:", listF)

def listoflists(n):
    list1=[]
    for i in range(1, n+1):
        list2=[]
        for j in range(1, 6):
            list2.append(j*i)
        list1.append(list2)    
    return list1

main()

#Ques7

def numtoletter(num):
    while(num>0):
        num

        dictL={1:"one",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6:"six",
           7:"seven",
           8:"eight",
           9:"nine"}
        str=''
        for s in num:
            if s in dictL:
                str+=dictL[s]
    return str 
           

num=int(input("Enter a number to be converted intop words: "))
word= numtoletter(num)
print("The word is",word)
'''