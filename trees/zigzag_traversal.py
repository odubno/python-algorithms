"""
Given a binary tree, populate an array to represent its zigzag level order
traversal. You should populate the values of all nodes of the first level from
left to right, then right to left for the next level and keep alternating in
the same manner for the following levels.
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root: TreeNode) -> List:
    # Use BFS
    # Use a boolean to track whether to go from left or right
    # use queue to track unvisited nodes
    # at each level collect all nodes and flip the boolean to append on the other side
    result = []

    queue = deque()
    queue.append(root)  # 12

    append_to_right = True

    while queue:  # 12 | 7, 1 |
        level_length = len(queue)  # 1 | 2
        level_node_values = deque()
        for _ in range(level_length):
            curr_node = queue.popleft()

            # alternate between popping values from either left or right
            if append_to_right:
                level_node_values.append(curr_node.val)
            else:
                level_node_values.appendleft(curr_node.val)

            # append child nodes to queue
            if curr_node.left:
                queue.append(curr_node.left)  # 7 | 9
            if curr_node.right:
                queue.append(curr_node.right)  # 1

        result.append(list(level_node_values))  # [[12], [7, 1]
        append_to_right = False

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
