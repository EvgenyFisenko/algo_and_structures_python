import random
import timeit


def bubble_sort(lst):
    """
    (O(n**2))
    """
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i+1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def short_bubble_sort(lst):
    """
    (O(n**2))
    """
    exchanges = True
    num = len(lst) - 1
    while num > 0 and exchanges:
        exchanges = False
        for i in range(num):
            if lst[i] > lst[i + 1]:
                exchanges = True
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        num = num - 1
    return lst


def insertion_sort(lst):
    """
    (O(n**2))
    """
    for index in range(1, len(lst)):

        current_value = lst[index]
        position = index

        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position = position - 1

        lst[position] = current_value

    return lst


def merge_sort(alist):
    """
    (O(n log n))
    """
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    return alist


def quick_sort(alist):
    """
    (O(n log n)), но может деградировать до (O(n**2))
    """
    quick_sort_helper(alist, 0, len(alist) - 1)

    return alist


def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def selection_sort(lst):
    """
    (O(n**2))
    """
    for fillslot in range(len(lst) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if lst[location] > lst[position_of_max]:
                position_of_max = location

        temp = lst[fillslot]
        lst[fillslot] = lst[position_of_max]
        lst[position_of_max] = temp

    return lst


def shell_sort(alist):
    """
    Производительность колеблется между (O(n)) и (O(n^2))
    """
    sublistcount = len(alist) // 2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2

    return alist


def gap_insertion_sort(alist, start, gap):

    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def shaker_sort(lst):
    """
    (O(n^2))
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        for i in range(left, right):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        right -= 1
        for i in range(right, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


def gen_list(len_lst):
    """
    генерирует список заданной длины
    """
    lst = [random.randint(-100, 100) for _ in range(len_lst)]
    return lst


def get_sorts_time_table():
    sorts = ('bubble_sort', 'short_bubble_sort', 'insertion_sort', 'merge_sort', 'quick_sort',
             'selection_sort', 'shell_sort', 'shaker_sort')
    list_lens = (10, 100, 300)

    print(f"{'Sort Name':30s}"
          f"{f'{list_lens[0]} el':13s}{f'{list_lens[1]} el':13s}{f'{list_lens[2]} el'} \n{'-' * 63}")

    for sort in sorts:
        print(f"{sort:25s}", end='')
        for list_len in list_lens:
            test_list = (gen_list(list_len))
            print(f"{timeit.timeit(f'{sort}({test_list})', setup=f'from __main__ import {sort}', number=1000):12f}",
                  end=' ')
        print()


get_sorts_time_table()
