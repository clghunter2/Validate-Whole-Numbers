number = float(input("Enter number"))
while number < 4 or number > 10 or not number.is_integer():
    print('Error. Youre daft!')
    number = float(input("Enter number"))

number = int(number)
