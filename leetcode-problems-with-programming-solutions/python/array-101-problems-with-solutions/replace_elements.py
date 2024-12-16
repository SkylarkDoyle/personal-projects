"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 
"""

# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass

    def replaceElements(arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        r = len(arr) - 1
        max_next_element =  -1
        
        """
         how to decrement in a for loop
        """
        
        for i in range(r, -1, -1):
            current = arr[i]
            
            #change value of current element to the next greatest element to the right
            arr[i] = max_next_element
            
            #check the max element btw current and next greatest element to the right
            max_next_element = max(current, max_next_element)
            
        return arr


arr = [17,18,5,4,6,1]

print(Solution.replaceElements(arr))

#Output => [18, 6, 6, 6, 1, -1]

            
        
        