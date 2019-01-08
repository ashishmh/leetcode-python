import sys

# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    result = binarySearch(nums, 0, len(nums)-1, target)
    return result
        
        
def binarySearch(arr, l, r, x):
    if l > r:
        return -1
    m = int((l + r) / 2)
    if arr[m] == x:
        return m
    
    if arr[m] < arr[r]:                             # right half is sorted
        if x >= arr[m] and x <= arr[r]:             # eligible, go right
            return binarySearch(arr, m + 1, r, x)
        else:                                       # not eligible, go left
            return binarySearch(arr, l, m - 1, x)
    elif x >= arr[l] and x <= arr[m]:               # left half is sorted
        return binarySearch(arr, l, m - 1, x)       # eligible, go left
    else:
        return binarySearch(arr, m + 1, r, x)       # not eligible, go right (unsorted)


def main():
	str = input('list: ')
	nums = list(map(int, str.split(',')))
	str = input('target: ')
	target = int(str)
	output = search(nums, target)
	print('output: ', output)


if __name__ == '__main__':
    main()