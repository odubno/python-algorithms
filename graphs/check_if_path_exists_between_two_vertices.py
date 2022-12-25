"""
Implement the check_path() function. It takes a source vertex and a destination
vertex and tells us whether or not a path exists between the two.
"""
from graph import Graph
from collections import deque


def check_path_rec(
        g: Graph,
        source_vertex: int,
        destination_vertex: int
    ) -> bool:

    visited = [False] * len(g.array)
    queue = deque()
    queue.append(source_vertex)

    while queue:
        curr_node = queue.pop()  # 0
        temp_node = g.array[curr_node].get_head()  # 2
        while temp_node:
            if temp_node.data == destination_vertex:
                return True
            if not visited[temp_node.data]:
                visited[temp_node.data] = True
                queue.append(temp_node.data)
            temp_node = temp_node.next_element
    else:
        return False


def check_path(g: Graph, source_vertex: int, destination_vertex: int) -> bool:
    """
    1. Use DFS to check if path exists
    2. Use source_vertex as the starting index
    3. Keep checking, using the same starting index, until a path does exist
    4. return True, otherwise return False

    Time: O(V + E) standard time complexity for DFS
    Space: O(V), we have to store the nodes
    """
    result = check_path_rec(g, source_vertex, destination_vertex)
    return result


def main():
    g = Graph(9)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(5, 3)
    g.add_edge(5, 6)
    g.add_edge(3, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 4)
    g.add_edge(7, 8)

    assert check_path(g, 0, 7)


main()
