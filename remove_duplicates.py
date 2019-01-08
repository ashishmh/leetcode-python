import sys

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return n

    currEle = nums[0]
    count = 1
    i = 1
    while i < n:
        if nums[i] == currEle:
            del nums[i]
            n = len(nums)
        else:
            currEle = nums[i]
            count += 1
            i += 1
    return count


def main():
    str = input('input: ')
    output = removeDuplicates(str.split())
    print('output: ', output)


if __name__ == '__main__':
    main()