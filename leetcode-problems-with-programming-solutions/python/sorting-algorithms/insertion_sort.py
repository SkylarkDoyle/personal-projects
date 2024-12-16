"""
Insertion sort => This is a sorting algorithm that divides an array into two groups,
                  sorted and unsorted groups
                  -then compare the groups, by comparing
                  -if the left element is greater than right element
                  -then swap
"""

# Time Complexity: O(n^2)
def insertionSort(arr):
    #in ten elements, loop through from range of 1 to 11, excluding 11
    for i in range(1, len(arr)):
        #set variable j = counter i
        j = i
        #if left element is greater than right element and j must not be less than 0, bcs we dont wanna decrement to negative indexes
        while arr[j-1] > arr[j] and j > 0:
            #swap if condition is TRUE
            arr[j-1], arr[j] = arr[j], arr[j-1]
            #decrement to check previous element and compare with next element
            #If condition is TRUE again, run the loop again, until condition is FALSE
            j -= 1

    return arr



arr = [2, 8, 6, 5, 1, 3, 4, 9]

print("Insertion Sort => ", insertionSort(arr))