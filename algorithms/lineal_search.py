import random

def lineal_search(the_list, objective):
    match = False

    for element in the_list: # O(n)
        if element == objective:
            match = True
            break

    return match


if __name__ == '__main__':
    list_size = int(input('What is the size of the list? '))
    objective = int(input('What number do you want to find? '))

    the_list = [random.randint(0, 100) for i in range(list_size)]

    find_it = lineal_search(the_list, objective)
    print(the_list)
    print(f'El element {objective} {"is" if find_it else "is not"} in the list')