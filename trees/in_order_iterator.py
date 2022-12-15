"""
Implement a class that implements an in-order iterator on a Binary Tree.

We are given the root node of a binary tree. We have to write an iterator
that takes in this root and iterates through the nodes of a binary tree in an
in-order way. The expectation is to write two critical methods of any iterator:
hasNext() and getNext(). Consider the following binary tree:
"""
import implementation_of_binary_tree as bt
from typing import Optional, List


class InOrderIterator:

    def __init__(self, root: bt.BinaryTreeNode):
        # use stack to maintain state
        # stack contains the next element at the top to return on getNext()
        self.stack = []
        # add left most nodes of tree to stack
        self.populate_iterator(root)

    def populate_iterator(self, root: bt.BinaryTreeNode) -> None:
        while root is not None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        if not self.stack:
            return False
        else:
            return True

    def getNext(self) -> Optional[bt.BinaryTreeNode]:
        if not self.stack:
            return None
        right_value = self.stack.pop()
        # if right child is not null, leftmost nodes will be added to stack
        temp = right_value.right
        self.populate_iterator(temp)
        return right_value


def inorder_using_iterator(root) -> List[int]:
    iterator = InOrderIterator(root)
    result = []
    while iterator.hasNext():
        ptr = iterator.getNext()
        result.append(ptr.data)
    return result


arr1 = [100, 50, 200, 25, 75, 125, 350]
root = bt.create_BST(arr1)
assert str(inorder_using_iterator(root)) == str([25, 50, 75, 100, 125, 200, 350])

arr2 = [25, 125, 200, 300, 75, 50, 12, 35, 60, 75]
root = bt.create_BST(arr2)
assert str(inorder_using_iterator(root)) == str([12, 25, 35, 50, 60, 75, 75, 125, 200, 300])
