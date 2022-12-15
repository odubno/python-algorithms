"""
Given a binary tree, populate an array to represent its level-by-level traversal
in reverse order, i.e., the lowest level comes first. You should populate the
values of all nodes in each level from left to right in separate sub-arrays.

input: [100, 50, 200, 25, 75, 350]
output: [[25, 27, 350], [50, 200], [100]]
"""

import implementation_of_binary_tree as bt
from collections import deque


def traverse(root: bt.BinaryTreeNode):
    result = deque()

    if root is None:
        return result

    # create an empty queue to track yet to be visited nodes
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        # visit all the nodes by level of the tree
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the node to the current level
            current_level.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.appendleft(current_level)

    return result


arr = [100, 50, 200, 25, 75, 350]
root = bt.create_BST(arr)
print(traverse(root))