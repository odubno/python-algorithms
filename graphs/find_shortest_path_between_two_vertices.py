"""
Implement the find_min() function which will take a directed graph and two
vertices, A and B. The result will be the shortest path from A to B.
"""
from graph import Graph
from collections import deque


def find_educative_min(g: Graph, source: int, destination: int) -> int:
    num_of_vertices = g.vertices
    visited = [False] * num_of_vertices
    distance = [0] * num_of_vertices

    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        curr_node = queue.pop()
        temp_node = g.array[curr_node].get_head()
        while temp_node:
            if not visited[temp_node.data] or temp_node.data == destination:
                visited[temp_node.data] = True
                queue.append(temp_node.data)

                # increment the curr_node count and record it to distance
                # of the temp_node
                # use the path of the current node and extend it to the temporary node
                # temp node could be thought of as the next node
                distance[temp_node.data] = distance[curr_node] + 1

                if temp_node.data == destination:
                    return distance[destination]
            temp_node = temp_node.next_element
    return -1


def dfs(g: Graph, source: int, destination: int):
    queue = deque()
    queue.append(source)
    shortest_path = float("inf")

    possible_path = 0
    while queue:
        curr_node = queue.pop()  # 0
        temp_node = g.array[curr_node].get_head()  # 3
        while temp_node:
            possible_path += 1
            if temp_node.data == destination:
                # if destination is found, record the length of the path
                if shortest_path > possible_path:
                    shortest_path = possible_path
                # whatever length path has been found, no use in continuing
                break
            temp_node = g.array[temp_node.data].get_head()

        next_node = g.array[curr_node].get_head()
        if next_node.next_element:
            # re-instantiating possible_path to 1 to account for the root
            possible_path = 1
            queue.append(next_node.next_element.data)

    return shortest_path


def find_min(g: Graph, source: int, destination: int):
    """
    Returns number of edges in the shortest path between source and destination

    1. We would have to visit all possible edges coming from source
    2. track `shortest_path` shortest edge to destination.
        1. decrement the path until all nodes are checked
    3. return the minimum edge

    1. Use DFS from the source and record all possible paths
    2. Choose the shortest path
    """

    return dfs(g, source, destination)


def main():
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.add_edge(2, 4)

    assert find_min(g, 0, 4) == 2
    assert find_educative_min(g, 0, 4) == 2


    g2 = Graph(7)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 4)
    g2.add_edge(4, 5)
    g2.add_edge(2, 5)
    g2.add_edge(5, 6)
    g2.add_edge(3, 6)

    assert find_min(g2, 1, 5) == 2
    assert find_educative_min(g2, 1, 5) == 2


main()
