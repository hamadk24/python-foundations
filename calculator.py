first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Choose the operation(+, -, /, *): ")

if operation == '+':
    print('{} + {} = '.format(first_number, second_number))
    print(first_number + second_number)

elif operation == '-':
    print('{} - {} = '.format(first_number, second_number))
    print(first_number - second_number)

elif operation == '*':
    print('{} * {} = '.format(first_number, second_number))
    print(first_number * second_number)

elif operation == '/':
    print('{} / {} = '.format(first_number, second_number))
    print(first_number / second_number)

else:
    print('You have not typed a valid operator or number, please run the program again.')
