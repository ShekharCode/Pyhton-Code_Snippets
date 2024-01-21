# char_count = {}

# sentence = "aaaabcdaassbcssdd"

# for char in sentence:
#     if char not in char_count:
#         char_count[char] = 0
    
#     char_count[char]+=1

# print(char_count)


# default dictionary 
from collections import defaultdict


def default():
    return 0

char_count = defaultdict(default)

sentence = "aaaabcdaassbcssdd"

for char in sentence:
    char_count[char]+=1

print(char_count)