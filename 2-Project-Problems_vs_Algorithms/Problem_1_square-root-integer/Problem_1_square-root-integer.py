def seaching_tool(num, arr):
    start_point = 0
    end_point = len(arr)

    while start_point is not None:
        search_point = int((start_point + end_point) / 2)

        if end_point < start_point:
            if num >= arr[end_point][1]:
                return [arr[end_point]]
            elif num < arr[end_point][1] and end_point > 0:
                return [arr[end_point - 1]]

        if num == arr[search_point][1]:
            return [arr[search_point]]
        elif num < arr[search_point][1]:
            end_point = search_point - 1

        else:
            start_point = search_point + 1


def calculating_sqrt(arr, sqrt_table):
    # based on https://www.freecodecamp.org/news/find-square-root-of-number-calculate-by-hand/
    part_1_number = arr
    part_2_to_subtract = None
    part_3_answering = None
    part_4_calculating = None
    first_turn = True

    while part_1_number:
        if part_2_to_subtract is None:
            part_2_to_subtract = part_1_number[0]
        else:
            if part_1_number == [0]:
                part_1_number[0] = '00'

            part_2_to_subtract = int(str(part_2_to_subtract)+str(part_1_number[0]))

        part_1_number.pop(0)

        if part_3_answering is None:
            part_3_answering = seaching_tool(part_2_to_subtract, sqrt_table)[0][0]

        if first_turn is True:
            part_4_calculating = part_3_answering * part_3_answering
            part_2_to_subtract = part_2_to_subtract - part_4_calculating
            first_turn = False
        else:
            temp = part_3_answering*2
            array = [9,8,7,6,5,4,3,2,1,0]
            number = None
            result_of_the_count = None

            for elem in array:
                if int(str(temp)+str(elem))*elem <= part_2_to_subtract:
                    number = elem
                    result_of_the_count = int(str(temp)+str(elem))*elem
                    break
            part_2_to_subtract = part_2_to_subtract - result_of_the_count
            part_3_answering = int(str(part_3_answering)+str(number))

    return part_3_answering


def sqrt(number):

    # negative numbers don't have real square roots
    if number < 0:
        return None

    sqrt_table = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81)]
    split_num = [int(d) for d in str(number)]

    if len(split_num) == 1:
        result = seaching_tool(number, sqrt_table)
        return result[0][0]

    elif len(split_num) == 2:
        result = seaching_tool(number, sqrt_table)
        return result[0][0]

    else:
        #separing into pairs

        number_separated = list()

        if len(split_num) % 2 != 0:
            number_separated.append(split_num[0])
            split_num.pop(0)

        while len(split_num)-1 >= 0:
            number_separated.append(int(str(split_num[0])+str(split_num[1])))
            split_num.pop(0)
            split_num.pop(0)

        return calculating_sqrt(number_separated, sqrt_table)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (45 == sqrt(2025)) else "Fail")
print("Pass" if (30 == sqrt(960)) else "Fail")
print("Pass" if (36 == sqrt(1296)) else "Fail")
print("Pass" if (370 == sqrt(136900)) else "Fail")
print("Pass" if (144 == sqrt(21000)) else "Fail") # not exactly sqrt
print("Pass" if (None == sqrt(-16)) else "Fail")
