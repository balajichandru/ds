"""

Given two strings, write a method to decide if one is a permutation of the
other.

Hints:

Describe what it means for two strings to be permutations of each other. Now, look at
that definition you provided. Can you check the strings against that definition?

There is one solution that is 0( N log N) time. Another solution uses some space, but
isO(N) time.

Could a hash table be useful?

Two strings that are permutations should have the same characters, but in different
orders. Can you make the orders the same?

Valid Anagram - Leetcode 242 - Python


"""

class Solution():

    def isAnagaram(s,t):

        # Verify length of two strings ,returns false if given len of strings are not equal

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):

            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for key in countS:
            if countS[key] != countT.get(key,0):
                return False
        return True



print(Solution.isAnagaram("rat","cat"))
print(Solution.isAnagaram("rrra","arrr"))