"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same.
 """


# Time Complexity: O(n)
class Solution(object):
    def __init__(self) -> None:
        pass

    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        newList = []
        
        if len(nums) == 0:
            return "Empty List, Please add values into list"
        
    
        for i in nums:
            #checks if function already exist in other array, if it doesnt, then add to the array
            if i not in newList:
                newList.append(i)
                
        nums[:] = newList[:]
        return nums


        """
        OR     two pointer approach
        #start from second element, first element shouldnt be touched
        writePointer = 1
                
                for readPointer in range(1, len(nums)):
                    #if current elemnt is not equal to previous element that means it is a unique element
                    if nums[readPointer] != nums[readPointer - 1]:
                        #add the unique element to the next position 
                        nums[writePointer] = nums[readPointer]
                        
                        writePointer += 1
                        
                return writePointer
                
        """

nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution.removeDuplicates(nums))

#Output => [0, 1, 2, 3, 4] |Remove all duplicates|