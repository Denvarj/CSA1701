"""Depth First Search (DFS)"""


def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print("Visiting:", start)

    if start == goal:
        return True

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    print("Goal found?", dfs(graph, 'A', 'F'))
