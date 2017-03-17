# https://py.checkio.org/mission/secret-message/

def find_message(text):
    """Find a secret message"""
    
    alf = "ABCDEFGHIJKLMNOPRSTQUVWXYZ"
    word = ""
    
    for i in text:
        if i in alf:
            word += i
    return word
