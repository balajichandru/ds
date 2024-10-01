"""
1984. Minimum Difference Between Highest and Lowest of K Scores

You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. 
You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest 
and the lowest of the k scores is minimized.

Return the minimum possible difference.

Example 1:

Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
Example 2:

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
"""

"""
why sorting?

sorting gives the min and max of any given range at any possible window

so two pointer are intialized in such a way that they represent the given range of selection

[9,4,1,7].sort -> [1,4,7,9] -> this gives min and max of window for any window value 

r is the key  where r = k-1 and l moves based on r < len(array)
"""
class Solution():
    
    def calculateMinDiff(self,nums,k):

        nums.sort()
        l , r = 0, k-1
        mindiff = float("inf")

        while r< len(nums):
            mindiff = min(mindiff, nums[r] - nums[l])
            l , r = l+1 , r+1 

        return mindiff 
    
print(Solution().calculateMinDiff([9,4,1,7],3))
