# https://py.checkio.org/mission/fizz-buzz/

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0 and number % 5 != 0:
        return "Fizz"
    elif number % 5 == 0 and number % 3 != 0:
        return "Buzz"
    else: 
        return str(number)
