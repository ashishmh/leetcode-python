import sys

# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    result = None
    resultPtr = None
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp = l1
            l1 = l1.next
            if result is None:
                resultPtr = temp
                result = resultPtr
            else:
                resultPtr.next = temp
                resultPtr = resultPtr.next
        else:
            temp = l2
            l2 = l2.next
            if result is None:
                resultPtr = temp
                result = resultPtr
            else:
                resultPtr.next = temp
                resultPtr = resultPtr.next
    while l1 is not None:
        temp = l1
        l1 = l1.next
        resultPtr.next = temp
        resultPtr = resultPtr.next
    while l2 is not None:
        temp = l2
        l2 = l2.next
        resultPtr.next = temp
        resultPtr = resultPtr.next

    return result


def main():
    str = input('input: ')
    output = mergeTwoLists()
    print('output: ', output)


if __name__ == '__main__':
    main()