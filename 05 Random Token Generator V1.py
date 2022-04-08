"""Random token generator v1
randomly generates token (Horse Zebra donkey unicorn) in random order"""

import random

token_list = ["zebra", "donkey", "horse", "unicorn"]

# testing loop generates 20 tokens
for item in range(20):
    computer = random.choice(token_list)
    print(computer, end='\t')  # wraps output so it's easy to document
