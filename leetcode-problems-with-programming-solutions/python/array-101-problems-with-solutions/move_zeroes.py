"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

# Time Complexity: O(n)
class Solution(object):
    def __init__(self):
        pass

    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #check for edges cases, if the length of list is only one the return the arr
        if len(nums) == 0:
            return "Empty List, Please add values into list"
        
        # the front will be position 0
        front = 0
        
        
        for i in range(len(nums)):
            #if the current element is not zero
            if nums[i] != 0:
                # swap!
                nums[front], nums[i] = nums[i], nums[front]
                front += 1

        """
         slower, bcs it does two operations on a single iteration , 
         remove and add the zero to the end of the list 
         it iterates thru the list again and finds any 0, removes and add it to end of list
         it does this for every zero, which is kinda tedious
        
        """
        
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.remove(0)
        #         nums.append(0)
                
        return nums

nums = [0,1,0,3,12]

print(Solution.moveZeroes(nums))

#Output => [1, 3, 12, 0, 0]

                