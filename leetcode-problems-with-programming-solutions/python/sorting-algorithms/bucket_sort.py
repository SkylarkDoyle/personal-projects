def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


def bucketSort(arr):
    buckets = []
    slot_nums = 10


    for i in range(slot_nums):
        buckets.append([])

    #put the element into different buckets
    for j in arr:
        bucket_idx = int(slot_nums * j)
        buckets[bucket_idx].append(j)

    #sort each bucket using insertion sort
    for bucket in range(slot_nums):
        buckets[bucket] = insertion_sort(buckets[bucket])

    #concatenate the result
    k = 0
    for i in range(slot_nums):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr




arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 
print("Bucket Sort => ", bucketSort(arr))

