"""
Given a binary tree and a node, find the level order successor of the
given node in the tree. The level order successor is the node that appears
right after the given node in the level order traversal.
"""

from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_successor(root: TreeNode, key: int) -> int:
    # traverse using BFS
    # once the key is found, grab the next node in the queue and break out of the loop
    # use a queue to keep track of yet to visit nodes
    queue = deque()
    queue.append(root)
    # use bool to find key
    key_found = False
    while queue:
        level_length = len(queue)
        for _ in range(level_length):
            curr_node = queue.popleft()

            # if prev key was found grab the value of the next available node
            if key_found:
                return curr_node.val

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

            if key == curr_node.val:
                key_found = True

    return 0


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    assert find_successor(root, 12) == 7
    assert find_successor(root, 9) == 10


main()
