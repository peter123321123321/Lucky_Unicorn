"""Random token generator v3
format currency
calculate percentages to ensure odds favour house
unicorn 10% everything else 30% each
 """

import random

token = ["horse", "horse", "horse",
         "donkey", "donkey", "donkey",
         "zebra", "zebra", "zebra",
         "unicorn"]

user_balance = 100
starting_balance = user_balance

# testing loop to generate 100 tokens
for item in range(100):
    computer = random.choice(token)
    # adjust balance depending on token generated
    if computer == "unicorn":
        user_balance += 4
    elif computer == "zebra":
        user_balance -= 1
    else:
        user_balance -= 0.5

    # Output
print(f"starting balance is {starting_balance:.2f}")
print(f"your balance is {user_balance:.2f}")
