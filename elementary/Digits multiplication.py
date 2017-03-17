# https://py.checkio.org/mission/digits-multiplication/

def checkio(number):
    
    list = "123456789"
    new_number = str(number)
    wynik = 1
    
    for i in new_number:
        if i in list:
            wynik *= int(i)
    return wynik
