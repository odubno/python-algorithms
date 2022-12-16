"""
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to a null node.
"""

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root: TreeNode):
    # Use BFS to loop the tree
    # use queue to keep track of left most nodes
    # at each level record left most nodes as val.next
    # keep going
    if root is None:
        return
    queue = deque()
    queue.append(root)

    while queue:
        prev_node = None
        level_size = len(queue)

        # connect all nodes of this level
        for _ in range(level_size):
            curr_node = queue.popleft()

            if prev_node:
                prev_node.next = curr_node
            prev_node = curr_node

            # insert the children of current node in the queue
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
