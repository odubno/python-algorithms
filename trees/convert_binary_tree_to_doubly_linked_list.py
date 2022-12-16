"""
Convert a binary tree to a doubly linked list so that the order of the
doubly-linked list is the same as an in-order traversal of the binary tree.
After conversion, the left pointer of the node should be pointing to the
previous node in the doubly linked list, and the right pointer should be
pointing to the next node in the doubly linked list.
Revisit
"""
import implementation_of_binary_tree as bt


def concatenate_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # use left for previous.
    # use right for next.
    tail1 = head1.left
    tail2 = head2.left

    tail1.right = head2
    head2.left = tail1

    head1.left = tail2
    tail2.right = head1
    return head1


def convert_to_linked_list_rec(root):
    if root is None:
        return None

    # 1. visit all the left nodes first
    list1 = convert_to_linked_list_rec(root.left)

    # 2. visit all the right nodes last
    list2 = convert_to_linked_list_rec(root.right)

    root.left = root
    root.right = root

    result1 = concatenate_lists(list1, root)
    result2 = concatenate_lists(result1, list2)

    return result2


def convert_to_linked_list(root):
    # first traverse all the left nodes, then revisit the root and finally the right
    head = convert_to_linked_list_rec(root)
    if head.left is not None:
        # most left value i.e. head, have it point to None
        head.left.right = None
        # most right value i.e. tail have it point to None
        head.left = None
    return head


def get_list(head):
    r = []
    if not head:
        return r

    temp = head
    while temp:
        r.append(temp.data)
        temp = temp.right
    return r


data = [100,50,200,25,75,350, 30, 60]
root = bt.create_BST(data)
head = convert_to_linked_list(root)
v = get_list(head)
print(v)