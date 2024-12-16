"""
Bubble Sort => This sorting algorithm works by iterating over an array and comparing the left and right elements
   -if left element is greater than right element, 
   -then swap the elements
"""

#here is the code

# Time Complexity: O(n^2)
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

    

arr = [2, 8, 6, 5, 1, 3, 4, 9]

print("Bubble Sort => ", bubbleSort(arr))