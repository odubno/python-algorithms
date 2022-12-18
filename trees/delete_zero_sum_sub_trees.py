"""
Given the root of a binary tree, delete any subtrees whose nodes sum up to zero.
In the below binary tree, we need to delete the subtree starting at node 5
as it’s sum (5 -3 -2) equals zero.

revisit
"""

import implementation_of_binary_tree as bt


def delete_zero_sum_subtree(root: bt.BinaryTreeNode):
    if not root:
        return 0

    # Traverse the left subtree by recursively calling the post-order function.
    sum_left = delete_zero_sum_subtree(root.left)

    # Traverse the right subtree by recursively calling the post-order function.
    sum_right = delete_zero_sum_subtree(root.right)

    if sum_left == 0:
        # if left subtree reports zero sum delete that subtree
        root.left = None

    if sum_right == 0:
        # if right subtree reports zero sum delete that subtree
        root.right = None

    # return sum of the subtree
    return sum([root.data, sum_left, sum_right])


def main():
    data = [7, 5, 9, -3, -2]
    root = bt.create_BST(data)
    delete_zero_sum_subtree(root)
    assert bt.bst_to_list(root) == [7, 9]


main()
