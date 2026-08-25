"""Water Jug Problem"""
from collections import deque


def water_jug(start=(0, 0), goal=2):
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        (x, y), path = queue.popleft()
        if x == goal or y == goal:
            return path

        states = [
            (0, y),
            (x, 0),
            (3, y),
            (x, 4),
        ]

        if x + y <= 3:
            states.append((x + y, 0))
        else:
            states.append((3, x + y - 3))

        if x + y <= 4:
            states.append((0, x + y))
        else:
            states.append((x + y - 4, 4))

        for nxt in states:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))

    return None


if __name__ == "__main__":
    print("Water jug path:", water_jug())
