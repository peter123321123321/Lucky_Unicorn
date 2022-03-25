"""04 how much v4
converted v3 into a function
changed user balance to response
and changed the condition and position of number comparison in the loop
to make the function recyclable"""


def num_check(question, low, high):
    error = "That is not a valid number\n"\
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


# Main Routine
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"you are playing with {user_balance}")
