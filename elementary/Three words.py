# https://py.checkio.org/mission/three-words/

def checkio(words):
    
    slo = 0
    for i in words.split():
        if i.isalpha():
            slo += 1
            if slo == 3:
                break
        elif i.isdigit():
            slo = 0
    
    if slo >= 3:
        return True
    else:
        return False

