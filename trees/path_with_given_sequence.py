"""
Given a binary tree and a number sequence, find if the sequence is present as a
root-to-leaf path in the given tree.
"""
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path_rec(root: TreeNode, desired_sequence: List, current_sequence=None):
    if not root:
        return False

    if current_sequence is None:
        current_sequence = []

    # continue to append value to current_sequence
    current_sequence.append(root.val)

    # if length of current_sequence exceeds the length of desired sequence,
    # then reset the current_sequence object
    if len(current_sequence) > len(desired_sequence):
        # reset current_sequence, always keeping the main root, and current root
        # b/c we're not revisiting the main root again, but still need it
        current_sequence = [current_sequence[0], root.val]

    # check if any children exist
    if not root.left and not root.right:

        # check if desired matches current sequence
        sequences_match = desired_sequence == current_sequence

        # if sequences don't match, keep going
        return sequences_match

    # go down the left side first
    return find_path_rec(root.left, desired_sequence, current_sequence) or find_path_rec(root.right, desired_sequence, current_sequence)


def find_path(root, sequence):
    """
    1. Use DFS
    2. for each node val track a single sequence as `curr_sequence`
    3. when node has no children check the `curr_sequence` against `desired_sequence`
    4. if there is a match return True, if not, reset `curr_sequence` list and continue
    """
    # result = find_path_recursive(root, sequence)
    return find_path_rec(root, sequence)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
