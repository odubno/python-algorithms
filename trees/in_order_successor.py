"""
The in-order successor of a node in a binary Search Tree (BST) is the next node
in in-order traversal. Write a method to find the in-order successor of a given
value “d” in a BST.
"""
import implementation_of_binary_tree as bt
from typing import Optional


def inorder_successor_bst(
        root: bt.BinaryTreeNode,
        d: int,
        minimum: Optional[bt.BinaryTreeNode] = None
    ):
    # traverse tree and find value d in the tree
    # traverse the left most nodes
    # if node matching value d has a right child node, then the left child node will be the successor
    # if d has no right child then:
    #   track int value that's just smaller than d
    #   return this node as the successor
    if minimum is None:
        minimum = root

    if root.data == d:
        if root.right is not None:
            return root.right
        elif minimum.data > d:
            return minimum
        else:
            return bt.BinaryTreeNode(None)
    elif root.data > d:
        temp_root = root.left
    else:
        temp_root = root.right

    if root.data > d:
        minimum = root

    return inorder_successor_bst(temp_root, d, minimum)


arr = [100, 50, 200, 25, 75, 125, 350]
root = bt.create_BST(arr)
for val in arr:
    successor = inorder_successor_bst(root, val).data
    if not successor:
        print(f"In-order successor of {val} is NULL since it is the last node")
    else:
        print(f"In-order successor of {val} is {successor}")
