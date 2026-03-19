#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ")
last_digit = number % 10
if number < 0:
    last_digit -= 10
    print(f"{last_digit}")
elif number > 0:
    print(last_digit)
elif number == 0:
    print(number)
elif last_digit < 6 and != 0:
    print(" and is less than 6 and not 0")
elif last_digit > 5:
    print(" and is greated that 5")
else:
    print("and is 0")
