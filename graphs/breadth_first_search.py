"""
Implement the Breadth First Search traversal in Python

Note: Your solution should work for both connected and unconnected graphs.
"""

from graph import Graph
from my_queue import MyQueue
from typing import List

# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex


def bfs_traversal_basic(g: Graph, source: int) -> str:
    """
    :param g: directed graph
    :param source: the starting vertex number (source)

    :output:
        string containing the vertices of the graph listed in the correct order of traversal

    1. Use BFS
    2. create a queue, append the root
    3. while queue has items keep searching
    4. continue to append w/e items are available

    Time: Since this algorithm traverses the whole graph once, its time complexity is O(V + E).
    """
    result = ""
    num_of_vertices = g.vertices
    result += str(source)
    for i in range(num_of_vertices):
        temp = g.array[i].get_head()
        while temp:
            result += str(temp.data)
            temp = temp.next_element
    return result


def bfs_traversal_helper(
        g: Graph,
        source: int,
        visited: List[bool]
    ) -> (str, List[bool]):
    result = ""
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True
    while not queue.is_empty():
        current_node = queue.dequeue()
        result += str(current_node)
        temp = g.array[current_node].head_node
        while temp:
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True  # visit the current Node
            temp = temp.next_element
    return result, visited


def get_visited_nodes(num_of_vertices: int) -> List[bool]:
    # create a list to hold the history of visited nodes
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    return visited


def bfs_traversal(g: Graph, source: int) -> str:
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result

    # create a list to hold the history of visited nodes
    visited = get_visited_nodes(num_of_vertices)

    # begin from source
    result, visited = bfs_traversal_helper(g, source, visited)

    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new
    return result


def main():
    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    bfs_traversal_result = bfs_traversal(g, 0)
    assert bfs_traversal_result in ('02143', '02134', '01234', '01243')

    bfs_traversal_result_first = bfs_traversal_basic(g, 0)
    assert bfs_traversal_result_first in ('02143', '02134', '01234', '01243')
    # g.print_graph()


main()
