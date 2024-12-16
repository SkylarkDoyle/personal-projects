def counting_sort(arr, place):
    length = len(arr)
    count = [0] * length
    output = [0] * length


 #get the count of occurences
    for i in range(length):
        index = arr[i] // place
        count[index % 10] += 1


 #get cumulative sum of count
    for j in range(len(count)):
        #add previous count to next count
        count[j] += count[j - 1]

  #position the element based on count
    for k in range(length-1, -1, -1):
        index = arr[k] // place
        output[count[index % 10] - 1] = arr[k]
        count[index % 10] -= 1

  #insert the output elements into item
    for item in range(length):
        arr[item] = output[item]

    # Main function to implement radix sort
def radixSort(arr):
    # Get maximum element
    max_element = max(arr)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10

    return arr
    

arr = [1, 4, 6, 7, 2, 4, 1, 3, 2, 3]
print("Radix Sort => ", radixSort(arr))
