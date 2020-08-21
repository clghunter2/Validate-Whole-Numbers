# Validate whole numbers
# (not decimal and not text)


number = False

while not number:
    string_in = input("Please enter a whole number")
    number = True
    for letter in string_in:
        if letter >= '0' and letter <= '9' or letter == '.':
            print (letter)
        else:
            number = False
