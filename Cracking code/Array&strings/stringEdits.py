"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
Hints:#23, #97, #130
"""

"""
class StringEdit():

    def __init__(self,str1,str2):

        self.original_string = str1
        self.modified_string = str2
        self.modified = len(self.original_string) - len(self.modified_string)


    def helper(self):
        i = 0
        while i < len(self.modified_string) and self.modified<=1:
            if  self.modified_string[i] != self.original_string[i]:
                if i+1 < len(self.original_string):
                    if  self.modified_string[i] == self.original_string[i+1]:
                       self.modified+=1
                    else:
                        self.modified+=2
                    i+=1
                else:
                   self.modified+=1
            i+=1
        print("modified", self.modified)
        return self.modified

    def validateEdits(self):
        print(self.modified)

        if   self.helper() > 1:
            return False
        return True

"""


def validateEdits(str1,str2):
    if abs(len(str1) - len(str2)) >1:
        return False
    

    original = str1 if str1< str2 else str2
    modified = str2 if str1< str2 else str1
    p1, p2 = 0, 0
    # pales   => p a l e s
    # pale    => p a l e s


    foundDiff = False
    while p1 < len(original) and p2 < len(modified):
        
        if original[p1] != modified[p2]:
            if foundDiff:
                return False
            foundDiff = True
            if len(original) == len(modified):
                p1 +=1
        else:
            p1 +=1
        p2+=1

    return True


print(validateEdits("Pales","Palessss"))
print(validateEdits("Pales","Ple"))
print(validateEdits("Pale","Bale"))
print(validateEdits("Pales","Palesss"))


# print(StringEdit("Pales","Pale").validateEdits())
# print(StringEdit("Pales","Ple").validateEdits())
# print(StringEdit("Pale","Bale").validateEdits())
# print(StringEdit("Pales","Bake").validateEdits())