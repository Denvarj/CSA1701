"""Best First Search"""
from heapq import heappush, heappop

def best_first_search(graph, start, goal):
    open_list = [(0, start)]
    came_from = {start: None}
    visited = {start}
    while open_list:
        _, node = heappop(open_list)
        if node == goal:
            return came_from
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = node
                heappush(open_list, (0, neighbor))
    return came_from

if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": ["F"], "E": ["F"], "F": []}
    print("Best First Search parents:", best_first_search(graph, "A", "F"))
