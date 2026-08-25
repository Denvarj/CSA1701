"""Minimax Algorithm"""

class Node:
    def __init__(self, score, children=None):
        self.score = score
        self.children = children or []

    def is_terminal(self):
        return not self.children

def minimax(node, depth, is_maximizing):
    if depth == 0 or node.is_terminal():
        return node.score
    if is_maximizing:
        best = float("-inf")
        for child in node.children:
            best = max(best, minimax(child, depth - 1, False))
        return best
    best = float("inf")
    for child in node.children:
        best = min(best, minimax(child, depth - 1, True))
    return best

if __name__ == "__main__":
    tree = Node(0, [Node(0, [Node(3), Node(5)]), Node(0, [Node(2), Node(9)])])
    print("Minimax result:", minimax(tree, 2, True))
