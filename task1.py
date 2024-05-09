import timeit
from random import shuffle


def insertion_sort(ulst):
    lst = ulst.copy()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

sequences = {}
for n in [10, 100, 1000, 10000]:
    sequences[n] = list(range(n))
    shuffle(sequences[n])

def main():
    setup_string = "from __main__ import insertion_sort, " + \
                   "merge_sort, sequences"
    for n in [10, 100, 1000, 10000]:
        print(f"Shuffled sequence of range({n}):")
        for sort_name in ["merge_sort", "insertion_sort", "sorted"]:
            timeit_res = timeit.timeit(f"{sort_name}(sequences[{n}])", 
                                       number=100,
                                       setup=setup_string)
            print(f"\tTime of {sort_name:<20}: {timeit_res}")
        print()

if __name__ == '__main__':
    main()
