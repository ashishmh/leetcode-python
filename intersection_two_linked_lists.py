import sys

# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# O(n+m) solution
def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
            return None

    ptrA = headA
    ptrB = headB
    for i in range(0, 3):
        while ptrA is not None and ptrB is not None:
            if ptrA is ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        if i < 2:
            if ptrA is None:
                ptrA = headB
            if ptrB is None:
                ptrB = headA
    return None


def createList(arr):
    n = len(arr)
    if n == 0:
        return None
    head = ListNode(arr[0])
    currNode = head
    for i in range(1, n):
        newNode = ListNode(arr[i])
        currNode.next = newNode
        currNode = newNode
    return head


def printList(head):
    if head is None:
        return
    print('list -> ', end='')
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print('')


def main():
    str1 = input('list 1: ').split()
    str2 = input('list 2: ').split()

    list1 = createList(str1)
    list2 = createList(str2)
    # write helper function to connect 2 lists at a node
    # output = getIntersectionNode(list1, list2)
    print('output: ', output)


if __name__ == '__main__':
    main()