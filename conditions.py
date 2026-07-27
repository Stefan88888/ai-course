# conditions_practice.py
# Check if a number is positive, negative, or zero

user_input = input("Enter a number: ")
number = float(user_input)  # float чтобы можно было ввести 2.5

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

if number % 2 ==0:
    print("this number is even")
else:
    print("this number is odd")