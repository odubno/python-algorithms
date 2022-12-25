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
        # stack to store nodes
        self.stack = []
        self.populate_stack(root)

    def populate_stack(self, root):
        # function to add left most nodes of root to stack
        temp_root = root
        while temp_root is not None:
            self.stack.append(temp_root)
            temp_root = temp_root.left

    def has_next(self) -> bool:
        if self.stack:
            return True
        else:
            return False

    def get_next(self) -> Optional[bt.BinaryTreeNode]:
        # update stack, by checking whether current node has children on the right side
        # if there are nodes on the right add it to populate_stack()
        # pop the right most value from the stack
        if not self.stack:
            return None
        right_value = self.stack.pop()
        self.populate_stack(right_value.right)
        return right_value


def inorder_using_iterator(root) -> List[int]:
    iterator = InOrderIterator(root)
    result = []
    while iterator.has_next():
        ptr = iterator.get_next()
        result.append(ptr.data)
    return result


arr1 = [100, 50, 200, 25, 75, 125, 350]
root = bt.create_bst(arr1)
assert str(inorder_using_iterator(root)) == str([25, 50, 75, 100, 125, 200, 350])

arr2 = [25, 125, 200, 300, 75, 50, 12, 35, 60, 75]
root = bt.create_bst(arr2)
assert str(inorder_using_iterator(root)) == str([12, 25, 35, 50, 60, 75, 75, 125, 200, 300])
