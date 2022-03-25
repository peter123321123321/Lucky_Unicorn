"""component two how much v2
use try/accept and pull error out of loop"""

error = "<Error> Please enter a number between 1 and 10"
valid = False

# Keep asking until a valid number is entered
while not valid:
    try:
        user_balance = int(input("how much do you want to play with"))
        if 1 <= user_balance <= 10:
            print(f"you are playing with {user_balance}")
        else:
            print(error)

    except ValueError:
        print(error)
