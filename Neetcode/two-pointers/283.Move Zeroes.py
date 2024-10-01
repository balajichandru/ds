"""
283. Move Zeroes

Given an integer array nums, 
move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        l , r = 0,1

        """
         [0,1,0,3,12] 
         [1,0,0,3,12]
         r+=1
         [1,3,0,0,12]
        """
   

        while r< len(nums):
            if nums[r] == 0 :
                r+=1
            else:
                nums[l] , nums[r] = nums[r],nums[l]
                l, r = l+1, r+1
        return nums
print(Solution().moveZeroes([0,1,0,3,12]))



