"""component two how much
ask user how much they want to play with and
check that it is a valid integer between 1 and 10.
if it is this amount becomes the balance in there account"""

user_balance = int(input("how much money do you want to play with(must be between 1 and 10)"))

# Keep asking until a valid number is entered
while not 1 <= user_balance <= 10:
    print("Please enter a number between 1 and 10")
    # Ask for amount
    user_balance = int(input("how much do you want to play with"))

print(f"you are playing with {user_balance}")
