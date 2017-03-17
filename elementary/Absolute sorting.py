# https://py.checkio.org/mission/absolute-sorting/

def checkio(numbers_array):
    
    new_array = list(numbers_array)
    result = []
    
    for i in range(len(new_array)):
        result.append(new_array[i])
        result.sort(key = abs)
    return result
