"""
Implement a function that returns the number of nodes at a given level starting
from a root node of a directed graph.
"""

from graph import Graph
from collections import deque


def number_of_nodes_helper(
        g: Graph,
        desired_level: int,
        current_level: int = 1,
        node_index: int = 0
    ):
    queue = deque()
    visited = [False] * g.vertices

    # initialize first queue value
    queue.append(node_index)
    visited[node_index] = True

    while queue:  # 1 | 2, 1
        level_length = len(queue)  # 1

        # if level match return length of nodes at that level
        if current_level == desired_level:  # 1 == 3
            return level_length

        # process remaining nodes
        curr_node = queue.popleft()  # 0, 2, 1
        temp_node = g.array[curr_node].get_head()  # 2
        while temp_node:
            if not visited[temp_node.data]:
                visited[temp_node] = True
                queue.append(temp_node.data)  # 2, 1, 4, 3
            temp_node = temp_node.next_element  # 1

        # completed a level increment it
        current_level += 1

    return 0


def number_of_nodes(g: Graph, level: int) -> int:
    """
    Calculate the number of nodes at a given level

    Input: An undirected graph represented as an adjacency list,
        and the level whose number of nodes we need to find

    Output: The number of nodes returned as a simple integer

    1. Use BFS to traverse nodes
    2. Use a queue and a visited list to track unvisted nodes
    3. while queue is not empty, take length of queue and increment number count
        1. at each queue implementation take the length of the queue
            1. if the level equals the desired level return length

    Time: O(V + E) because we will traverse all nodes and edges
    """

    result = number_of_nodes_helper(g, level)
    return result


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    assert number_of_nodes(g, 1) == 1
    assert number_of_nodes(g, 2) == 2
    assert number_of_nodes(g, 3) == 2
    assert number_of_nodes(g, 4) == 0

    g2 = Graph(10)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(0, 3)
    g2.add_edge(1, 4)
    g2.add_edge(1, 5)
    g2.add_edge(1, 6)
    g2.add_edge(1, 7)
    g2.add_edge(4, 8)
    g2.add_edge(4, 9)

    assert number_of_nodes(g2, 2) == 4
    assert number_of_nodes(g2, 3) == 2
    assert number_of_nodes(g2, 4) == 0, "level does not exist and is zero"
