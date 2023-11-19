import random
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
    def display_board(self):
        print(f'{self.board[0]}|{self.board[1]}|{self.board[2]}')
        print('-+-+-')
        print(f'{self.board[3]}|{self.board[4]}|{self.board[5]}')
        print('-+-+-')
        print(f'{self.board[6]}|{self.board[7]}|{self.board[8]}')
    def get_valid_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
    def make_move(self, move):
        self.board[move] = self.current_player 
        self.current_player = 'O' if self.current_player == 'X' else 'X'

class MonteCarloAgent:
    def __init__(self):
        self.Q = {}
    def choose_move(self, state):
        valid_moves = state.get_valid_moves()
        if random.random() < 0.1:
            return random.choice(valid_moves)
        else:
            values = [self.Q.get((state, move), 0) for move in valid_moves]
            max_value = max(values)
            if values.count(max_value) > 1:
                best_moves = [i for i in range(len(valid_moves)) if values[i] == max_value]
                i = random.choice(best_moves)
            else:
                i = values.index(max_value)
            return valid_moves[i]
    def update_Q(self, episode):
        states, moves, rewards = zip(*episode)
        returns = 0
        for t in range(len(episode) - 1, -1, -1):
            returns += rewards[t]
            state = states[t]
            move = moves[t]
            if (state, move) in self.Q:
                self.Q[(state, move)] += returns - self.Q[(state, move)]
            else:
                self.Q[(state, move)] = returns
    def play_episode(self):
        episode = []
        state = TicTacToe()
        state.display_board() 
        while True:
            move = self.choose_move(state)
            episode.append((state, move, 0))
            state.make_move(move)
            if self.is_terminal(state):
                reward = self.get_reward(state)
                episode.append((state, None, reward))
                break
        self.update_Q(episode)
    def is_terminal(self, state):
        return self.get_reward(state) != 0 or len(state.get_valid_moves()) == 0
    def get_reward(self, state):
        if self.has_won(state, 'X'):
            return 1
        elif self.has_won(state, 'O'):
            return -1
        else:
            return 0
    def has_won(self, state, player):
        b = state.board
        return ((b[0] == player and b[1] == player and b[2] == player) or
                (b[3] == player and b[4] == player and b[5] == player) or
                (b[6] == player and b[7] == player and b[8] == player) or
                (b[0] == player and b[3] == player and b[6] == player) or
                (b[1] == player and b[4] == player and b[7] == player) or
                (b[2] == player and b[5] == player and b[8] == player) or
                (b[0] == player and b[4] == player and b[8] == player) or
                (b[2] == player and b[4] == player and b[6] == player))

    def train(self, num_episodes):
        for i in range(num_episodes):
            self.play_episode()
    def evaluate(self, num_games):
        wins = 0
        losses = 0
        draws = 0
        for i in range(num_games):
            state = TicTacToe()
            while True:
                if state.current_player == 'X':
                    move = self.choose_move(state)
                else:
                    move = random.choice(state.get_valid_moves())
                state.make_move(move)
                if self.is_terminal(state):
                    reward = self.get_reward(state)
                    if reward == 1:
                        wins += 1
                    elif reward == -1:
                        losses += 1
                    else:
                        draws += 1
                    break
        print(f'Wins: {wins}, Losses: {losses}, Draws: {draws}')

agent = MonteCarloAgent()
agent.train(10000)
agent.evaluate(100)