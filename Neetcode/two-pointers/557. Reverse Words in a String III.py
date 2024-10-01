"""
557. Reverse Words in a String III
Solved
Easy
Topics
Companies
Given a string s, reverse the order of characters in each word within a sentence while still 
preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:

        L = 0 
        R=0
        resArr = []
        while R < len(s):

            while R<len(s) and s[R]!=" ":
                R+= 1
            
            LastR = R-1

            while LastR>=L:
                resArr.append(s[LastR])
                LastR-=1
            
            if R < len(s):
                resArr.append(s[R])
            
            L,R = R+1 ,R+2
        if R == len(s):
            resArr.append(s[L])
        return ''.join(resArr)
    
def reverseWords2(s: str) -> str:
    L = 0
    res = list(s)

    for R in range(len(s)):
        if s[R] == " " or R == len(s)-1:
            tempL, tempR = L, R-1

            if R == len(s)-1:
                tempR = R
            print(tempR, tempL)
            while tempL < tempR:
                res[tempL], res[tempR] = res[tempR], res[tempL]
                tempR-=1
                tempL+=1
            L = R+1
    print(res)
    return ''.join(res)
# print(Solution().reverseWords("I love u"))
print(reverseWords2("I love u"))



            