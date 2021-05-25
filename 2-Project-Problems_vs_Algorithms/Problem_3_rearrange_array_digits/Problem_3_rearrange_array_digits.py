"""
Rearrange Array Elements so as to form two number such that their sum is maximum.
"""

def sorting_arr(input_list):

    # quicksort
    arr = input_list
    pivot_index = len(arr) - 1
    pivot = arr[pivot_index]
    set_index_visited = set()
    i = 0

    while len(set_index_visited) != len(arr):
        if i in set_index_visited:
            i += 1
            continue

        if pivot_index in set_index_visited:
            pivot_index -= 1
            pivot = arr[pivot_index]

            if pivot_index < 0:
                break
            continue

        while i is not pivot_index:
            start = arr[i]
            start_index = i
            before_pivot_index = pivot_index - 1
            before_pivot = arr[before_pivot_index]
            temp = before_pivot

            if pivot > start:

                arr[before_pivot_index] = pivot
                arr[pivot_index] = start
                pivot_index = before_pivot_index
                if before_pivot_index is not start_index:
                    arr[start_index] = temp
                continue

            if pivot <= start:
                i += 1

        if pivot_index == i:
            set_index_visited.add(i)
            pivot_index = len(arr) - 1
            pivot = arr[pivot_index]
            i = 0

    return arr


def rearrange_digits(input_list):

    if len(input_list) == 0:
        return []
    if len(input_list) == 1:
        return [input_list[0], 0]

    sorted_numbers = sorting_arr(input_list)

    first_elem = str()
    second_elem = str()

    while len(sorted_numbers) > 0:

        first_elem = first_elem + str(sorted_numbers.pop(0))
        if len(sorted_numbers) > 0:
            second_elem = second_elem + str(sorted_numbers.pop(0))

    return [int(first_elem), int(second_elem)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[], []])
test_function([[1, 0], [1, 0]])
test_function([[10], [10]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 1, 3, 4, 4, 8, 9, 9], [9841, 9431]])
test_function([[1, 1, 1, 1, 1, 1, 1], [1111, 111]])
test_function([[0, 0, 0, 1, 0, 0, 0], [1000, 0]])


