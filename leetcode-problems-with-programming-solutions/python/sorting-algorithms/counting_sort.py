"""
Counting sort => is a stable sorting algorithm, that counts the occurences of each items in an array
                and uses it to determine the position of each element

"""

def countingSort(arr):
    length = len(arr)
    count = [0] * length
    output = [0] * length

    #count the occurences of each item
    for i in range(length):
        count[arr[i]] += 1

    #add count to previous count
    for j in range(len(count)):
        count[j] += count[j - 1]

    #remove last count and position element based on count
    k = length - 1
    while k >= 0:
        output[count[arr[k]] - 1] = arr[k]
        count[arr[k]] -= 1
        k -= 1

     #add each output element into array 
    for item in range(0, length):
        arr[item] = output[item]

    return arr

arr = [1, 4, 6, 7, 2, 4, 1, 3, 2, 3]
print("Counting Sort => ", countingSort(arr))
