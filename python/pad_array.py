#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value = None):

    #min size <= array return array
    if min_size <= len(array):
        return array
    else:
        #append value while array < min size and return array
        while len(array) < min_size:
            array.append(value)
    return array