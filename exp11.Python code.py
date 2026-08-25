"""Alpha-Beta Pruning"""

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []

    def is_terminal(self):
        return not self.children

    def evaluate(self):
        return self.value

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()
    if maximizing_player:
        value = float("-inf")
        for child in node.children:
            value = max(value, alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for child in node.children:
        value = min(value, alpha_beta(child, depth - 1, alpha, beta, True))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value

if __name__ == "__main__":
    root = Node(0, [Node(5, [Node(3), Node(8)]), Node(4, [Node(2), Node(9)])])
    print("Alpha-beta pruning value:", alpha_beta(root, 2, float("-inf"), float("inf"), True))
