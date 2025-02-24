import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list).reshape(3, 3)
    mean = [[np.mean(x) for x in matrix.transpose()], [np.mean(x) for x in matrix], np.mean(list)]
    variance = [[np.var(x) for x in matrix.transpose()], [np.var(x) for x in matrix], np.var(list)]
    std = [[np.std(x) for x in matrix.transpose()], [np.std(x) for x in matrix], np.std(list)]
    max = [[np.max(x) for x in matrix.transpose()], [np.max(x) for x in matrix], np.max(list)]
    min = [[np.min(x) for x in matrix.transpose()], [np.min(x) for x in matrix], np.min(list)]
    sum = [[np.sum(x) for x in matrix.transpose()], [np.sum(x) for x in matrix], np.sum(list)]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum
        }
    return calculations