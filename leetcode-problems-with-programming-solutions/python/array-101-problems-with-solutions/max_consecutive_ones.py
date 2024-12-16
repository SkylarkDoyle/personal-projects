# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass

    def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #initialize variables
        #the numbers at the right
        r_num = 1
        #max consecutive ones will be zero first because there is no consecutives ones yet..
        max_consecutive_ones, inc = 0, 0
        
        for i in nums:
                #if the current element == 1
                if i == r_num:
                        #increment max_consecutive by one
                        inc += 1
                        #and check which one is the maximum number between current number and max_conseutive_ones
                        max_consecutive_ones = max(max_consecutive_ones, inc)
                #else dont increment
                else:
                        inc = 0
        #then return max_consecutive_ones
        return max_consecutive_ones

#test with any array input
binary_numbers = [1,0,1,1,0,1]

print('Max Consecutive Ones = ', Solution.findMaxConsecutiveOnes(binary_numbers))


# Output => Max Consecutive Ones =  2