"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
"""

# Time Complexity: O(nlog(n)
class Solution(object):
    def __init__(self):
        pass

    def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        First, we convert the list to a set to remove all the duplicate numbers.
        Then, we sort the set in descending order.
        
        """
        new_list = sorted(set(nums), reverse=True)
        
        #Next, we find the maximum number in list
        maximum = max(new_list)
        
        #if thelength of list is less than 3, just return the maximum number
        if len(new_list) < 3:
            return maximum
        else:
            #else return the third maximum number from a list with no duplicates
            third_max = new_list[2]
            return third_max

#test with any array input      
nums = [2,2,3,1]

print(Solution.thirdMax(nums))

#Output => 1 |bcs 1is the third largest number in the list|