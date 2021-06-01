#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value = None):
    return_array = array
    while len(array) < min_size:
        return_array.append(value)
    return (return_array)
