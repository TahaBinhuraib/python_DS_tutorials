# A recursive algorithm, that aims to sort an array
# Its's a divide and conquer algorithm
"""
Algorithm merge_sort(l, h){
    if(l<h){
        mid = (l+h)/2
        merge_sort(l,mid)
        merge_sort(mid+1, h)
        merge(l, mid, h)
}
}
O(nlogn);
"""

"""
Pros:
    1. Large lists
    2. LinkedList
    3. External Sorting
    4. Preserves order of dublicates
Cons:
    1. Extra space not an inplace sort algorithm
    2. Becomes fast only when n>=15
    3. Recursive
    4. Takes O(n+logn) space

"""
class mergeSort:
    
    def __init__(self, array):

        self.array = array
        self.sorted = []

    def merge_sort(self)->list[int]:
        sorted = self.sort(self.array)
        self.sorted = sorted

    def sort(self, arr)->list[int]:

        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.sort(L)
            self.sort(R)
  
            i = j = k = 0
    
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def __str__(self):
        return str(self.array)




def main():
    unsorted_list = [4,2,56,12,41,60,1]
    sort_list = mergeSort(unsorted_list)
    sort_list.merge_sort()
    print(sort_list)

if __name__ == "__main__":
    main()