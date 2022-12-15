# Implementation of BinaryTreeNode Class
import random
from collections import deque
from typing import Optional


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        self.next = None
        self.parent = None
        self.count = None


# Implementation of BinaryTree helper functions
def insert(root: Optional[BinaryTreeNode], data: int) -> BinaryTreeNode:
    new_parent = BinaryTreeNode(data)
    if root is None:
        # this means there are no parents for the data
        return new_parent

    # determine which parent to insert value under
    # traverse the root back up
    parent = None
    temp_parent = root
    while temp_parent is not None:
        parent = temp_parent
        if temp_parent.data > data:
            temp_parent = temp_parent.left
        else:
            temp_parent = temp_parent.right

    if parent.data > new_parent.data:
        parent.left = new_parent
    else:
        parent.right = new_parent

    return root


def find_in_bst(root, d):
    if root == None:
        return None

    if root.data == d:
        return root
    elif root.data > d:
        return find_in_bst(root.left, d)
    else:
        return find_in_bst(root.right, d)


# find node in inorder
# works for both BST and binary tree
def find_node(root, d):
    if root == None:
        return

    if root.data == d:
        return root

    temp = find_node(root.left, d)
    if temp != None:
        return temp

    return find_node(root.right, d)


def display_inorder(node):
    if node == None:
        return

    display_inorder(node.left)
    print(str(node.data))
    display_inorder(node.right)


def create_BST(arr):
    root = None
    for data in arr:
        # recursively update root of bst
        root = insert(root, data)
    return root


def create_binary_tree(count):
    root = None
    for i in range(1, count):
        root = insert(root, random.randrange(1, 100))
    return root


def create_random_BST(count):
    root = None;
    for i in range(1, count):
        root = insert(root, random.randrange(200, 300))
    return root


def bst_to_list_rec(root, lst):
    if root == None:
        return

    bst_to_list_rec(root.left, lst)
    lst.append(root.data)
    bst_to_list_rec(root.right, lst)


def bst_to_list(root):
    lst = []
    bst_to_list_rec(root, lst)
    return lst


def insert_at_head(head, data):
    newNode = LinkedListNode(data)
    newNode.next = head
    return newNode


def populate_parents_rec(root, parent):
    if root == None:
        return
    root.parent = parent

    populate_parents_rec(root.left, root)
    populate_parents_rec(root.right, root)


def populate_parents(root):
    populate_parents_rec(root, None)


def display_level_order(root):
    if root == None:
        return
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        print(str(temp.data))
        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)

    print()


def get_level_order(root):
    output = []
    if root == None:
        return output

    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        output.append(temp.data)
        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)

    return output


def get_inorder_helper(root, output):
    if root == None:
        return output

    output = get_inorder_helper(root.left, output)
    output.append(root.data)
    output = get_inorder_helper(root.right, output)

    return output


def get_inorder(root):
    output = []
    return get_inorder_helper(root, output)


def is_identical_tree(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None and root1.data == root2.data:
        return is_identical_tree(root1.left, root2.left) and is_identical_tree(root1.right, root2.right)

    return False
