import sys

# https://leetcode.com/problems/add-two-numbers/

class ListNode():
	def __init__(self, val):
		self.val = val
		self.next = None


def addTwoNumbers(l1, l2):
	if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    resultPtr = None
    result = None
    carry = 0
    while (l1 is not None and l2 is not None):
        sum = l1.val + l2.val + carry
        if sum > 9:
            carry = 1
            sum = sum % 10
        else:
            carry = 0
        if resultPtr is None:
            resultPtr = ListNode(sum)
            result = resultPtr
        else:
            resultPtr.next = ListNode(sum)
            resultPtr = resultPtr.next
        l1 = l1.next
        l2 = l2.next
    while l1 is not None:
        sum = l1.val + carry
        if sum > 9:
            carry = 1
            sum = sum % 10
        else:
            carry = 0
        resultPtr.next = ListNode(sum)
        resultPtr = resultPtr.next
        l1 = l1.next
    while l2 is not None:
        sum = l2.val + carry
        if sum > 9:
            carry = 1
            sum = sum % 10
        else:
            carry = 0
        resultPtr.next = ListNode(sum)
        resultPtr = resultPtr.next
        l2 = l2.next
    if carry != 0:
        resultPtr.next = ListNode(carry)
    
    return result

	
def main():
	str = input('input: ')
	output = addTwoNumbers()
	print('output: ', output)


if __name__ == '__main__':
    main()