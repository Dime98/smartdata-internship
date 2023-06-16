# 21. Write a function to find the longest common prefix string amongst a list of
# strings.

import os
str_arr = ["123a", "123ddsa", '123abcaa', "12345"]
 
prefix = os.path.commonprefix(str_arr)
# print(prefix)

def commonprefix(m):
    if not m: return ''
    m = tuple(map(os.fspath, m))
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

print(commonprefix(str_arr))
