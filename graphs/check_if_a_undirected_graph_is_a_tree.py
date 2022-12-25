"""
A graph can only be a tree under two conditions:
    1. There are no cycles.
    2. The graph is connected.


"""
from graph import Graph
from collections import deque, defaultdict


def is_tree(g: Graph) -> bool:
    """
    Returns True if the graph is a tree

    1. Either DFS or BFS would work here
    2. Use BFS to traverse the graph keeping track of visited nodes
    3. if the next element of a node points back to an already visited node,
        then we have a graph
    4. keep checking until the end

    Time: O(V + E)
    Space: O(V) for tracking all the vertices
    """
    visited = [False] * g.vertices
    nodes = defaultdict(int)

    for node_index in range(g.vertices):
        visited, nodes = bfs(g, node_index, visited, nodes)
        has_cycle = any([True for k, v in nodes.items() if v > 1])
        if has_cycle:
            return False
        if all(visited):
            # if all nodes have already been visited and no cycle is present
            # return true for is_tree
            return True
    else:
        return True


def bfs(g: Graph, node_index: int, visited, nodes):

    queue = deque()
    queue.append(node_index)  # 0
    nodes[node_index] += 1
    visited[node_index] = True

    while queue:
        curr_node = queue.popleft()  # 0, 2
        temp_node = g.array[curr_node].get_head()  # 1, 3
        while temp_node:
            if not visited[temp_node.data]:
                visited[temp_node.data] = True
                queue.append(temp_node.data)
            nodes[temp_node.data] += 1
            temp_node = temp_node.next_element

    return visited, nodes


def main():
    # g = Graph(5)
    # g.add_edge(0, 1)
    # g.add_edge(0, 2)
    # g.add_edge(0, 3)
    # g.add_edge(3, 4)
    #
    # assert is_tree(g)

    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(0, 3)
    g2.add_edge(2, 3)

    assert not is_tree(g2)

main()
