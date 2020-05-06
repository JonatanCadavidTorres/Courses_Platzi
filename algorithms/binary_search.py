import random

def binary_search(the_list, start, end, objective):
    print(f'searching {objective} between {the_list[start]} and {the_list[end - 1]}')
    if start > end:
        return False

    middle = (start + end) // 2

    if the_list[middle] == objective:
        return True
    elif the_list[middle] < objective:
        return binary_search(the_list, middle + 1, end, objective)
    else:
        return binary_search(the_list, start, middle - 1, objective)


if __name__ == '__main__':
    list_size = int(input('What is the size of the list? '))
    objective = int(input('What number do you want to find? '))

    the_list = sorted([random.randint(0, 100) for i in range(list_size)])

    find_it = binary_search(the_list, 0, len(the_list), objective)

    print(the_list)
    print(f'The element {objective} {"is" if find_it else "is not"} in the list')