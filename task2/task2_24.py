# 24. Write a function that, given a dictionary, would translate a sentence. Words
# not found in the dictionary need not be translated.

# ! modified dict, deleted spaces in dictionary and added element

dictionary = {
 "mama": "mother",
 "papa": "father",
 "abc": "testabc"
}

sentence = "mama is with papa "

for k in dictionary.keys():
    # print()
    # print(k)
    # print(dictionary[k])
    # print(k in sentence)
    if k in sentence:
        sentence = sentence.replace(k, dictionary[k])

print(sentence)