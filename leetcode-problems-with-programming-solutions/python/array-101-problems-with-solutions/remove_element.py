# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""

# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass

    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i = 0 

        if len(nums) == 0:
            return "Empty List, Please add values into list"

        #this is kinda slow 
        #WHILE VALUE IS IN THE LIST
        # while val in nums:  
        #     #KEEP REMOVING THE VALUE UNTIL IT ISNT IN THE LIST
        #     nums.remove(val)



        #this is faster
        #while the increment is less than length of array - 1  
        while i <= len(nums) - 1:
            #while the current element == value
            while nums[i] == val:
                #set the current element to None
                nums[i] = None
            i += 1
                
        #check for None keywords
        while None in nums:
            #and remove them from the list
            nums.remove(None)

        return nums

        

#test with any array input
nums = [3,2,2,3]
val = 3

print(Solution.removeElement(nums, val))


#Output => [2, 2] 
