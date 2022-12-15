"""
Given the root of a binary tree, display the node values at each level.
Node values for all levels should be displayed on separate lines. Let’s
take a look at the below binary tree.

input: [100, 50, 200, 25, 75, 125, 350]
output:
100
50,200
25,75,350
"""

import implementation_of_binary_tree as bt


def get_max_height(node: bt.BinaryTreeNode) -> int:
    if node is None:
        return 0

    left_height = get_max_height(node.left)
    right_height = get_max_height(node.right)

    # Return the larger height
    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


# get nodes at a specific level
def get_h_level_order(root, level):
    if root is None:
        return None

    if level == 0:
        # using `end=" "` will help keep print to a single line
        print(root.data, end=" ")

    get_h_level_order(root.left, level-1)
    get_h_level_order(root.right, level-1)


def level_order_traversal(root: bt.BinaryTreeNode):
    height = get_max_height(root)
    result = ""
    for level in range(height+1):
        get_h_level_order(root, level)
        print()


def level_order_traversal_2(root: bt.BinaryTreeNode) -> str:
    # use breadth for search
    # use two queues: current_queue and next_queue
    # nodes will be pushed to queue determined by current level
    # nodes will be dequeued from the current_queue and enqueue child nodes to next_queue
    # once current_queue is empty, all nodes were processed for current level_number
    # to indicate a new level, \n will be added to string
    # swap the two queues and continue
    current_queue = [root]
    result = ""
    next_queue = []
    current_level = 0
    while current_queue:
        current_node = current_queue.pop(0)
        result += str(current_node.data)
        if not current_queue and not next_queue:
            result += '\n'

        if current_node.left:
            next_queue.append(current_node.left)
        if current_node.right:
            next_queue.append(current_node.right)

        if next_queue:
            current_queue.extend(next_queue)
            next_queue = []

    return result



arr = [100, 50, 200, 25, 75, 350]
root = bt.create_BST(arr)
# print(get_max_height(root))
print(level_order_traversal(root))


