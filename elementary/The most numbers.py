# https://py.checkio.org/mission/most-numbers/

def checkio(*args):
    
    if args == ():
        return 0
    for i in args:
        if i == ():
            return 0
        else:
            return max(args) - min(args)
