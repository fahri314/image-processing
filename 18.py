import numpy as np

my_Array = np.array([[1,2,3],[2,6,9]],np.int32)
my_Array.ndim,my_Array.shape
my_Array_1 = my_Array.reshape(1,6)
print(my_Array)
print("  ")
print(my_Array_1)