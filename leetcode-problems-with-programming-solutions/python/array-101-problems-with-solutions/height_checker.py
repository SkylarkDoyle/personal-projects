"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
"""



# Time Complexity: O(n)
class Solution(object):
    def __init__(self):
        pass

    def heightChecker(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        count = 0
        expectedHeights = sorted(heights)
        
        if len(heights) == 0:
            return "Empty List"
        
        #loop through each list
        for i, j in zip(heights, expectedHeights):
            #if the element in heights equal to element in expectedHeights        
            if i != j:
                #increment count by 1
                count += 1
        # return the counted value
        return count

#test with any array input
heights = [1,1,4,2,1,3]
print(Solution.heightChecker(heights))
        
#Output => 3  |in this case, Indices 2, 3, 4 do not match |
