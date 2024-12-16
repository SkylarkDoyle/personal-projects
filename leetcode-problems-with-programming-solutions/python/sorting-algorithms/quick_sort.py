"""
QuickSort => This is a sorting algorithm that recursively split an array into partition(divide and conquer algorithm),
              In each partition, there is a pivot(mainly last element), that is used in comparing 
              each element 
              - if element is less than pivot 
              - then swap with adjacent element
"""

def partition(arr,l, r):
    #make i pointer outside the array first
    i = l - 1
    #make last element the pivot
    pivot = arr[r]

    for j in range(l, r):
        #if j is less than pivot
        if arr[j] < pivot:
            #increment i by 1 => we assume the element i adjacent to j is greater
            i += 1
            #then swap i and j elements
            arr[i], arr[j] = arr[j], arr[i]
    #swap, middle element with pivot
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    #return the position of middle element[pivot], so we use it in the recursive function
    return i + 1


#this is the recursive function
def qs(arr, l, r):
    #base case => if the list is empty or has only one element
    if l >= r:
        return
    else:
        #store the returned partition value as split because, it splits the array recursively
        split = partition(arr, l, r)
        #now right element is the middle element - 1[pivot], this sort the element less than the pivot
        qs(arr, l, split-1)
        #now the left pointer is the middle element - 1[pivot], this sort the element greater than the pivot
        qs(arr, split+1, r)


#this function calls the recursive function and return the sorted array
# Time Complexity: O(n log n)
def quickSort(arr):
    qs(arr, 0, len(arr) - 1)
    return arr

arr = [2, 6, 5, 1, 3, 4, 8, 9]

print("Quick Sort => ", quickSort(arr))
    