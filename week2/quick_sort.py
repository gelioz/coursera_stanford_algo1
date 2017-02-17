import random
import sys


def get_left_pivot_idx(arr, left_idx, right_idx):
    return left_idx


def get_right_pivot_idx(arr, left_idx, right_idx):
    return right_idx


def get_median_pivot_idx(arr, left_idx, right_idx):
    return sorted(
        (left_idx, right_idx, left_idx + (right_idx - left_idx) // 2),
        key=lambda x: arr[x]
    )[1]


def get_random_pivot_idx(arr, left_idx, right_idx):
    return random.randint(left_idx, right_idx)


def partition(arr, left_idx, right_idx, pivot_idx):
    """ Move arr elements that are less then pivot to the left from pivot,
        greater then pivot - to the right. Returns pivot index.
    """

    # move pivot to beginning of the array
    arr[left_idx], arr[pivot_idx] = arr[pivot_idx], arr[left_idx]
    pivot = arr[left_idx]

    # look for first element greater then pivot - first element of right part
    for i in range(left_idx + 1, right_idx + 1):
        if arr[i] > pivot:
            right_part_idx = i
            break
    else:
        # all elements are less then pivot - we move pivot to the end of array
        arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]
        return right_idx

    # move element less then pivot to left part of array
    for i in range(right_part_idx + 1, right_idx + 1):
        if arr[i] <= pivot:
            arr[right_part_idx], arr[i] = arr[i], arr[right_part_idx]
            right_part_idx += 1

    # swap pivot with last element that less then pivot
    arr[right_part_idx - 1], arr[left_idx] = arr[left_idx], arr[right_part_idx - 1]
    return right_part_idx - 1


comparisons_count = 0


def quick_sort(arr, left_idx=None, right_idx=None):
    if left_idx is None and right_idx is None:
        left_idx, right_idx = 0, len(arr) - 1

    if right_idx - left_idx < 1:
        return arr

    pivot_idx = get_left_pivot_idx(arr, left_idx, right_idx)

    pivot_idx = partition(arr, left_idx, right_idx, pivot_idx)

    # data for coursera assignments
    global comparisons_count
    comparisons_count += right_idx - left_idx

    quick_sort(arr, left_idx, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, right_idx)
    return arr


if __name__ == "__main__":
    # print([1, 3, 5, 2, 4, 6])
    # print(quick_sort([1, 3, 5, 2, 4, 6]))
    if len(sys.argv) < 2:
        SORT_ERR_MSG = "%s: Array expected to be sorted"
        for arr in (
            [1, 3, 5, 2, 4, 6],
            [5, 9, 7, 4, 6, 3],
            [6, 5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5, 6],
            [1, 5, 5, 5, 5, 2],
            [0, 1],
            [0],
            [],
        ):
            sorted_arr = quick_sort(arr)
            assert sorted_arr == sorted(arr), SORT_ERR_MSG % arr
    elif len(sys.argv) == 2:
        f = open(sys.argv[1])
        arr = list(map(int, f.readlines()))
        sorted_arr = quick_sort(arr)
        print("Array size: %s. Comparisons count: %d" % (len(arr), comparisons_count))
    else:
        print("Wrong arguments. Usage:\n 'python quick_sort.py ints_array.txt'")
