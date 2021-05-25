def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    """
    if len(ints) == 0:
        return ()

    smaller = ints[0]
    bigger = ints[0]

    for int in ints:
        if int > bigger:
            bigger = int
        elif int < smaller:
            smaller = int

    return (smaller, bigger)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if (get_min_max([40, 1, 0, -4]) == (-4, 40)) else "Fail")
print("Pass" if (get_min_max([0, 0, 0, -0]) == (0, 0)) else "Fail")
print("Pass" if (get_min_max([]) == ()) else "Fail")