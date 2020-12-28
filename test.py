#task3
import numpy as np
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[3::7,4]
    d = a[6::7,9] #wrtie your code here
    x = np.concatenate((x,d), axis =0)
    x = np.sort(x)
    return x
    """
    Expected Output:
     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
       945, 980] 
    """ 
x = function3()
print(x)
# a = np.arange(1, 100*10+1).reshape((100,10))
# print(a)