import sys


def merge_and_count_inversion(left_arr, right_arr, inversions_count):
    li, ri, res = 0, 0, []
    for _ in range(len(left_arr) + len(right_arr)):
        if li == len(left_arr):
            res.extend(right_arr[ri:])
            break
        if ri == len(right_arr):
            res.extend(left_arr[li:])
            break

        if left_arr[li] <= right_arr[ri]:
            res.append(left_arr[li])
            li += 1
        else:
            res.append(right_arr[ri])
            ri += 1
            inversions_count += len(left_arr) - li  # count of items left in left part
    return res, inversions_count


def sort_and_count_inversions(arr, inv_count=0):
    if len(arr) < 2:
        return arr, inv_count

    pivot = len(arr) // 2
    left_part = arr[:pivot]
    right_part = arr[pivot:]

    sorted_left, left_inversions = sort_and_count_inversions(left_part)
    sorted_right, right_inversions = sort_and_count_inversions(right_part)
    inv_count += left_inversions + right_inversions
    return merge_and_count_inversion(sorted_left, sorted_right, inv_count)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        COUNT_ERR_MSG = "Testcase %s: Expected %d inversions, got %d."
        SORT_ERR_MSG = "Testcase %s: Array expected to be sorted"
        for arr, expected in (
            ([1, 3, 5, 2, 4, 6], 3),
            ([6, 5, 4, 3, 2, 1], 15),
            ([1, 2, 3, 4, 5, 6], 0),
            ([0], 0),
            ([], 0),
        ):
            sorted_arr, inversions = sort_and_count_inversions(arr)
            assert inversions == expected, COUNT_ERR_MSG % (arr, expected, inversions)
            assert sorted_arr == sorted(arr), SORT_ERR_MSG % arr
    elif len(sys.argv) == 2:
        f = open(sys.argv[1])
        arr = list(map(int, f.readlines()))
        _, inversions_count = sort_and_count_inversions(arr)
        print("Array size: %s. Inversions count: %d" % (len(arr), inversions_count))
    else:
        print("Wrong arguments. Usage:\n 'python inversion_count.py ints_array.txt'")
