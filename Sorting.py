#implement a bubble sort

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


#implement a selection sort
def selectionSort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

#implement a insertion sort
def insertionSort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst

#Implement a merge sort
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return (left + right)

#Implement a quick sort
def quickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = []
    right = []
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return quickSort(left) + [pivot] + quickSort(right)


l = [3, 9, 1, 2, 4, 5, 8, 7, 6]
print(bubbleSort(l))
print(selectionSort(l))
print(insertionSort(l))
print(mergeSort(l))
print(quickSort(l))



    

