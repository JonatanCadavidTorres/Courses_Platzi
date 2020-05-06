

def sort_by_insertion(the_list):

    for index in range(1, len(the_list)):
        actual_value = the_list[index]
        actual_position = index

        while actual_position > 0 and the_list[actual_position - 1] > actual_value:
            the_list[actual_position] = the_list[actual_position - 1]
            actual_position -= 1

        the_list[actual_position] = actual_value

    return the_list

the_list = [62, 32, 10, 62, 94, 89, 0, 53, 71, 61, 1, 33, 26, 52,
            15, 79, 13, 58, 3, 79, 36, 42, 29, 70, 20, 27, 44, 79, 
            17, 32, 45, 99, 63, 90, 8, 13, 30, 2, 79, 8, 91, 93, 74, 1, 40, 35, 64, 14, 94, 51]

print(the_list)
print(sort_by_insertion(the_list))