"""
Merge Sort => This is a divide and conquer algorithm that recursively breaks an array into subarrays
              until each sub array is simple enough to swap and then merge the sub-arrays..
              -if any left sub-array element is less than any right sub-array element
                  -then insert the left sub-array element into merged array
              -else if any left sub-array element is greater than any right sub-array element
                   -then insert the right sub-array element into merged array
"""


def mergeSort(arr):
    #get the middle element
    mid = len(arr) // 2;

    if len(arr) > 1:
        left_array = arr[:mid] #split left array from beginning to middle of array
        right_array = arr[mid:] #split right array from middle to end of array

        #recursively sort eavh sub-array
        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0 #i points to left array, j points to right array, k points to merged array

        while i < len(left_array) and j < len(right_array):
            #if any left sub-array element is less than any right sub-array element
            if left_array[i] < right_array[j]:
                #then insert the left sub-array element into merged array
                arr[k] = left_array[i]
                i += 1
           #else if any left sub-array element is greater than any right sub-array element
            else:
                # -then insert the right sub-array element into merged array
                arr[k] = right_array[j]
                j += 1
            k += 1

        #add the remaining element in left_array to merged element
        while i < len(left_array):
            arr[k] =  left_array[i]
            i += 1
            k += 1

        #add the remaining element in right_array to merged element
        while j < len(right_array):
            arr[k] =  right_array[j]
            j += 1
            k += 1
    return arr

    

arr = [2, 8, 6, 5, 1, 3, 4, 9]

print("Merge Sort => ", mergeSort(arr))