"""
Implement the find_mother_vertex() function which will take a directed graph
as an input and find out which vertex is the mother vertex in the graph.

By definition, the mother vertex is a vertex in a graph such that all other
vertices in a graph can be reached by following a path from that vertex.
A graph can have multiple mother vertices, but you only need to find one.
"""
from graph import Graph
from collections import deque


def dfs_path_counter(g: Graph, index: int) -> int:
    # initialize values
    result = 0
    visited = [False] * g.vertices
    queue = deque()

    # visit first node
    queue.append(index)
    visited[index] = True
    result += 1

    # visit remaining nodes
    while queue:
        curr_node = queue.pop()
        temp_node = g.array[curr_node].get_head()
        while temp_node:
            if not visited[temp_node.data]:
                visited[temp_node.data] = True
                result += 1
                queue.append(temp_node.data)
            temp_node = temp_node.next_element
    return result


def find_mother_vertex(g: Graph) -> int:
    """
    Mother vertex is a vertex in a graph such that all other vertices in a
    graph can be reached by following a path from that vertex.
    1. Loop over each node and for each node run DFS
    2. keep a counter of visited nodes
    3. If the response counter equals to the number of vertices, then
        we found the mother node that reaches all other vertices in the graph
    """
    for node_index in range(len(g.array)):
        result = dfs_path_counter(g, node_index)
        if result == g.vertices:
            return node_index
    else:
        return -1


def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)

    assert find_mother_vertex(g) == 3

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 0)

    assert find_mother_vertex(g2) == 0


main()
