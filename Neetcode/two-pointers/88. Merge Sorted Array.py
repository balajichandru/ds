"""
88. Merge Sorted Array
Solved
Easy
Topics
Companies
Hint
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
 representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""

"""
0 should be ignored
[1,2,3] [2,5,6]
l =1 r = 2
l=1
l+=1
l= 2 , r = 2
[1,2,2]
l+=1 , r+=1
l = 3 r = 5
l=3
l+1
[5,6]

"""
class Solution():

    def mergeInplacemerge(self,nums1,m, nums2,n):

        n1, n2, i = m-1, n-1, m+n-1
        while n2 >= 0:
            if n1 >=0 and nums1[n1] > nums2[n2]:
                nums1[i] = nums1[n1]
                n1 -= 1
            else:
                nums1[i] = nums2[n2]
                n2 -= 1
            i -= 1
        

    def merge(self,nums1,m, nums2,n):
        res = []

        l =0

        while l < m and r < n:
            if nums1[l] != 0:
                if nums1[l] < nums2[r]:
                    res.append(nums1[l])
                    l+=1
                elif nums1[l] > nums2[r]:
                    res.append(nums2[r])
                    r+=1
                else:
                    res.append(nums1[l])
                    res.append(nums2[r])
                    l+=1
                    r+=1
        
                
        while l < m and nums1[l] != 0:
            res.append(nums1[l])
            l+=1

        while r < n:
            res.append(nums2[r])
            r+=1

        return res

print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))

