"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    * arr.length >= 3
    * There exists some i with 0 < i < arr.length - 1 such that:
         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""


# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass
    
    def validMountainArray(arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        if len(arr) < 3 or arr[0] >= arr[1]: return False

        inc = True
        for i in range(1, len(arr)):
            #if curent element is equals to previous element
            if arr[i] == arr[i-1]:
                return False
            #if current element is greater than previous element
            elif inc == (arr[i] > arr[i-1]):
                continue
            elif not inc:
                return False
            else:
                inc = False

        return not inc

#test with any array input
arr = [3,5,5]

print(Solution.validMountainArray(arr))

#Output => False |Bcs this list is not in an increasing order|

 