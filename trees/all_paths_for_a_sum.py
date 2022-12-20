"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such
that the sum of all the node values of each path equals ‘S’.
revist
"""


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
    """
    We can follow the DFS approach. There will be two differences:
    1. Every time we find a root-to-leaf path, we will store it in a list.
    2. We will traverse all paths and will not stop processing after finding the first path.
    """
    if currentNode is None:
        return

    # add the current node to the path
    currentPath.append(currentNode.data)

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if currentNode.data == required_sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(currentNode.left, required_sum -
                             currentNode.data, currentPath, allPaths)
        # traverse the right sub-tree
        find_paths_recursive(currentNode.right, required_sum -
                             currentNode.data, currentPath, allPaths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del currentPath[-1]


def find_paths_rec(root, path_sum, all_paths=None, one_path=None):
    if all_paths is None:
        all_paths = []
    if one_path is None:
        one_path = []
    if root is None:
        return all_paths

    sum_of_one_path_before_addition = sum(one_path)
    if sum_of_one_path_before_addition < path_sum:
        one_path.append(root.data)
    elif sum_of_one_path_before_addition >= path_sum:
        # reset the path if previous path sum has been found
        # one_path[0] is the original root
        one_path = [one_path[0], root.data]

    sum_of_one_path_after_addition = sum(one_path)
    if sum_of_one_path_after_addition == path_sum:
        all_paths.append(one_path)

    # traverse left most tree
    find_paths_rec(root.left, path_sum, all_paths, one_path)
    find_paths_rec(root.right, path_sum, all_paths, one_path)

    return all_paths


def find_paths(root, required_sum):
    """
    1. Use DFS to check the sum of paths originating from the root
    2. Continue searching until the sum of paths is equal to 'S'
    3. only append to all_paths if something is equal
    4. if path sum exceeds 'S' stop and search the other side of the tree
    """
    all_paths = []
    # update all_paths inplace
    find_paths_recursive(root, required_sum, [], all_paths)
    result = find_paths_rec(root, required_sum)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(9)
    root1.left.left = TreeNode(4)
    root1.right.left = TreeNode(5)
    root1.right.left = TreeNode(2)
    root1.right.right = TreeNode(7)
    print("Tree paths with sum " + str(12) +
        ": " + str(find_paths(root1, 12)))


main()