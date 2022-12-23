"""
Implement the find_mother_vertex() function which will take a directed graph
as an input and find out which vertex is the mother vertex in the graph.

By definition, the mother vertex is a vertex in a graph such that all other
vertices in a graph can be reached by following a path from that vertex.
A graph can have multiple mother vertices, but you only need to find one.
"""
from graph import Graph
from collections import deque


def find_mother_vertex(g):
    """
    1. use dictionary to track count of each vertex
    2. visit every node using DFS
    3. return vertex with highest counter
    4. if there is a duplicate counter
        1. get the highest count and only return the vertices with the top counter
    """
    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS(g, i)
        if num_of_vertices_reached == g.vertices:
            return i
    return -1


def perform_DFS(g, source):
    # track number of vertices reached from source
    vertices_reached = 0

    visited = [False] * g.vertices
    stack = deque()
    stack.append(source)
    visited[source] = True

    while stack:
        current_node = stack.pop()
        temp = g.array[current_node].head_node
        while temp:
            if not visited[temp.data]:
                stack.append(temp.data)
                visited[temp.data] = True
                vertices_reached += 1
            temp = temp.next_element
    return vertices_reached + 1



def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)

    assert find_mother_vertex(g) == 3

    g2 = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    assert find_mother_vertex(g2) == 1


main()
