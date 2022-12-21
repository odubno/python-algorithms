"""
Given a binary tree and a number ‘S’, find all paths in the tree such that the
sum of all the node values of each path equals ‘S’. Please note that the paths
can start or end at any node but all paths must follow direction from parent to
child (top to bottom).

revist
"""


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        return 0

    # add the current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    # find the sums of all sub-paths in the current path list
    # reverse list up to zero index hence `range(3, -1, -1)` -> `[3, 2, 1, 0]`
    # this is to help work backwards
    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]
    # if the sum of any sub-path is equal to 'S' we increment our path count.
    if pathSum == S:
        pathCount += 1

    # traverse the left sub-tree
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    # traverse the right sub-tree
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currentPath[-1]

    return pathCount


def get_path_count(current_nodes, desired_node_sum, path_count):
    for index in range(len(current_nodes)):
        temp_sum = sum(current_nodes[index:])
        if temp_sum == desired_node_sum:
            path_count += 1
        if temp_sum < desired_node_sum:
            # break early, since sum is unlikely to be close to desired sum as we keep removing numbers
            break
    return path_count


def count_paths_rec(root, desired_node_sum, current_nodes=None):
    if not root:
        return 0

    if current_nodes is None:
        current_nodes = []

    current_nodes.append(root.val)
    path_count = 0
    if sum(current_nodes) == desired_node_sum:
        path_count += 1
    elif sum(current_nodes) > desired_node_sum:
        # if sum of current_nodes is greater check the sum by removing top most values
        # check sum of all nodes until sum is below desired_node_sum
        path_count += get_path_count(current_nodes, desired_node_sum, path_count)

    # start with left side
    path_count += count_paths_rec(root.left, desired_node_sum, current_nodes)
    # proceed with the right
    path_count += count_paths_rec(root.right, desired_node_sum, current_nodes)

    # pop recently visited values as we move back up the tree
    # Remove the current node from the current path before returning.
    # This is needed to Backtrack while going up the recursive call stack
    # to process other paths
    current_nodes.pop()

    return path_count


def count_paths(root, desired_node_sum):
    """
    1. Use DFS
    2. Track and store root values in a list current_nodes
    3. Check if the sum of current_nodes matches desired_node_sum
        1. increment result counter
        2. reset current_nodes to an empty list
    4. Check if sum of current_nodes exceeds desired_node_sum
        1. also check if children exist
        2. reset the current_nodes to an empty list
    5. remember to track initial root node val
    """
    r = count_paths_rec(root, desired_node_sum)
    return r


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))

    root2 = TreeNode(1)
    root2.left = TreeNode(7)
    root2.right = TreeNode(9)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(2)
    root2.right.right = TreeNode(3)
    print("Tree has paths: " + str(count_paths(root2, 12)))

    root3 = TreeNode(1)
    root3.left = TreeNode(7)
    root3.right = TreeNode(9)
    root3.left.left = TreeNode(6)
    root3.left.right = TreeNode(5)
    root3.left.left.left = TreeNode(6)
    root3.left.left.right = TreeNode(3)
    root3.right.left = TreeNode(2)
    root3.right.right = TreeNode(3)
    root3.right.left.left = TreeNode(2)

    assert count_paths(root3, 12) == 4



main()
