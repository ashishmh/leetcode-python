import sys

# https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def diameterOfBinaryTree(self, root):
	"""
	:type root: TreeNode
	:rtype: int
	"""
	self.maxPathLen = 0
	self.findMaxPaths(root)
	return self.maxPathLen
        
    
def findMaxPaths(self, root):
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return 0
	leftLen = 0
	if root.left is not None:
		leftLen = self.findMaxPaths(root.left) + 1
	rightLen = 0
	if root.right is not None:
		rightLen = self.findMaxPaths(root.right) + 1
	if leftLen + rightLen > self.maxPathLen:
		self.maxPathLen = leftLen + rightLen
	return max(leftLen, rightLen)


def main():
	str = input('input: ')
	output = function(str)
	print('output: ', output)


if __name__ == '__main__':
    main()