#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        result = ""
        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        if not result:
            result = str(number)
        print(result, end=" ")
