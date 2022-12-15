"""
Given a binary tree, populate an array to represent the averages of all of its
levels.

input: [100, 50, 200, 25, 75, 350]
output: [100.0, 125.0, 150.0]
"""

import implementation_of_binary_tree as bt
from collections import deque


def find_level_averages(root: bt.BinaryTreeNode):
    # use breadth for search
    # use a queue to keep track of all nodes at each level
    # before moving on to the next level, take the average and add to result
    result = []

    queue = deque()
    queue.append(root)

    while queue:  # 1, 2

        level_length = len(queue)  # 1, 2
        level_nodes = []
        for _ in range(level_length):

            # we want to track left most nodes first to maintain order
            curr_node = queue.popleft()  # 100, 50

            if curr_node.left:
                queue.append(curr_node.left)  # 50, 25
            if curr_node.right:
                queue.append(curr_node.right)  # 200, 75

            level_nodes.append(curr_node.data)  # 100

        level_average = sum(level_nodes)/float(len(level_nodes))  # 100
        result.append(level_average)

    return result


arr = [100, 50, 200, 25, 75, 350]
root = bt.create_BST(arr)
print(find_level_averages(root))

"""
Time complexity
The time complexity of the above algorithm is O(N), where ‘N’ is the total
number of nodes in the tree. This is due to the fact that we traverse each
node once.

Space complexity
The space complexity of the above algorithm will be O(N) which is required for the queue.
Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest level),
therefore we will need O(N) space to store them in the queue.
"""