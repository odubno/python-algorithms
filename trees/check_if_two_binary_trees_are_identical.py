"""
Given the roots of two binary trees, determine if these trees are identical
or not. Identical trees have the same layout and data at each node. Consider
the following two identical binary trees that have the same layout and data.
"""
import implementation_of_binary_tree as bt


def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return False

    if root1 is not None and root2 is not None:
        roots_are_same = root1.data == root2.data
        left_roots_are_same = are_identical(root1.left, root2.left)
        right_roots_are_same = are_identical(root1.right, root2.right)
        return roots_are_same and left_roots_are_same and right_roots_are_same

    return False


arr1 = [100, 50, 200, 25, 125, 350]
arr2 = [1, 2, 10, 50, 180, 199]
root1 = bt.create_BST(arr1)
root2 = bt.create_BST(arr2)
assert not are_identical(root1, root2), "trees are not identical"

arr3 = [100, 50, 200, 25, 125, 350]
root3 = bt.create_BST(arr3)
assert not are_identical(root3, root3), "trees are identical"
