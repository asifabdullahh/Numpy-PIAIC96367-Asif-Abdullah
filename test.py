import numpy as np

#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr >= 5) & (arr < 10)] #write your code here 
  
    return ans

    """
     Expected Output:
              array([6, 9])
    """ 
  
print(function13())