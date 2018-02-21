import numpy as np

def demean(arr, dim):
    """Demeans an array (i.e., subtracts the mean
    from each value) for across rows (dim=0)
    or columns (dim=1)."""

    arr_demeaned = arr - np.mean(arr, axis=dim, keepdims=True)
    return arr_demeaned

