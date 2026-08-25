"""Monkey and Banana Problem"""
from collections import deque

def monkey_and_banana():
    start = (0, 0, 0)
    goal = (1, 1, 1)
    queue = deque([start])
    visited = {start}
    while queue:
        state = queue.popleft()
        if state == goal:
            return True
        monkey, box, banana = state
        next_states = [(1, box, banana), (monkey, 1, banana), (1, 1, 1), (0, 0, banana)]
        for nxt in next_states:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return False

if __name__ == "__main__":
    print("Monkey can reach banana?", monkey_and_banana())
