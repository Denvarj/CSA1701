"""Travelling Salesman Problem (TSP)"""
from itertools import permutations

def tsp(cost_matrix):
    n = len(cost_matrix)
    cities = list(range(n))
    best_cost = float("inf")
    best_path = None
    for perm in permutations(cities[1:]):
        path = [0] + list(perm) + [0]
        total_cost = sum(cost_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path
    return best_cost, best_path

if __name__ == "__main__":
    cost = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print("Minimum cost:", tsp(cost)[0])
    print("Route:", tsp(cost)[1])
