# https://py.checkio.org/mission/right-to-left/

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    way = ","
    new_phrases = way.join(phrases)
    
    return new_phrases.replace("right", "left", new_phrases.count("right"))
