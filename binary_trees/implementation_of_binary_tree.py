# Implementation of BinaryTreeNode Class
from typing import List, Optional

"""
input: [100, 50, 200, 25, 125, 350]
output: 
                100
                /  \ 
               50   200
              /     /  \ 
            25     125  350
"""


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: int):
        # recursively and inplace insert the new value in the tree
        if data < self.data:
            if self.left:
                # if we still need to move towards the left subtree
                self.left.insert(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                # if we still need to move towards the right subtree
                self.right.insert(data)
            else:
                self.right = BinaryTreeNode(data)


def create_bst(arr: List) -> BinaryTreeNode:
    root = BinaryTreeNode(arr[0])
    for data in arr[1:]:
        root.insert(data)
    return root


# arr1 = [100, 50, 200, 25, 125, 350]
# bst = create_bst(arr1)
