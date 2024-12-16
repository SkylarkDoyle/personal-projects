"""
Selection Sort => This is an in-place comparison algorithm, that sets the first element as minimum
                  then compare with other elements in the array
                  -if current_minimum is greater than element
                  -then swap them
"""


# Time Complexity: O(n^2)
def selectionSort(arr):
    #loops from 0, to second last element
    for i in range(0, len(arr) - 1):
        #set first element as current minimum
        current_min = i
        #loops from element i + 1 to end of array
        for j in range(i + 1, len(arr)):
            #if any element to the right is less than current minimum
            if arr[j] < arr[current_min]:
                #then set the right element as new current minimum
                current_min = j
        #swap the new current minimum with previous current minimum
        arr[current_min], arr[i] = arr[i], arr[current_min]

    return arr


arr = [2, 8, 6, 5, 1, 3, 4, 9]

print("Selection Sort => ", selectionSort(arr))