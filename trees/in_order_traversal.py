import implementation_of_binary_tree as bt
from typing import List

"""
The runtime complexity of this solution is linear, O(n).
The memory complexity of this solution is O(h).
"""

def populate_stack(stack: List, root: bt.BinaryTreeNode) -> List[bt.BinaryTreeNode]:
    temp_root = root
    while temp_root is not None:
        stack.append(temp_root)
        temp_root = temp_root.left
    return stack


def inorder_iterative(root: bt.BinaryTreeNode) -> List[bt.BinaryTreeNode]:
    # 1. create a stack to store nodes of left most nodes
    # 2. scan the left most nodes until node has no left children
    #   1. store nodes in stack while searching
    # 3. check if a right node for the last node exists if it does
    #   then call the same populate of left nodes function on this node and keep going
    result = []
    stack = []
    stack = populate_stack(stack, root)
    while stack:
        right_value = stack.pop()
        result.append(right_value.data)
        populate_stack(stack, right_value.right)
    return result


arr = [100,50,200,25,75,35]
root = bt.create_BST(arr)
print(inorder_iterative(root))
