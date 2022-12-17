"""
Given the root node of a binary tree, print the nodes that form the boundary
(perimeter).

In the following tree, the highlighted nodes form the perimeter.
The expected output for the below tree would be
100, 50, 25, 10, 70, 400, 350, 200
"""
import implementation_of_binary_tree as bt
from collections import deque


def get_left_perimeter(root: bt.BinaryTreeNode, result=None):
    if result is None:
        result = []

    if not root:
        return result

    if root.left:
        result.append(root.data)
        get_left_perimeter(root.left, result)

    return result


def get_right_perimeter(root: bt.BinaryTreeNode, result=None):
    if result is None:
        result = deque()

    if not root:
        return list(result)

    if root.right:
        result.appendleft(root.data)
        get_right_perimeter(root.right, result)

    return list(result)[:-1]


def get_lower_perimeter(root: bt.BinaryTreeNode, result=None):
    if result is None:
        result = []

    if not root:
        return result

    if root.left:
        get_lower_perimeter(root.left, result)
    if root.right:
        get_lower_perimeter(root.right, result)

    if not root.left and not root.right:
        result.append(root.data)

    return result


def display_tree_perimeter(root):
    # Use DFS to traverse the left most side of the tree
    # store all the values in a list beginning with the root node value and down
    # traverse the right most side of the tree, use a queue to store value in reverse
    # during the DFS traversal if any nodes do not have children store value as bottom most nodes
    # merge left, bottom and right sides of the tree
    left = get_left_perimeter(root)
    right = get_right_perimeter(root)
    bottom = get_lower_perimeter(root)
    return left + bottom + right


def main():
    arr = [100, 50, 200, 25, 60, 350, 10, 70, 400]
    root = bt.create_BST(arr)
    print("\nPrint tree perimeter\n")
    print(display_tree_perimeter(root))


main()
