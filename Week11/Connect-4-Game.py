import numpy as np

class ConnectFour:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.player_turn = 1  # Player 1 starts

    def display_board(self, board=None):
        if board is None:
            board = self.board
        for row in reversed(range(self.rows)):
            print("|", end="")
            for col in range(self.cols):
                if board[row, col] == 0:
                    print("   |", end="")
                else:
                    print(f" {board[row, col]} |", end="")
            print("\n" + "-" * (4 * self.cols + 1))
   
    def is_valid_move(self, col, board=None):
        if board is None:
            board = self.board
        return 0 <= col < self.cols and board[self.rows - 1, col] == 0
    def make_move(self, col, player, board=None):
        if board is None:
            board = np.copy(self.board)
        for row in range(self.rows):
            if board[row, col] == 0:
                board[row, col] = player
                return board
    def undo_move(self, col, board):
        for row in reversed(range(self.rows)):
            if board[row, col] != 0:
                board[row, col] = 0
                return board

    def check_winner(self, board=None):
        if board is None:
            board = self.board
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if (self.board[row, col] == self.board[row, col + 1] == self.board[row, col + 2] == self.board[row, col + 3]) and (self.board[row, col] != 0):
                    return self.board[row, col]
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if (self.board[row, col] == self.board[row + 1, col] == self.board[row + 2, col] == self.board[row + 3, col]) and (self.board[row, col] != 0):
                    return self.board[row, col]
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if (self.board[row, col] == self.board[row + 1, col + 1] == self.board[row + 2, col + 2] == self.board[row + 3, col + 3]) and (self.board[row, col] != 0):
                    return self.board[row, col]
                if (self.board[row + 3, col] == self.board[row + 2, col + 1] == self.board[row + 1, col + 2] == self.board[row, col + 3]) and (self.board[row + 3, col] != 0):
                    return self.board[row + 3, col]
        return 0

    def is_board_full(self, board=None):
        if board is None:
            board = self.board
        return np.all(board != 0)

    def evaluate_state(self, board=None):
        if board is None:
            board = self.board

        # Evaluate based on the number of connected pieces
        score = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row, col] == 1:
                    score += self.score_position(board, row, col, 1)
                elif board[row, col] == 2:
                    score -= self.score_position(board, row, col, 2)

        return score

    def score_position(self, board, row, col, player):
        score = 0

        # Horizontal 
        for c in range(col, col + 4):
            if 0 <= c < self.cols:
                if board[row, c] == player:
                    score += 1

        # Vertical
        for r in range(row, row + 4):
            if 0 <= r < self.rows:
                if board[r, col] == player:
                    score += 1

        # Diagonal \
        for i in range(4):
            r, c = row + i, col + i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if board[r, c] == player:
                    score += 1

        # Diagonal /
        for i in range(4):
            r, c = row + i, col - i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if board[r, c] == player:
                    score += 1

        return score

    def minimax(self, depth, alpha, beta, maximizing_player, board=None):
        if board is None:
            board = self.board
        if depth == 0 or self.is_board_full(board):
            return self.evaluate_state(board)

        if maximizing_player:
            max_eval = float("-inf")
            for col in range(self.cols):
                if self.is_valid_move(col, board):
                    new_board = self.make_move(col, 2, board)
                    eval = self.minimax(depth - 1, alpha, beta, False, new_board)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float("inf")
            for col in range(self.cols):
                if self.is_valid_move(col, board):
                    new_board = self.make_move(col, 1, board)
                    eval = self.minimax(depth - 1, alpha, beta, True, new_board)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def get_best_move(self):
        best_move = -1
        best_eval = float("-inf")
        for col in range(self.cols):
            if self.is_valid_move(col):
                new_board = self.make_move(col, 2)
                eval = self.minimax(3, float("-inf"), float("inf"), False, new_board)  # Adjust the depth as needed
                if eval > best_eval:
                    best_eval = eval
                    best_move = col
        return best_move

    def play_game(self):
        while True:
            self.display_board()
            print(f"Player {self.player_turn}'s turn")

            if self.player_turn == 1:
                col = int(input("Player 1 (X) - Enter column (0-6): "))
            else:
                col = self.get_best_move()

            if self.is_valid_move(col):
                self.board = self.make_move(col, self.player_turn)
                winner = self.check_winner() 
                if winner:
                    self.display_board()
                    print(f"Player {winner} wins!")
                    break
                elif self.is_board_full():
                    self.display_board()
                    print("It's a tie!")
                    break
            else:
                print("Invalid move. Try again.")

            self.player_turn = 3 - self.player_turn  # Switch player turn

if __name__ == "__main__":
    connect_four_game = ConnectFour()
    connect_four_game.play_game()
