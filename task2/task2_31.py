# 31. Given a balanced expression that can contain opening and closing parenthesis, check 
# if it contains any duplicate parenthesis or not.
# Input:  ((x+y))+z
# Output: true
# Explanation: Duplicate () found in subexpression ((x+y))
# Input:  (x+y)
# Output: false
# Explanation: No duplicate () is found

import collections


def dup_check(inp, parenthesis):
    ret = {}
    for i in parenthesis.keys():
        # dubs = [count for item, count in collections.Counter(inp).items()]
        inv_i = parenthesis[i]
        tmp = f"{i}{inv_i}" # to return open and close parenthesis, prettier outpt
        if i in inp:
            if inp.count(i) != inp.count(inv_i):
                ret[tmp] = False 
            else:
                ret[tmp] = True
        else:
            ret[tmp] = None
    return ret

inp = "(((x+y))+[z]"

parenthesis = {
        "(" : ")" , 
        "[" : "]" , 
        "{" : "}" , 
    }

print(inp)
print()
print(dup_check(inp, parenthesis))




