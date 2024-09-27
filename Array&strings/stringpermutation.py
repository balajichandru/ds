"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
Hints: #106, #121, #134, #136
"""

class Solution():

    def __init__(self,s):

        self.given_string = s
        self.hash_map ={}
        self.letters = 0

    def charFreqGen(self):
        for key in self.given_string:
            if key ==' ':
                continue
            self.letters+=1
            self.hash_map[key.lower()] = 1+  self.hash_map.get(key.lower(),0)
        return self.hash_map.items()
        
    
    def isPalindrome(self):
        foundOdd = False
        for key,value in self.charFreqGen():
            
            if value % 2 == 1:
                if foundOdd:
                    return False
                foundOdd = True
                
        return True
    
print(Solution('Tact Coa').isPalindrome())


            
