"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

"""

# Time Complexity: O(n)
class Solution(object):
    def __init__(self):
        pass

    def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #remove duplicates from list
        noDuplicatesList = set(nums)
        new_arr = []
        
        
        #first solution 
        #return [i for i in range(1, len(nums) + 1) if i not in s]
        
        #OR
        
        #loop throught array from second element 
        for i in range(1, len(nums) + 1):
            #if element not in the list with no duplicates
            if i not in noDuplicatesList:
                #add  to new list / array
                new_arr.append(i)
        return new_arr

#test with any array input
nums = [4,3,2,7,8,2,3,1]

print(Solution.findDisappearedNumbers(nums))

#Output => [5, 6] |5, 6 are the numbers not existing in the list|