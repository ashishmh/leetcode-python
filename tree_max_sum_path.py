import sys

# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.maxSum = -sys.maxsize
    self.calculatePathSum(root)
    return self.maxSum


def calculatePathSum(self, root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if root.val > self.maxSum:
            self.maxSum = root.val
        return root.val
    
    leftPathSum = self.calculatePathSum(root.left)
    rightPathSum = self.calculatePathSum(root.right)
    
    sum = root.val
    if leftPathSum > 0:
        sum += leftPathSum
    if rightPathSum > 0:
        sum += rightPathSum
    self.maxSum = max(self.maxSum, sum)
    return max(root.val, root.val + max(leftPathSum, rightPathSum))


def main():
	str = input('input: ')
	output = function(str)
	print('output: ', output)


if __name__ == '__main__':
    main()