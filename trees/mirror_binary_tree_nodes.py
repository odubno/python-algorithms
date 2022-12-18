"""
Given the root node of a binary tree, swap the ‘left’ and ‘right’ children for
each node. The below example shows how the mirrored binary tree should look like.
"""
import implementation_of_binary_tree as bt
from collections import deque
from typing import Optional


def mirror_tree(root: bt.BinaryTreeNode) -> Optional[bt.BinaryTreeNode]:
    """
    1. Use DFS
    2. Initialize new BinaryTreeNode
    3. when traversing the left side of tree and nodes to the right side of the new initialized tree
    """
    if not root:
        return None

    # initialize next node
    mirror_root = bt.BinaryTreeNode(root.data)

    # for each node flip values
    mirror_root.right = mirror_tree(root.left)
    mirror_root.left = mirror_tree(root.right)

    return mirror_root


def main():
    arr = [100, 50, 200, 75, 25, 300]
    root = bt.create_BST(arr)

    bt.display_level_order(root)
    mirrored_tree = mirror_tree(root)
    print("\nMirrored Level Order Traversal:")
    bt.display_level_order(mirrored_tree)


main()
