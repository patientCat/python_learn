import numpy as np

# sorting array

arr = np.array([1, 3, 2, 4])
sort_arr = np.sort(arr)

# attention ! np.sort will return a copy of an array which is input
print("arr={}\nsort_arr={}".format(arr, sort_arr))

# concatenate : to link or join together, esp in a chain or series
# give two array :
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))
print("concatenate_array={}".format(c))

# add a row
example = np.arange(12).reshape(3, 4)
print("example={}".format(example))
# do add a row
one_row = [1, 1, 1 ,1]
example_addrow = np.append(example, [one_row], axis=0)
print("example_addrow={}".format(example_addrow))


# add a column

# remove a row

# remove a column