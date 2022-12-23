"""
The concept of loops or cycles is very common in graph theory. A cycle exists
when you traverse the directed graph and come upon a vertex that has already
been visited.

You have to implement the detect_cycle function which tells you whether or not
a graph contains a cycle.
"""

from graph import Graph
from collections import deque


def detect_cycle_mine(g: Graph) -> bool:
    """
    1. keep a track of visited nodes
    2. traverse graph using BFS if a previous node that's in visited
        comes up again return True
    """
    results = set()
    visited = [False] * g.vertices
    source = 0
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        # pop FIFO elem
        curr_node = queue.popleft()

        # check for cycle
        if curr_node in results:
            return True
        results.add(curr_node)

        temp = g.array[curr_node].get_head()
        while temp:
            if visited[temp.data]:
                temp = None
                continue
            queue.append(temp.data)
            visited[temp.data] = True
            temp = temp.next_element
    return False


def detect_cycle_basic(g):
    result = set()
    result.add(0)
    num_of_vertices = g.vertices
    for i in range(num_of_vertices):
        temp = g.array[i].get_head()
        while temp:
            if temp.data in result:
                return True
            result.add(temp.data)
            temp = temp.next_element
    return False


def dfs_detect_cycle_recursive(g, source=0, result=None, visited=None):
    """
    1. recursively visit child nodes of parents
    2. store results in result
    revisit: see if less while loops are possible

    Like the BFS, this algorithm traverses the whole list once.
    Hence, it’s time complexity is O(V + E)
    """
    if result is None:
        result = set()

    if visited is None:
        visited = [False] * len(g.array)

    if all(visited):
        return False

    stack = deque()
    stack.append(source)
    visited[source] = True

    while stack:
        current_node = stack.pop()
        result.add(current_node)
        temp = g.array[current_node].head_node
        while temp:

            if temp.data in result:
                return True
            result.add(temp.data)

            if not visited[temp.data]:
                stack.append(temp.data)
                visited[temp.data] = True
            temp = temp.next_element

    return dfs_detect_cycle_recursive(g, source+1, result, visited)


def main():
    V = 4  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 0)

    assert dfs_detect_cycle_recursive(g)

    V = 3  # Total vertices
    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    assert not dfs_detect_cycle_recursive(g2)

    g.print_graph()


main()
