import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if square == None:
            return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True  # Return True for a successful move
        return False  # Return False for an invalid move

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(player1, player2):
    game = TicTacToe()
    while game.empty_squares():
        player1_move = player1.get_move(game)
        if game.make_move(player1_move, 'X'):
            if game.current_winner:
                return game.current_winner

        player2_move = player2.get_move(game)
        if game.make_move(player2_move, 'O'):
            if game.current_winner:
                return game.current_winner

    return 'Draw'


class RandomPlayer:
    def get_move(self, game):
        return random.choice(game.available_moves())


class MonteCarloPlayer:
    def __init__(self, epsilon=0.1, alpha=0.5):
        self.epsilon = epsilon
        self.alpha = alpha
        self.q = {}

    def get_q(self, state, action):
        if (state, action) not in self.q:
            self.q[(state, action)] = 0
        return self.q[(state, action)]

    def get_move(self, game):
        available_moves = game.available_moves()
        if not available_moves:
            return None  # Handle the case when there are no available moves

        if random.uniform(0, 1) < self.epsilon:
            return random.choice(available_moves)
        else:
            best_action = None
            best_value = -float('inf')
            for action in available_moves:
                current_state = tuple(game.board)
                value = self.get_q(current_state, action)
                if value > best_value:
                    best_value = value
                    best_action = action
            return best_action

    def update_q_values(self, state, action, winner):
        if (state, action) not in self.q:
            self.q[(state, action)] = 0
        if winner == 'X':
            self.q[(state, action)] += self.alpha
        elif winner == 'O':
            self.q[(state, action)] -= self.alpha


if __name__ == "__main__":
    num_episodes = 100

    player1 = MonteCarloPlayer()
    player2 = MonteCarloPlayer()

    for episode in range(num_episodes):
        episode_moves = []
        game = TicTacToe()  # Create a new game for each episode
        while True:
            winner = play(player1, player2)
            current_state = tuple(game.board)
            episode_moves.append((current_state, player1.get_move(game)))

            if winner:
                break

            current_state = tuple(game.board)
            episode_moves.append((current_state, player2.get_move(game)))

        for state, action in episode_moves:
            player1.update_q_values(state, action, winner)
            player2.update_q_values(state, action, winner)

    # Test the trained agent against a random player
    wins = 0
    for _ in range(100):
        game = TicTacToe()
        winner = play(player1, player2)
        if winner == 'X':
            wins += 1

    print(
        f"Monte Carlo Player won {wins} out of 100 games against a random player.")
