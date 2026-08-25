"""Tic-Tac-Toe Problem with Minimax"""
import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def winner(board):
    for line in board + [list(col) for col in zip(*board)]:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, is_maximizing):
    w = winner(board)
    if w == "X":
        return 1
    if w == "O":
        return -1
    if not available_moves(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for r, c in available_moves(board):
            board[r][c] = "X"
            score = minimax(board, False)
            board[r][c] = " "
            best_score = max(best_score, score)
        return best_score
    best_score = math.inf
    for r, c in available_moves(board):
        board[r][c] = "O"
        score = minimax(board, True)
        board[r][c] = " "
        best_score = min(best_score, score)
    return best_score

if __name__ == "__main__":
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_board(board)
    print("Best move score:", minimax(board, True))
