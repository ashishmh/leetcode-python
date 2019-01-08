import sys

# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def buildTree(self, inorder, postorder):
	"""
	:type inorder: List[int]
	:type postorder: List[int]
	:rtype: TreeNode
	"""
	if len(inorder) == 0 or len(postorder) == 0:
		return None

	n = len(postorder) - 1
	root = TreeNode(postorder[n])
	rIdx = inorder.index(root.val)
	x = n - rIdx
	root.left = self.buildTree(inorder[0:rIdx], postorder[0:rIdx])
	root.right = self.buildTree(inorder[rIdx+1:rIdx+1+x], postorder[rIdx:rIdx+x])
	return root


def main():
	str = input('input: ')
	output = function(str)
	print('output: ', output)


if __name__ == '__main__':
    main()