from random import randint

def quicksort(lst, start, end):

    if start < end:
        pivot = randint(start, end)

        # intercambiar con el último elemento
        lst[end], lst[pivot] = lst[pivot], lst[end]

        # dividir la lista
        split = partition(lst, start, end)

        # ordenar ambas mitades
        quicksort(lst, start, split - 1)
        quicksort(lst, split + 1, end)

def partition(lst, start, end):

    pivot_index = start - 1

    for index in range(start, end):

        # comparar con el pivote
        if lst[index] < lst[end]:
            pivot_index = pivot_index + 1

            # intercambiar
            lst[pivot_index], lst[index] = lst[index], lst[pivot_index]

    # intercambiar con el último elemento
    lst[pivot_index + 1], lst[end] = lst[end], lst[pivot_index + 1]

    return pivot_index + 1

nums = [7, 2, 5, 1, 29, 6, 4, 19, 11]

quicksort(nums, 0, len(nums) - 1)

print(nums)#  1, 2, 4, 5, 6, 7, 11, 19, 29