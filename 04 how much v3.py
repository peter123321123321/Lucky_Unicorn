"""component two how much v3
More efficient code uses range as basis of loop
So I don't have to use valid variable"""

error = "<Error> That is not a valid input <Error>"
user_balance = 0

# Keep asking until a valid number is entered
while not 1 <= user_balance <= 10:
    try:
        # Ask for amount
        user_balance = int(input("Please choose a number between 1 and 10"
                                 "\nhow much do you want to play with"))
        print()

    except ValueError:
        print(error)

print(f"you are playing with {user_balance}")
