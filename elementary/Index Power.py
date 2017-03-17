# https://py.checkio.org/mission/index-power/

def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if n == 0:
        return 1
    elif len(array)-1 < n:
        return -1
    elif len(array)-1 >= n:
        return (array[n])**n
