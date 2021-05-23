# Return original array if min_size is less than array's size
# if min_size > original array's size, fill array with value until size is reached
# return the changed array
def pad(array, min_size, value=None):
    if min_size <= len(array):
        return array

    while len(array) < min_size:
        array.append(value)

    return array
