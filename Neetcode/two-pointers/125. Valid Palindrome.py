"""
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution():
    def isPalindrome(self,s:str)->bool:
        l , r = 0, len(s)-1
        while l < r :
        
            while l < r  and not self.alphanum(s[l]):
                l+= 1
            
            while r > l and not self.alphanum(s[r]):
                r-= 1

            if s[l] != s[r]:
                return False
            l ,r  = l+1, r-1
        return True
            
    
    def alphanum(self,c):
        return (
                ord('A') <= ord(c) <= ord("Z") or
                ord('a') <= ord(c) <= ord("z") or
                ord('0') <= ord(c) <= ord("9")
            )


print(Solution().isPalindrome(" man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))

