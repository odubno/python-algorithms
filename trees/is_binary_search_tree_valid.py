"""
Given a Binary Tree, figure out whether it’s a Binary Search Tree.
In a binary search tree, each node’s key value is smaller than the key
value of all nodes in the right subtree, and are greater than the key
values of all nodes in the left subtree i.e. L < N < R.
"""
import implementation_of_binary_tree as bt


def is_bst_recursive(root: bt.BinaryTreeNode, minimum, maximum):
    if not root:
        # we reached the end of the tree and did not find any fault
        return True

    # check if the tree is valid
    if root.data < minimum or root.data > maximum:
        return False

    return (
        is_bst_recursive(root.left, minimum, root.data) and
        is_bst_recursive(root.right, root.data, maximum)
    )


def is_bst(root: bt.BinaryTreeNode) -> bool:
    return is_bst_recursive(root, -float('inf'), float('inf'))


def main():
    arr = [100, 50, 200, 25, 75, 125, 350]
    valid_bst = bt.create_BST(arr)
    assert is_bst(valid_bst) is True

    invalid_bst = bt.BinaryTreeNode(100)
    invalid_bst.left = bt.BinaryTreeNode(50)
    invalid_bst.right = bt.BinaryTreeNode(200)
    invalid_bst.left.left = bt.BinaryTreeNode(25)
    invalid_bst.left.right = bt.BinaryTreeNode(110)
    invalid_bst.right.left = bt.BinaryTreeNode(150)
    invalid_bst.right.right = bt.BinaryTreeNode(350)

    assert is_bst(invalid_bst) is False


main()