"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes
along the shortest path from the root node to the nearest leaf node.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    """
    1. use a variable minimum to track lowest value
    2. use bfs to travers the tree and track the minimum depth level
    3. if a node does not have any children record that depth level
    4. use a queue to track unvisited nodes
    5. use length of queue to determine depth
    """

    queue = deque()
    queue.append(root)
    minimum_depth = 1

    while queue:  # [12, 7, 1]
        level_length = len(queue)  # 1, 2, 2

        for _ in range(level_length):
            curr_node = queue.popleft()  # 12, 7, 1

            if not curr_node.left and not curr_node.right:
                return minimum_depth

            if curr_node.left:
                queue.append(curr_node.left)  # 7, 9, 10
            if curr_node.right:
                queue.append(curr_node.right)  # 1, 5

        minimum_depth += 1

    return minimum_depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
