"""component 4 - game mechanics and looping v1
based on 05 token generator v4 but hard-wired to only allocated donkeys
gives user feedback about number of rounds and maintains balance
test amount set to $5"""

import random

# Main Routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

while play_again != "x":
    rounds_played += 1  # keep track of rounds
    computer = random.randint(6, 36)  # can only be a donkey

    # adjust balance
    # if computer is between 1-5
    # user gets a unicorn(+4$ to balance)
    if 1 <= computer <= 5:
        token = "unicorn"
        balance += 4

    # if computer is between 6-36
    # user gets a zebra(-1$ to balance)
    elif 6 <= computer <= 36:
        token = "zebra"
        balance -= 1

        # in all other cases token is a Donkey or Horse
        # (-0.5$ to balance regardless of either donkey or horse)
    else:
        balance -= 0.5
        # if computer is even set token as Horse
        if computer % 2 == 0:
            token = "Horse"

        # in all other cases set token as Donkey
        else:
            token = "donkey"

    # Output
    print(f"Round {rounds_played}. token: {token}, Balance: ${balance:.2f}")
    if balance < 1:
        print("\nSorry you have run out of money")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\n<enter> to play"
                           " again or 'X' to exit").lower()
    print()

print("Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print("Goodbye")
