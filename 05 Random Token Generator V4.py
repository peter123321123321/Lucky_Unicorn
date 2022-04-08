"""Random token generator v5
calculate odds to ensure that the house has the advantage
5% unicorn 30% zebra 65% donkey/horse
 """

import random

starting_balance = 100
user_balance = starting_balance

# testing loop that generates token 100 times
for item in range(100):
    computer = random.randint(1, 100)

    # adjust balance
    # if computer is between 1-5
    # user gets a unicorn(+4$ to balance)
    if 1 <= computer <= 5:
        user_balance += 4
        token = "Unicorn"

    # if computer is between 6-36
    # user gets a zebra(-1$ to balance)
    elif 6 <= computer <= 36:
        user_balance -= 1
        token = "Zebra"

        # in all other cases token is a Donkey or Horse
        # (-0.5$ to balance regardless of either donkey or horse)
    else:
        user_balance -= 0.5
        # if computer is even set token as Horse
        if computer % 2 == 0:
            token = "Horse"

        # in all other cases set token as Donkey
        else:
            token = "Donkey"

    # Output
    print(f"Token: {token} Balance: {user_balance:.2f}")

print()
print(f"Starting Balance = ${starting_balance:.2f}")
print(f"Final Balance = ${user_balance:.2f}")
