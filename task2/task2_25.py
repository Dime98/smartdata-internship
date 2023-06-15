# 25. White a function that, given an array of strings, would group the anagrams together.
# you should have a dictionary with one word, where the values will be the list of same word and its anagrams;

str_dict = {
    "woble": ["arc", "cra", "elbow", "another", "another", "anagrams"],
    "arc": ["cra", "another", "another"],
    "no anagrams": ["cra", "another", "another"],
    }

filtered_dict = {}
for k, v in str_dict.items():
    if k[::-1] in v:
        filtered_dict[k] = k[::-1]

print(filtered_dict)

# str_dict = ["arc", "cra", "woble", "elbow", "another", "word", "anagrams"]

# anagrams = []
# for i in str_arr:
#     if i[::-1] in str_arr:
#         anagrams.append(i)
# print(anagrams)