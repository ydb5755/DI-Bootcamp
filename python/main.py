number = int(input("please enter a number between 0 and 100"))

if 1 <= number <= 100:
    print("number is good")
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
else:
    print("no good")