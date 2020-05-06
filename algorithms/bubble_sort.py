import random


def bubble_sort(the_list):
    n = len(the_list)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            if the_list[j] > the_list[j + 1]:
                the_list[j], the_list[j + 1] = the_list[j + 1], the_list[j]

    return the_list

if __name__ == '__main__':
    list_size = int(input('What is the size of the list? '))

    the_list = [random.randint(0, 100) for i in range(list_size)]
    print(the_list)

    list_sorted = bubble_sort(the_list)
    print(list_sorted)