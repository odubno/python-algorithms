"""
Serialize a binary tree to a file and then deserialize it back to a tree so that
the original and the deserialized trees are identical.

Serialize: write the tree in a file.

Deserialize: read from a file and reconstruct the tree in memory.

revisit
"""
import implementation_of_binary_tree as bt
from typing import Optional
import io
import pickle


def serialize(node: bt.BinaryTreeNode, stream: pickle.Pickler) -> pickle.Pickler:
    # use DFS to serialize nodes in order
    if not node:
        # write None to indicate the end
        stream.dump(None)
        return stream

    stream.dump(node.data)

    # traverse left most tree first
    serialize(node.left, stream)

    # traverse right most tree after
    serialize(node.right, stream)

    return stream


def deserialize(stream: io.BufferedReader) -> Optional[bt.BinaryTreeNode]:
    try:
        data = pickle.load(stream)
    except:
        return None

    if not data:
        return None

    root = bt.BinaryTreeNode(data)

    root.left = deserialize(stream)
    root.right = deserialize(stream)

    return root


def both_trees_match(root_1: bt.BinaryTreeNode, root_2: bt.BinaryTreeNode):
    if root_1 is None and root_2 is None:
        return True

    if root_1 is not None and root_2 is not None:
        data_is_equal = root_1.data == root_2.data
        return data_is_equal and \
               both_trees_match(root_1.left, root_2.left) and \
               both_trees_match(root_1.right, root_2.right)
    else:
        return False


def main():
    arr = [100, 50, 200, 25, 75, 125, 350]
    root = bt.create_BST(arr)
    arr1 = [100, 50, 200, 25, 75, 350]
    root1 = bt.create_BST(arr1)
    output = open('data.class', 'wb')
    p = pickle.Pickler(output)
    serialize(root, p)
    output.close()
    input2 = open('data.class', 'rb')
    root_deserialized = deserialize(input2)  # type: ignore # typing.TextIO incompatible with io.IOBase
    print('result')
    assert both_trees_match(root, root1) is False
    assert both_trees_match(root, root_deserialized) is True

    assert root == root_deserialized


main()
