""""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

"""
Hints
Try a hash table.
Could a bit vector be useful?
Can you solve it in O(N log N) time? What might a solution like that look like?
"""


"""
Loop over the given string 
store it in hash table

Base case: No repetition in string 

return True or False
"""

class UniqueString():

    def __init__(self) -> None:
        pass

    def validateString(s):
        #hash table
        hashSet =  set()

        #looping over given string and store in set

        for char in s:
            if char in hashSet:
                return False
            hashSet.add(char)
        return True 
    
    def validateString2(s):
        pass
print(UniqueString.validateString("Balaji"))
print(UniqueString.validateString("Balaji"))







    
    