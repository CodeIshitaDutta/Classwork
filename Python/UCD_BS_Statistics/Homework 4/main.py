import datetime
import  sys
sys.setrecursionlimit (20000)
"""Import the data"""
array = []
with open("num2.txt") as f:    
    for line in f:        
        array += [int(x) for x in line.split()]

#Record start time
start = datetime.datetime.now()
print("Start at", start)
#Run the sorting algorithm for 10 times
def bubbleSort(plist):    
    for i in range(len(plist)-1, 0, -1):        
        for j in range(i):            
            if plist[j] > plist[j+1]:                
                plist[j], plist[j+1] = plist[j+1], plist[j]
for i in range(10):    
    bubbleSort(array)
#Record end time
end = datetime.datetime.now()
print("End at", end)
elapsed = end - start
minute, second = divmod(elapsed.total_seconds(), 60)
print("Total runtime Bubble Sort:", minute, "minutes and", second, "seconds")


start = datetime.datetime.now()
print("Start at", start)
def  bubbleSortShort(plist):
    for i in  range(len(plist) -1, 0,  -1):
        exchanged = False
        for j in  range(i):
            if  plist[j] > plist[j+1]:
                plist[j], plist[j+1] = plist[j+1],  plist[j]
                exchanged = True
        if not  exchanged:
            break
for i in range(10):    
    bubbleSortShort(array)
end = datetime.datetime.now()
print("End at", end)
elapsed = end - start
minute, second = divmod(elapsed.total_seconds(), 60)
print("Total runtime Bubble Short:", minute, "minutes and", second, "seconds")


start = datetime.datetime.now()
print("Start at", start)
def  selectionSort(plist):
    for i in  range(len(plist) -1, 0,  -1):
        idx_of_max = 0
        for j in  range(1, i+1):
            if  plist[j] > plist[idx_of_max ]:
                idx_of_max = j
        temp = plist[i]
        plist[i] = plist[idx_of_max]
        plist[idx_of_max] = temp
for i in range(10):    
    selectionSort(array)
end = datetime.datetime.now()
print("End at", end)
elapsed = end - start
minute, second = divmod(elapsed.total_seconds(), 60)
print("Total runtime Selection Sort:", minute, "minutes and", second, "seconds")


start = datetime.datetime.now()
print("Start at", start)
def  insertionSort(plist):
    for i in  range(1, len(plist)):
        val = plist[i]
        j = i
        while j > 0 and  val < plist[j-1]:
            plist[j] = plist[j-1]
            j  -= 1
        plist[j] = val
for i in range(10):    
    insertionSort(array)
end = datetime.datetime.now()
print("End at", end)
elapsed = end - start
minute, second = divmod(elapsed.total_seconds(), 60)
print("Total runtime Insertion Sort:", minute, "minutes and", second, "seconds")


start = datetime.datetime.now()
print("Start at", start)
def  mergesort(plist):
    if len(plist)  <= 1:
        return  plist
    m = len(plist) // 2
    left = plist[:m]
    right = plist[m:]
    return  merge(mergesort(left), mergesort(right))

def  merge(left , right):
    if left == []:
        return  right
    if  right  == []:
        return  left
    

    if left [0]  <= right [0]:
        return [left [0]] + merge(left [1:],  right)
    else:
        return [right [0]] + merge(left , right [1:])


for i in range(10):    
    mergesort(array)
end = datetime.datetime.now()
print("End at", end)
elapsed = end - start
minute, second = divmod(elapsed.total_seconds(), 60)
print("Total runtime Merge Sort:", minute, "minutes and", second, "seconds")



start = datetime.datetime.now()
print("Start at", start)
def lt(plist , pivot):
    result = []
    for x in  plist:
        if x < pivot:
            result.append(x)
    return  result
def gt(plist , pivot):
    result = []
    for x in  plist:
        if x  >= pivot:
            result.append(x)
    return  result
def  quicksort(plist):
    if len(plist)  <= 1:
        return  plist
    else:
        pivot = plist [0]
        rest = plist [1:]
        return  quicksort(lt(rest , pivot)) + [pivot] +quicksort(gt(rest , pivot))
for i in range(10):    
    quicksort(array)
end = datetime.datetime.now()
print("End at", end)
elapsed = end - start
minute, second = divmod(elapsed.total_seconds(), 60)
print("Total runtime Quick Sort:", minute, "minutes and", second, "seconds")