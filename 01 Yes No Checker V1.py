# Ask the user if they have played before
check = str(input("Have you played before: "))

# If they say yes, output Program continues
if check == "yes":
    print("Program continues")

# If they say no, output 'Display instructions'
elif check == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Error - Please enter yes or no")

