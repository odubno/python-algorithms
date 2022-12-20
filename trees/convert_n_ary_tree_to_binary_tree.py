"""
Convert an N-ary tree to a Binary tree and then convert the Binary tree back
to its original N-ary tree structure. Consider the following N-ary tree:

The root of the Binary Tree is the Root of the N-ary Tree.
The leftmost child of a node in the N-ary is the Left child of that node in the Binary Tree.
The right sibling of any node in the N-ary Tree is the Right child of that node in the Binary Tree.
"""

import implementation_of_binary_tree as bt

from os import *
from sys import *
from collections import *
from math import *


# Nary tree node class for reference:
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def display_level_order(self, root=0):
        if root == 0:
            root = self.data

        if root is None:
            return

        q = deque()
        q.extend(self.children)
        while q:
            temp = q.popleft()
            if temp.children:
                for child in temp.children:
                    print(str(child.data))
                    q.append(child)
        print()


def convert_n_ary_to_binary(node):
  return convert_n_ary_to_binary_rec(node,1)

def convert_n_ary_to_binary_rec(root,isLeft):
  if root == None:
    return

  btnode = bt.BinaryTreeNode(root.data)
  lastnode = btnode

  for child in root.children:
    if isLeft == 1:
      lastnode.left = convert_n_ary_to_binary_rec(
        child, 0);
      lastnode = lastnode.left;
    else:
      lastnode.right = convert_n_ary_to_binary_rec(
        child, 1);
      lastnode = lastnode.right;

  return btnode;

def convert_binary_to_n_ary(node):
  return convert_binary_to_n_ary_rec(node,1)

def convert_binary_to_n_ary_rec(node,isLeft):
  if node == None:
    return

  nnode = TreeNode(node.data)
  temp = node

  if isLeft == 1:
    while(temp.left != None):
      child = convert_binary_to_n_ary_rec(temp.left, 0)
      nnode.children.append(child)
      temp = temp.left
  else:
    while(temp.right != None):
      child = convert_binary_to_n_ary_rec(temp.right, 1)
      nnode.children.append(child)
      temp = temp.right

  return nnode

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.children.append(node2)
node1.children.append(node3)
node1.children.append(node4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node3.children.append(node5)
node3.children.append(node6)

print("Original n-ary tree")
node1.display_level_order()
bnode1 = convert_n_ary_to_binary(node1)
print("Converted binary tree")
bt.display_level_order(bnode1)
# If the tree is converted into BT then the following statement must return "5"
# print("Root.Left.Left.Right = " + str(bnode1.left.left.right.data))

tnode1 = convert_binary_to_n_ary(bnode1)
print("\nConverted n-ary tree")
tnode1.display_level_order()
