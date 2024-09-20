import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list)

    flat_mean = np.mean(arr)
    flat_variance = np.var(arr)
    flat_std = np.std(arr)
    flat_max = arr.max()
    flat_min = arr.min()
    flat_sum = arr.sum()

    matrix = arr.reshape(3, 3)
    print(matrix)

    rows_mean = np.mean(matrix, axis=1).tolist()
    rows_variance = np.var(matrix, axis=1).tolist()
    rows_std = np.std(matrix, axis=1).tolist()
    rows_max = matrix.max(1).tolist()
    rows_min = matrix.min(1).tolist()
    rows_sum = matrix.sum(1).tolist()

    columns_mean = np.mean(matrix, axis=0).tolist()
    columns_variance = np.var(matrix, axis=0).tolist()
    columns_std = np.std(matrix, axis=0).tolist()
    columns_max = matrix.max(0).tolist()
    columns_min = matrix.min(0).tolist()
    columns_sum = matrix.sum(0).tolist()

    calculations = {
        "mean": [columns_mean, rows_mean, flat_mean],
        "variance": [columns_variance, rows_variance, flat_variance],
        "standard deviation": [columns_std, rows_std, flat_std],
        "max": [columns_max, rows_max, flat_max],
        "min": [columns_min, rows_min, flat_min],
        "sum": [columns_sum, rows_sum, flat_sum],
    }
    # print(calculations)
    return calculations
