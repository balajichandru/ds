"""
189. Rotate Array
Medium
Topics
Companies
Hint
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

1 ->5   5->2
2 -> 6  6 ->3
3->7     7->4
4->1
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution:
    def rotate(self, nums, k):
        """
        when you rotate array by some times which equals to array length , then the array is same
        """
        k = k % len(nums)
        self.nums = nums
        #reverse the input array 
        self.reverse(0,len(nums)-1)
        self.reverse(0,k-1)
        self.reverse(k,len(nums)-1)

        return self.nums

        
    
    def reverse(self,n,k):
        
        L = n 
        R = k

        while L< R:
            self.nums[L] ,self.nums[R] = self.nums[R], self.nums[L]
            L+=1
            R-=1
        return None
    
print(Solution().rotate([1,2,3,4,5,6,7],6))