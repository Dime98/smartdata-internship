# 21. Write a function to find the longest common prefix string amongst a list of
# strings.

import os
str_arr = ["123a", "123ddsa", '123abcaa', "12345"]
 
prefix = os.path.commonprefix(str_arr)
print(prefix)
