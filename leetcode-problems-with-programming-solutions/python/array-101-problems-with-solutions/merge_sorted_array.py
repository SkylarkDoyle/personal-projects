# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.


class Solution(object):
    def __init__(self) -> None:
        pass

    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # Time Complexity: O(n)

        #the mth positon element to the end of the list is replaced with second list from beginning to nth position of element
        # nums1[m:] = nums2[:n]
        # #then sort the merge list
        # nums1.sort()

        """
         OR USE THIS ALGORITHM
        """

        #get the last element in nums1
        last = m + n - 1

        # Time Complexity: O(m + n)
        while m > 0 and n > 0:
            #if the real numbers at the end of nums1 > real numbers at the end of nums2
            if nums1[m - 1] > nums2[n - 1]:
                #then add the number to the end of nums1 instead
                nums1[last] = nums1[m - 1]
                #then move to the element at the left
                m -= 1
            #if the real numbers at the end of nums1 < real numbers at the end of nums2
            else:
                #then add the number to the end of nums1 instead
                nums1[last] = nums2[n - 1]
                 #then move to the element at the left
                n -= 1
             #then move last elemnt 
            last -= 1

        #if there is any leftover element in nums2
        while n > 0:
            #then add current last element of nums1
            nums1[last] = nums2[n - 1]
            #then move to the element at the left
            n -= 1
            last -= 1

        return nums1

#test with any array input
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


print(Solution.merge(nums1, m, nums2, n))

#Output => [1, 2, 2, 3, 5, 6] |excluding the zeroes|
