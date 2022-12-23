from graph import Graph
from stack import MyStack

# You can check the input directed graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}
# Depth First Traversal of Graph "g" from source vertex
from collections import deque


def dfs_traversal_mine(g, source, visited=None, result=None):
    if visited is None:
        visited = [False] * g.vertices

    if result is None:
        result = []

    if all(visited):
        return result

    stack = deque()
    stack.append(source)
    result.append(source)
    visited[source] = True

    while stack:
        temp_node_index = stack.pop()
        temp_node = g.array[temp_node_index].get_head()
        while temp_node:
            if not visited[temp_node.data]:
                result.append(temp_node.data)
                stack.append(temp_node.data)
                visited[temp_node.data] = True
            temp_node = temp_node.next_element
    dfs_traversal_mine(g, source+1, visited, result)
    return result


def dfs_traversal_recursive(g, source, visited=None):
    """
    1. recursively visit child nodes of parents
    2. store results in result
    revisit: see if less while loops are possible

    Like the BFS, this algorithm traverses the whole list once.
    Hence, it’s time complexity is O(V + E)
    """
    result = ""

    if visited is None:
        visited = [False] * len(g.array)

    if all(visited):
        return result

    stack = deque()
    stack.append(source)
    visited[source] = True

    while stack:
        current_node = stack.pop()
        result += str(current_node)

        temp = g.array[current_node].head_node
        while temp:
            if not visited[temp.data]:
                stack.append(temp.data)
                visited[temp.data] = True
            temp = temp.next_element

    result += dfs_traversal_recursive(g, source+1, visited)
    return result


def dfs_traversal_helper_basic(g, source):
    result = ""

    visited = [False] * len(g.array)

    stack = deque()
    stack.append(source)
    visited[source] = True

    while stack:
        current_node = stack.pop()
        result += str(current_node)

        temp = g.array[current_node].head_node
        while temp:
            if not visited[temp.data]:
                stack.append(temp.data)
                visited[temp.data] = True
            temp = temp.next_element

    return result


def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while not stack.is_empty() :
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited  # For the above graph it should return "12453"


def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    # result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


def main():
    V = 7  # Total vertices
    g = Graph(V)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    m = dfs_traversal_mine(g, 0)

    g.print_graph()

    dfs_rec = dfs_traversal_recursive(g, 0)

    assert dfs_rec in ('0124536', '0136254')

    dfs_traversal_result = dfs_traversal(g, 0)
    assert dfs_traversal_result in ('0124536', '0136254')


main()
