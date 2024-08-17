
print('''
Hello World!
Hello Again
I like typing this.
This is fun.
Yay! Printing.
I'd much rather you 'not'.
I "said" do not touch this.
''')


'''
#ques 2 of 9:of string to reverse without reversing the word
def funcRev(str1):
    str2=''
    list=[]
    for char in str1:
        if not char.isspace():
            str2+=char
        else:
            str2+=" "
            list.append(str2)
            str2=''
    return list
    
def revString(list):
    revWord=''
    for word in range(len(list)-1, -1, -1):
        revWord+=list[word]
    return revWord    
    
str1=input("Enter the string: ")
list1= funcRev(str1+' ')
revStr=revString(list1)
print(revStr)


#ques 5 of 9:
def delIndex(str1, ind):
    revStr=""
    for i in range(len(str1)):
        if ind==i:
            continue
        else:
            revStr+=str1[i]
    return revStr
    
    
str1=input("Enter the string: ")
retStr= delIndex(str1, 5)
print(retStr)



#check and count vowel and consonant:

def checkVowel(str1):
    string1= "aeiou"
    count1,count2=0,0
    for char in str1:
        if char in string1:
            count1+=1
        else:
            count2+=1
    return count1,count2
    
    
str1="gdhbweboslwaa"
count1,count2=checkVowel(str1)
print(count1,count2)


remove duplicate:
def removeDup(str1):
    list=[]
    for char in str1:
        if char not in list:
            list.append(char)
            
    return ''.join(list)
    
str1="ygsquygshiysg"    
str2=removeDup(str1)
print(str2)


#countfreq of a string
def countfreq(str1):
    dict={}
    for char in str1:
        if char not in dict.keys():
            dict[char]=1
        else:
            dict[char]+=1
    return dict 
    
str1=" hdwhdwhdwhdw"   
dict1=countfreq(str1)
print(dict1)


def countfreq(str1):
    dict={}
    for char in str1:
        if char not in dict.keys():
            dict[char]=1
        else:
            dict[char]+=1
    return dict 



    #to find maximum freq   
def maxFreq(dict):
    max1=dict[0]
    for i in dict.keys():
        if max1<dict.values(i):
            max1= dict[i]
    return max1    
    
str1=" hdwhdwhdwhdw"   
dict1=countfreq(str1)
max= maxFreq(dict1)
print(max)
            
'''
