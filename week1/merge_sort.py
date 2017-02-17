def merge_parts(left_arr, right_arr):
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
    return res


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = len(arr) // 2
    left_part = arr[:pivot]
    right_part = arr[pivot:]

    sorted_left_part = merge_sort(left_part)
    sorted_right_part = merge_sort(right_part)
    return merge_parts(sorted_left_part, sorted_right_part)


if __name__ == "__main__":
    ERR_MSG = "Expected %s to be sorted"
    for arr in (
        [1, 5, 6, 2, 3, 4],
        [6, 5, 4, 3, 2, 1],
        [10, -1],
        [0],
        []
    ):
        assert merge_sort(arr) == sorted(arr), ERR_MSG % arr
