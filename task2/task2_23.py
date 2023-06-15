# 23. Create a pair of functions to encode and decode strings using the Caesar cipher.
import string

sentence_to_encode = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG "
# sentence_to_encode = "the"

letters = [i for i in string.ascii_uppercase]
# print(letters)

encoded = ""
for i in sentence_to_encode:
    i = i.upper()
    if i.upper() in letters:
        encoded += letters[letters.index(i)-3 % 26]
    else: 
        encoded += i
print(sentence_to_encode)
print(encoded)

print()

sentence_to_decode = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD "
decoded = ""
for i in sentence_to_decode:
    i = i.upper()
    if i.upper() in letters:
        indx = letters.index(i)+3 % 26
        if indx >= len(letters):
            indx = abs(len(letters) - indx)
        decoded += letters[indx]
    else: 
        decoded += i
print(sentence_to_decode)
print(decoded)

print()

# # =========================
# # from https://www.scaler.com/topics/caesar-cipher-python/
# def encrypt_text(plaintext,n):
#     ans = ""
#     # iterate over the given text
#     for i in range(len(plaintext)):
#         ch = plaintext[i]
#         if ch.isalpha():
#             # check if a character is uppercase then encrypt it accordingly 
#             if (ch.isupper()):
#                 ans += chr((ord(ch) + n-65) % 26 + 65)
#             # check if a character is lowercase then encrypt it accordingly
#             else:
#                 ans += chr((ord(ch) + n-97) % 26 + 97)
#         else:
#             ans += ch
    
#     return ans

# shift = -3
# print("==")
# sentence_to_encode = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG "
# print(sentence_to_encode)
# print( encrypt_text(sentence_to_encode, shift) )
