import sys

# https://www.geeksforgeeks.org/bottom-view-binary-tree/

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def bottomView(root):
	if root is None:
		return
	state = dict()
	inorderModified(root, 0, state)
	print('\nbottom view: ', state)


def inorderModified(root, vlevel, state):
	if root is None:
		return

	inorderModified(root.left, vlevel - 1, state)
	# logic for processing node
	state[vlevel] = root.val
	inorderModified(root.right, vlevel + 1, state)


def inorder(root):
	if root is None:
		return

	inorder(root.left)
	print(root.val, end=(' '))
	inorder(root.right)


def main():
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.left.right.left = TreeNode(8)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(7)
	root.right.right.right = TreeNode(9)
	
	print('inorder: ', end='\n')
	inorder(root)
	output = bottomView(root)
	print('output: ', output)


if __name__ == '__main__':
    main()