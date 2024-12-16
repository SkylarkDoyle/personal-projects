
"""
Given an array arr of integers, check if there exist two indices i and j such that :

    * i != j
    * 0 <= i, j < arr.length
    * arr[i] == 2 * arr[j]
 """


# Time Complexity: O(n^2)
class Solution(object):
    def __init__(self) -> None:
        pass
    
    def checkIfExist(arr):
            """
            :type arr: List[int]
            :rtype: bool
            """
            
            for i in range(len(arr)):
                for j in range(len(arr)):
                    #if i is not equal to j AND position i is equal to 2 * position j
                    if i != j and arr[i] == 2*arr[j]:
                        return True
                return False
           

#test with any array input          
arr = [3,1,7,5]

print(Solution.checkIfExist(arr))

#Output => False  |bcs there is no even number existing in the list|