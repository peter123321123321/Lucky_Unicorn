"""Lu Y/N
based off 01 yes no checker v3
"""

# functions go here...


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


# Main Routine goes here...
check = yes_no("Have you played before: ")
print(f"You entered '{check}'")
print("")
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")
