"""
We are given a Binary Search Tree(BST) and a node number n.
We have to find the node with the nth highest value.
"""
import implementation_of_binary_tree as bt


def find_nth_highest_in_bst(node, n, count=0):
    """
    In-order traversal of BST is always sorted in ascending order.
    To find the nth highest node, we will need to scan the tree in descending order by doing reverse in-order traversal.
    """
    if not node:
        return None

    count += 1

    if n == count:
        return node

    result = find_nth_highest_in_bst(node.right, n, count)
    if result:
        return result

    result = find_nth_highest_in_bst(node.left, n, count)
    if result:
        return result

    return None


arr = [100, 50, 200, 25, 60, 350, 10, 70, 400]
root = bt.create_BST(arr)

nth_highest_node = find_nth_highest_in_bst(root, 2)
assert nth_highest_node.data == 200

nth_highest_node = find_nth_highest_in_bst(root, 1)
assert nth_highest_node.data == 100

n = 5
nth_highest_node = find_nth_highest_in_bst(root, 5)
assert nth_highest_node is None

nth_highest_node = find_nth_highest_in_bst(root, 30)
assert nth_highest_node is None
