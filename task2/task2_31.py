# 31. Given a balanced expression that can contain opening and closing parenthesis, check 
# if it contains any duplicate parenthesis or not.
# Input:  ((x+y))+z
# Output: true
# Explanation: Duplicate () found in subexpression ((x+y))
# Input:  (x+y)
# Output: false
# Explanation: No duplicate () is found

def dup_check(inp, dictionary):
    ret = False
    for k, v in dictionary.items():
        if inp.find(k) >= 0 and inp.find(v) >= 0 :
            print(f"duplicates found: {k} {v}")
            return True
        else: return False
inp = "((x+y))+z"

dictionary = {
    "((" : "))",
    "[[" : "]]",
}

dup_check(inp, dictionary)



