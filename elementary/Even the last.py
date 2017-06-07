# https://py.checkio.org/mission/even-last/

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    sumo = 0
    array2 = []
    
    if array == []:
        return 0
        
    for i in range(0, len(array)):
        if i % 2 == 0:
            sumo += array[i]
    return sumo*array[-1]
