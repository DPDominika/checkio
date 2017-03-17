# https://py.checkio.org/mission/number-radix/

def checkio(str_number, radix):
    
    try:
        result = int(str_number, radix)
        return result
    except:
        return -1
