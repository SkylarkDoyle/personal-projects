"""
Tim Sort => is an hybrid sorting algorithm that is based on insertion and merge sort
                -if arr is less than min_run
                    -them use insertion sort only
"""


min_run = 32
def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
    """
    r = 0
    while n >= min_run:
        r |= n & 1
        n >>= 1
    return n + r
 


#create insertion sort first
def insertion_sort(arr, l, r):
    for i in range(l+1, r+1):
        j = i
        while j > l and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

# create merge sort to merge each block(run) of the array
def merge_sort(arr):
    mid = len(arr) // 2;

    if len(arr) > 1:
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=j=k=0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr



# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = len(arr) - 1
        insertion_sort(arr, start, end)
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = len(arr) // 2
            right = arr[min:]
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge_sort(arr)
 
        size = 2 * size

    return arr


arr = [1,6,5, 3, 7,4,3, 2,8 ,7]

print(timSort(arr))