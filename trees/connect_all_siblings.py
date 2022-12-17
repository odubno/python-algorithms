"""
Given the root to a binary tree where each node has an additional pointer called
sibling (or next), connect the sibling pointer to the next node in the same level.
The last node in each level should point to the first node of the next level in
the tree.
"""

import implementation_of_binary_tree as bt
from collections import deque


def populate_sibling_pointers(root: bt.BinaryTreeNode) -> bt.BinaryTreeNode:
    # maintain a queue and track previous pointer
    queue = deque()

    # add the root node to the queue
    queue.append(root)

    # set previous node to the first root node
    prev = root

    while queue:
        curr_node = queue.popleft()

        prev.next = curr_node
        prev = curr_node

        curr_node.next = curr_node
        # set next to left first
        if curr_node.left:
            queue.append(curr_node.left)

        # set next to right last
        if curr_node.right:
            queue.append(curr_node.right)

    prev.next = None

    return root


def main():
    arr = [100, 50, 200, 25, 75, 300, 350]
    root = bt.create_BST(arr)
    _ = populate_sibling_pointers(root)
    while root.next:
        print(root.data, end=" ")
        root = root.next

main()