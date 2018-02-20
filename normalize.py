import numpy as np

def demean(arr):
    """Demeans an array (i.e., subtracts the mean
    from each value in the array)."""

    arr_demeaned = arr - np.mean(arr)
    return arr_demeaned
