'''def selection(list1):
    for i in range(0, len(list1)-1):
        min=i
        for j in range(i+1, len(list1)):
            if list1[j]<list1[min]:
                min=j
        if min!=i:        
            list1[min], list1[i] =list1[i],list1[min]

list1=[1,2,4,5,8,9,3]
selection(list1)
print("The list is :", list1)
'''
'''
def bubblesort(list1):
    for i in range(0, len(list1)-1):
        swap=False
        for j in range(0, len(list1)-i-1):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1]=list1[j+1],list1[j]
                swap= True
        if swap==False:
            break
list1=[1,2,4,5,8,9,3]
bubblesort(list1)
print("The list is :", list1)
''' 
'''
def insertionsort(list1):
    for i in range(0, len(list1)):
        key=list1[i]
        j=i-1
        while j>=0 and key<list1[j]:
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=key
list1=[1,2,4,5,8,9,3]
insertionsort(list1)
print("The list is :", list1)       
'''
'''
def mergeSort(arr, low, high):
    if low<high:
        mid=(low+(high-low))//2
        lst1=mergeSort(arr, low, mid)
        lst2=mergeSort(arr, mid+1, high)
        merge(lst1,lst2)



def merge(lst1,lst2):
    newList=[]
    while len(lst1)!=0 and len(lst2)!=0:
        if lst1[0]<lst2[0]:
            newList.append(lst1[0])
            lst1.remove(lst1[0])
        else:
            newList.append([lst1[0]])
            lst1.remove(lst1[0])
    if len(lst1)==0:
        newList+=lst1
    else:
        newList+=lst2
    return newList       
list1=[1,2,4,5,8,9,3]
mergeSort(list1, 0, len(list1)-1)
print("The list is :", list1) 
 '''   

