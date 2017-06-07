def checkio(number):

    result = ""
    result_new = ""
    while number != 0:
        if number % 2 == 1:
            result += "1"
        if number % 2 == 0:
            result += "0"
        number //= 2

    for i in result.split():
        new_result = list(i)
        new_result.reverse()
        ''.join(new_result)
    return new_result.count('1')

print(checkio(255))


   
