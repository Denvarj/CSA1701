"""Missionaries and Cannibals Problem"""
from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    if m_left >= 0 and c_left >= 0 and m_right >= 0 and c_right >= 0:
        if (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right):
            return True
    return False

def next_states(state):
    m_left, c_left, boat = state
    moves = []
    if boat == 0:
        for dm in [1, 2]:
            for dc in [0, 1, 2]:
                if dm + dc in [1, 2]:
                    nm, nc = m_left - dm, c_left - dc
                    if 0 <= nm <= 3 and 0 <= nc <= 3:
                        moves.append((nm, nc, 1))
    else:
        for dm in [1, 2]:
            for dc in [0, 1, 2]:
                if dm + dc in [1, 2]:
                    nm, nc = m_left + dm, c_left + dc
                    if 0 <= nm <= 3 and 0 <= nc <= 3:
                        moves.append((nm, nc, 0))
    return [s for s in moves if is_valid(s)]

def missionaries_cannibals():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for nxt in next_states(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

if __name__ == "__main__":
    print("Solution path:", missionaries_cannibals())
