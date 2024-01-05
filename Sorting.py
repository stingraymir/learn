#implement a BUBBLE SORT

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


#implement a SELECTION SORT
def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

#implement a INSERTION SORT
def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
            j -= 1
    return list

#Implement a MERGE SORT
def mergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return (left + right)

#Implement a QUICK SORT
def quickSort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for i in range(1, len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])
    return quickSort(left) + [pivot] + quickSort(right)


l = [3, 9, 1, 2, 4, 5, 8, 7, 6, 0]
print(bubbleSort(l))
print(selectionSort(l))
print(insertionSort(l))
print(mergeSort(l))
print(quickSort(l))


    

