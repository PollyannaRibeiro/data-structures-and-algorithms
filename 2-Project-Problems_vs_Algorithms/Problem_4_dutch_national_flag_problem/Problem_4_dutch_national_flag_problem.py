def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    """
    arr = input_list

    first_pivot = None
    current_pivot = 0
    last_pivot = len(arr) - 1

    while current_pivot <= last_pivot:

        if arr[current_pivot] == 0:

            if first_pivot is None:
                first_pivot = 0
            else:
                first_pivot +=1

            if current_pivot == first_pivot:
                current_pivot += 1
                continue

            temp = arr[current_pivot]
            arr[current_pivot] = arr[first_pivot]
            arr[first_pivot] = temp

        elif arr[current_pivot] == 2:

            temp = arr[current_pivot]
            arr[current_pivot] = arr[last_pivot]
            arr[last_pivot] = temp

            last_pivot -=1

        else:
            current_pivot +=1

    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0])
test_function([2, 1, 1, 0, 1, 1])
test_function([2, 1, 2, 0, 0, 2, 0, 0, 1])
test_function([2, 2, 2])
test_function([])

