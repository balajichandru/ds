"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith "
, 13
Output: "Mr%20John%20Smith"
"""

class Solution():

    def URLify(str_list, trueLength):

        spaceCount = 0

        for key in range(trueLength):
            if str_list[key] == ' ':
                spaceCount +=1
        
        index = trueLength + spaceCount * 2
        print(index)

        str_list = str_list +[' '] * (index-trueLength)
        print(str_list)

        for i in range(trueLength-1,-1,-1):
            if str_list[i] ==' ':
                str_list[index-1] = "0"
                str_list[index-2] = "2"
                str_list[index-3] = "%"
                index -=3
            else:
                str_list[index-1] = str_list[i]
                index -=1
            
        return ''.join(str_list)
            
            
        
            
        
        # new_len = trueLength+space_count*2
        # print(len(str_list),space_count,new_len)

print(Solution.URLify(list('Mr John Smith    '), 13))

