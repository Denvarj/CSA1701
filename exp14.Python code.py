"""A* Search Algorithm"""
from heapq import heappush, heappop

def a_star(graph, start, goal):
    heuristic = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "G": 0}
    open_heap = [(0, 0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    while open_heap:
        _, cost_so_far, node = heappop(open_heap)
        if node == goal:
            return cost_so_far, parent
        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost_so_far + edge_cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = node
                heappush(open_heap, (new_cost + heuristic[neighbor], new_cost, neighbor))
    return None, parent

if __name__ == "__main__":
    graph = {"A": [("B", 2), ("C", 1)], "B": [("D", 3)], "C": [("E", 2)], "D": [("G", 1)], "E": [("G", 1)], "G": []}
    cost, parent = a_star(graph, "A", "G")
    print("A* path cost:", cost)
    print("Parents:", parent)
