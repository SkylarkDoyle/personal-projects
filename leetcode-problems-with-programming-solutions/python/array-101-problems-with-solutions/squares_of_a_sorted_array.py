# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass
    
    def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # i = 0
        
        #this is an inplace operation => we do not create another array, which takes extra space in memory

        # while i < len(nums):
        #     #square each element
        #     squares = nums[i]**2
        #     #make each element equal the squared numbers
        #     nums[i] = squares
        #     i += 1

        # nums.sort()  
        # return nums


        new_list = []
        for i in nums:
                #square each element in list
                square = i ** 2
                #then add to new list
                new_list.append(square)
                #then sort the new list in ascending order
                new_list.sort()
        return new_list

#test with any array input
nums = [-7,-3,2,3,11]

print('Squares of a Sorted Array = ', Solution.sortedSquares(nums))


#Output => Squares of a Sorted Array =  [4, 9, 9, 49, 121]
        