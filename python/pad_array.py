#REMEMBER TO PSEUDOCODE

# ## Let's get started
# In this challenge, you'll want to write a method `pad`. It will accept a list, a minimum size (non-negative integer) for the list, and an optional argument of what the list should be "padded" with (see the example with "apple" below).

# If the list's length is less than the minimum size, `pad` should return a new list padded with the pad value up to the minimum size.

# For example,
# ```python
# pad([1,2,3], 5)
# ```

# should return

# ```python
# [1,2,3,None,None]


def pad(array, min_size, value = None):

    # append extra values to list if needed
    counter = min_size - len(array)

    # decare counter for values to be appended
    if counter <= 0:
        return array
        
    # append values
    elif counter > 0:
        while counter > 0:
            array.append(value)
            counter -= 1

    return array


    # return extended array to min size with value as the extras

