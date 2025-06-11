import numpy as np 

def calculate(list: list) -> dict:
    """
    take a list of 9 elements and converts them into a 3 x 3 matrix, 
    then gives out the mean, variance, std, max, min, sum of all the coloums(axis=0) and
    the same for rows(axis=1) and gives a flat value of the entire list. 
    """
    
    if len(list) != 9:
        raise ValueError("List should have 9 elements")

    arr = np.array(list)

    matrix = arr.reshape(3, 3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'var': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0, dtype("float16"), ddof=0).tolist(),
            
        ]
    }
    
    
    return calculations
