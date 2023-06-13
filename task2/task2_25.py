# 25. White a function that, given an array of strings, would group the anagrams together.

str_arr = ["arc", "cra", "woble", "elbow", "another", "word", "anagrams"]

anagrams = []
for i in str_arr:
    if i[::-1] in str_arr:
        anagrams.append(i)
print(anagrams)