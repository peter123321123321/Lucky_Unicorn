"""Lu Y/N
based off 01 yes no checker v3
"""
import random


# functions go here...


# Yes no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they've played before
        answer = input(question_text).lower()

        # If they say yes, output Program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Error - Please enter yes or no")


# Function to show instructions
def instructions():
    print(formatter("=", "How To Play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. You will get a random token which might"
          " be a horse, a zebra, a donkey, or a unicorn")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your money back. These are the payout amounts:\n"
          "\tUnicorn: $5.00(balance increases by $4\n"
          "\tZebra: $0.00(balance decreases by $1.00)\n"
          "\tHorse: $0.50(balance decreases by $0.50)\n"
          "\tDonkey: $0.50(balance decreases by $0.50)\n")
    print("\nSee if you can avoid zebras, get the unicorns, and finish with"
          " more money than you started with.\n")

    print("*" * 150)
    print()


# Number checking function
def num_check(question, low, high):
    error = "That is not a valid number\n" \
            "please enter a number between 1 and 10\n".format(low, high)

    # Keep asking until a valid number(1, 10) is input
    while True:
        try:
            # Ask amount
            response = int(input(question))
            # Check if number between valid range
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Function to generate random token
def generate_tokens(balance):
    rounds_played = 1
    play_again = ""
    while play_again != "x":
        print(formatter(".", f"Round {rounds_played}"))
        print()
        rounds_played += 1  # keep track of rounds
        computer = random.randint(1, 100)

        # adjust balance
        # if computer is between 1-5
        # user gets a unicorn(+4$ to balance)
        if 1 <= computer <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()

        # if computer is between 6-36
        # user gets a zebra(-1$ to balance)
        elif 6 <= computer <= 36:
            balance -= 1
            print(formatter("Z", "Bad luck you got a Zebra"))
            print()

            # in all other cases token is a Donkey or Horse
            # (-0.5$ to balance regardless of either donkey or horse)
        else:
            balance -= 0.5
            # if computer is even set token as Horse
            if computer % 2 == 0:
                print(formatter("H", "You got Horse"))

            # in all other cases set token as Donkey
            else:
                print(formatter("D", "You got a Donkey"))

        # Output
        print(f"Your Balance is now: ${balance:.2f}")
        if balance < 1:
            print("\nSorry you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play"
                               " again or 'X' to exit").lower()
        print()
    return balance


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine goes here...
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played before? ")

if played_before == "No":
    instructions()

# ask the user how much they want to play with
starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with {starting_balance}")
print()

closing_balance = generate_tokens(starting_balance)
print(formatter("=", "Thanks for playing"))
print()
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
