import pprint

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(str(root.data), end=' ')
    inorder(root.right)


def inorderIterative(root):
    if root is None:
        return

    stack = []
    while len(stack) != 0 or root is not None: 
        while True:
            if root is None:
                break
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.data, end=' ')
        root = root.right


def main():
    print('hello world')
    root = Node(1, None, None)
    # root.left = Node(2, None, None)
    root.right = Node(3, None, None)
    # root.left.left = Node(4, None, None)
    # root.left.right = Node(5, None, None)
    root.right.left = Node(6, None, None)
    root.right.right = Node(7, None, None)
    
    print('inorder traversal:')
    inorder(root)
    print('\n\ninorder iterative traversal:')
    inorderIterative(root)


if __name__ == '__main__':
    main()