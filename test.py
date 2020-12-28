import numpy as np

#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    x = np.zeros(4, dtype=np.int64)
    return x #write your code here

    """
    Expected Output:
          array([0, 0, 0, 0], dtype=int64)
    """ 

z = function7()
print(z)