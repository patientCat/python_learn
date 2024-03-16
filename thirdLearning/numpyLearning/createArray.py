import numpy as np

# for beginners

# numpy array is different from python list

# attention : the constructor param need a python array !
# wrong example :
# a = np.array(1, 2, 3, 4, 5, 6)
a = np.array([1, 2, 3, 4, 5, 6])
print(a)

# create a basic array

a = np.array([1, 2, 3])
a = np.zeros(2)
a = np.empty(2)

# the default type of np.array datatype is float64
# to specify your data type
a = np.ones(3, dtype=np.int64)


# to create a example array for demonstration
example = np.arange(0, 6, 1, dtype=np.int32)
print("example={}".format(example))

example = np.arange(9).reshape(3, 3)
print("example={}".format(example))

