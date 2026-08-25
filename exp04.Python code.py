"""8-Puzzle Problem using BFS"""
from collections import deque


def swap(state, i, j):
    lst = list(state)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)


def neighbors(state):
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    result = []

    if row > 0:
        result.append(swap(state, zero_index, zero_index - 3))
    if row < 2:
        result.append(swap(state, zero_index, zero_index + 3))
    if col > 0:
        result.append(swap(state, zero_index, zero_index - 1))
    if col < 2:
        result.append(swap(state, zero_index, zero_index + 1))

    return result


def bfs_8_puzzle(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        for nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None


if __name__ == "__main__":
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    path = bfs_8_puzzle(start, goal)
    print("Solution path:", path)
    print("Steps:", len(path) - 1 if path else "No solution")
