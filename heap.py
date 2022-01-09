# Heapify is the process of creating a heap DS from an array
# left child of node is 2*i+1
# right child of node is 2*i+2
# heap is used in priority queue
# max-heap data structure
# code mostly taken from programiz website!
#TODO use oop to store values and organize code!

def heapify(arr, size, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < size and arr[i] < arr[l]:
        largest = l

    if r < size and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def insert(array, value):
    size = len(array)-1
    if size == 0:
        array.append(value)
    else:
        array.append(value)
        for i in range(size//2, -1, -1):
            heapify(array, size+1, i)

def delete_node(array, value):
    size = len(array)
    i = 0
    for i in range(0, size):
        if array[i] == value:
            break
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(value)
    size = len(array)-1

    for i in range(size//2,-1,-1):
        heapify(array, len(array), i)



