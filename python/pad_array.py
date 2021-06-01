#Compare length of ARRAY to MIN_SIZE
#If length ARRAY is less than MIN_SIZE append VALUE to end of
#ARRAY equal to MIN_SIZE minus length of ARRAY
def pad(array, min_size, value = None):
    if (len(array) < min_size):
        i = 0
        number_elements_to_add = min_size - len(array)
        while i < number_elements_to_add:
            array.append(value)
            i += 1
    
    return array
