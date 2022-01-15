# Quick sort works on the idea that an element is sorted if all the elements on the left are smaller
# and all the elements of the right are greater
# It's a recursive algorithm
# time, space complexity = O(nlogn)
# Method: Partitioning

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1

def quick_sort(arr, low, high):

    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


data = [1,2,3,4,100,0]
print(f'Unsorted array:\n{data}')
size = len(data)

quick_sort(data, 0, size - 1)

print(f'Sorted array:\n{data}')


