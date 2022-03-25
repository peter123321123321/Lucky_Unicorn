"""Lu Y/N
simplifies input by converting it to lowercase.
prints user choice
also allows for y or n input
"""
# Ask the user if they have played before
check = input("Have you played before: ").lower()

# If they say yes, output Program continues
if check == "yes" or check == "y":
    print("Program continues")

# If they say no, output 'Display instructions'
elif check == "no" or check == "n":
    print("Display instructions")

# Otherwise - show error
else:
    print("Error - Please enter yes or no")

print(f"You entered {check}")
