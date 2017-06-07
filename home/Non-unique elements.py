# https://py.checkio.org/mission/non-unique-elements/

def checkio(data):

    new_data = data[:]
    for i in data:
        if data.count(i) == 1:
            new_data.remove(i)
    return new_data
