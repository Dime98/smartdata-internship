# 23. Create a pair of functions to encode and decode strings using the Caesar cipher.

def get_keys_by_value(dict_obj, value):
    return [k for k, v in dict_obj.items() if v == value]

dictionary = {
    "A": "X",
    "B": "Y",
    "C": "Z",
    "D": "A",
    "E": "B",
    "F": "C",
    "G": "D",
    "H": "E",
    "I": "F",
    "J": "G",
    "K": "H",
    "L": "I",
    "M": "J",
    "N": "K",
    "O": "L",
    "P": "M",
    "Q": "N",
    "R": "O",
    "S": "P",
    "T": "Q",
    "U": "R",
    "V": "S",
    "W": "T",
    "X": "U",
    "Y": "V",
    "Z": "W",
}

sentence_to_encode = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG "
# sentence_to_encode = "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques. "
sentence_to_encode = sentence_to_encode.upper()
encoded = ""
for i in sentence_to_encode:
    # print(i)
    if i in dictionary.keys():  encoded += dictionary[i]
    else: encoded += i

encoded = encoded.replace("\n", "")
print(encoded)

decoded = ""
sentence_to_decode = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
for i in sentence_to_decode:
    if i in dictionary.values():
        decoded += get_keys_by_value(dictionary, i)[0]
    else: decoded += i
print(decoded)
