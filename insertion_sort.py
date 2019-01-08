import sys
import pprint


def insertion_sort(l):
    ops = 0
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            ops += 1
            if l[j] < l[j-1]:
                temp = l[j-1]
                l[j-1] = l[j]
                l[j] = temp
            else:
                break
    print("insertion sort: ", l)
    # try printing ops with and without else part
    print("ops: ", ops)


def merge_sort(arr, l, r):
    if l >= r:
        return
    # while l < r:
    mid = (l + r) / 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, mid + 1, r)


def merge(arr, l1, r1, l2, r2):
    # print("merge called...")
    # print("with arr: ", arr)
    # print("and indexes: ", l1, r1, l2, r2)
    l_size = r1 - l1 + 1
    r_size = r2 - l2 + 1
    left = [None] * l_size
    for i, j in zip(range(l1, r1 + 1), range(0, l_size)):
        left[j] = arr[i]
    right = [None] * r_size
    for i, j in zip(range(l2, r2 + 1), range(0, r_size)):
        right[j] = arr[i]
    i = 0
    j = 0
    k = 0
    while i < l_size and j < r_size:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < l_size:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < r_size:
        arr[k] = right[j]
        j += 1
        k += 1
    # print("after merging: ", arr)
    # sys.exit(0)


def main():
    l = [5, 1, 8, 3, 4, 2, 10, 7, 13, 6, 21, 1]
    print("input: ", l)
    # insertion_sort(l[:])
    merge_sort(l, 0, len(l) - 1)
    print("merge sort: ", l)


if __name__ == "__main__":
    main()