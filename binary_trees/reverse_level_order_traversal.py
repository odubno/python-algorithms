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
    # store results in a queue to make it easier to
    # prepend values to the beginning of the object
    result = deque()

    # use queue to track nodes to visit
    queue = deque()
    queue.append(root)

    while queue:
        # use length of queue to visit all the nodes for any one level
        level_length = len(queue)
        level_node_values = []
        for _ in range(level_length):

            # pop off the left most value in the queue
            # and check add its children nodes to the queue
            temp_node = queue.popleft()
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)

            level_node_values.append(temp_node.data)

        result.appendleft(level_node_values)

    return result


arr = [100, 50, 200, 25, 75, 350]
root = bt.create_bst(arr)
print(traverse(root))