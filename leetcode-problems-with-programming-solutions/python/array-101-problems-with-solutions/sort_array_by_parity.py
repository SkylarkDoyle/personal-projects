"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""


# Time Complexity: O(n)
class Solution(object):
    def __init__(self):
        pass
    
    def sortArrayByParity(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        temp_arr = []
        beg = 0
        if len(nums) == 0:
            return "Empty List, Please add values into list"
        
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
#                #insert to beginning of list
                temp_arr.insert(beg, nums[i])
                beg += 1
            else:
                #if odd number, add to end of list
                temp_arr.append(nums[i])
                
        return temp_arr


nums = [3,1,2,4]

print(Solution.sortArrayByParity(nums))

#Output => [2, 4, 3, 1]
