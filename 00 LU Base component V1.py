"""Lu Y/N
based off 01 yes no checker v3
"""

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
    print("=== How To Play ===")
    print("")
    print("instructions go here")
    print("")


# Number checking function
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


# Main Routine goes here...
played_before = yes_no("Have you played before: ")

if played_before == "No":
    instructions()
