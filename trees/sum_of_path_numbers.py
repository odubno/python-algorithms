"""
Given a binary tree where each node can only have a digit (0-9) value,
each root-to-leaf path will represent a number. Find the total sum of all the
numbers represented by all paths.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers_rec(root, path_sum=None, results=None):
    if not root:
        return results

    if path_sum is None:
        path_sum = ''

    if results is None:
        # use list to store all string results
        results = []

    # track each node value
    path_sum += str(root.val)

    if not root.left and not root.right:
        results.append(int(path_sum))
        # reset path_sum but the root i.e. first index should always be the same
        path_sum = path_sum[0]

    find_sum_of_path_numbers_rec(root.left, path_sum, results)
    find_sum_of_path_numbers_rec(root.right, path_sum, results)

    return results


def find_sum_of_path_numbers(root):
    """
    1. Use DFS to track each node
    2. append integers as strings to a path_sum variable until node has no children
    3. when node has no children:
        1. append path_sum string to a list of results
        2. reset path_sum variable
        3. continue
    2. return sum of results list
    """
    r = sum(find_sum_of_path_numbers_rec(root))
    return r


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
    assert find_sum_of_path_numbers(root) == 332

    root2 = TreeNode(1)
    root2.left = TreeNode(7)
    root2.right = TreeNode(9)
    root2.right.left = TreeNode(2)
    root2.right.right = TreeNode(9)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root2)))
    assert find_sum_of_path_numbers(root2) == 408


main()
