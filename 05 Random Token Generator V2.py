"""Random token generator v2
calculates user_balance based on randomly generated token
(Horse Zebra donkey unicorn)"""

import random

user_balance = 0
tokens = ["donkey", "horse", "zebra", "unicorn"]

# Testing loop to generate 20 tokens
for item in range(20):
    computer = random.choice(tokens)
    print(computer, end='\t')  # wraps output making it easier to document

    # adjust balance depending on token generated
    if computer == "horse":  # Horse
        user_balance -= 0.5
    elif computer == "donkey":  # donkey
        user_balance -= 0.5
    elif computer == "zebra":  # Zebra
        user_balance -= 1
    elif computer == "unicorn":  # Unicorn
        user_balance += 4

    # Output
    print(f"token: {computer} balance: {user_balance:.2f}")
