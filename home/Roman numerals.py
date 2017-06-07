# https://py.checkio.org/mission/roman-numerals/

def checkio(data):

    jednosci = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dziesiatki = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    setki = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M"]
    str_data = str(data)
    result = ""
    
    if len(str_data) == 4:
        result = setki[10]*int(str_data[0]) + setki[int(str_data[1])] + dziesiatki[int(str_data[2])] + jednosci[int(str_data[3])]
        return result
    elif len(str_data) == 3:
        result = setki[int(str_data[0])] + dziesiatki[int(str_data[1])] + jednosci[int(str_data[2])]
        return result
    elif len(str_data) == 2:
        result = dziesiatki[int(str_data[0])] + jednosci[int(str_data[1])]
        return result
    elif len(str_data) == 1:
        result = jednosci[int(str_data[0])]
        return result
