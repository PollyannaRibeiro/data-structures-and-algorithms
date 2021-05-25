def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    search_arr = input_list
    first_index = 0
    last_index = len(search_arr)-1

    while first_index <= last_index:

        middle_index = int((first_index + last_index) / 2)

        first_number = search_arr[first_index]
        middle_number = search_arr[middle_index]
        last_number = search_arr[last_index]

        if first_number == number:
            return first_index
        if middle_number == number:
            return middle_index
        if last_number == number:
            return last_index

        if middle_number > number:
            # rotated
            if first_number > number:
                first_index = middle_index+1
                last_index = last_index-1
                continue
            if first_number < number:
                first_index = first_index+1
                last_index = middle_index-1
                continue

        else:
            if last_number > number:
                first_index = middle_index+1
                last_index = last_index-1
                continue
            if last_number < number:
                first_index = first_index+1
                last_index = middle_index-1
                continue
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # element not in the array
test_function([[6, 7, 8, 1, 2, 3, 4], 0]) # element not in the array
test_function([[], 5]) # empty array

