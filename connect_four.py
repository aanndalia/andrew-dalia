class Player:
    def __init__(self, is_x, name):
        self.is_x = is_x
        self.name = name


class Game:
    def __init__(self, player1_name, player2_name, dim=10, seq_len=4):
        if dim <= seq_len:
            raise AttributeError('Dimensions of board must be at least as large as sequence length')

        self.player1 = Player(True, player1_name)
        self.player2 = Player(False, player2_name)
        self.dim = dim
        self.seq_len = seq_len
        self.turn = self.player1
        self.board = self.init_board()
        self.last_row_played_by_column = [-1 for _ in range(self.dim)]
        self.winner = None

    def init_board(self):
        board = []
        for r in range(self.dim):
            board.append([None for _ in range(self.dim)])

        return board

    def change_turn(self):
        self.turn = self.player1 if self.turn == self.player2 else self.player2

    def play_turn(self):
        self.print_board()
        self.process_move()
        self.check_winner()
        self.change_turn()

    def check_winner(self):
        for r in range(self.dim):
            for c in range(self.dim):
                if self.check_sequence_win(r, c):
                    self.winner = self.turn
                    return

    def check_sequence_win(self, row, col):
        value_check = self.turn.is_x
        col_check = True
        row_check = True
        diagonal_forward_check = True
        diagonal_backward_check = True
        for i in range(self.seq_len):
            if col_check and (not self.in_range(row, col + i) or self.board[row][col + i] != value_check):
                col_check = False

            if row_check and (not self.in_range(row + i, col) or self.board[row + i][col] != value_check):
                row_check = False

            if diagonal_forward_check and (not self.in_range(row + i, col + i) or self.board[row + i][col + i] != value_check):
                diagonal_forward_check = False

            if diagonal_backward_check and (not self.in_range(row - i, col - i) or self.board[row - i][col - i] != value_check):
                diagonal_backward_check = False

        check = col_check or row_check or diagonal_backward_check or diagonal_forward_check
        return check

    def in_range(self, row, col):
        if row < 0 or row >= self.dim or col < 0 or col >= self.dim:
            return False

        return True

    def process_move(self):
        column_choice = self.get_choice()
        while not self.is_valid_move(column_choice):
            column_choice = self.get_choice()

        last_row_played_in_column = self.last_row_played_by_column[column_choice]
        self.board[last_row_played_in_column + 1][column_choice] = True if self.turn.is_x else False
        self.last_row_played_by_column[column_choice] = self.last_row_played_by_column[column_choice] + 1

    def get_choice(self):
        raw_choice = input(f'{self.turn.name}: Which column would you like to place a piece? ')
        column_choice = int(raw_choice)
        return column_choice

    def is_valid_move(self, col_choice):
        if not isinstance(col_choice, int):
            return False

        if col_choice < 0 or col_choice >= self.dim:
            return False

        if self.board[self.dim-1][col_choice] is not None:
            return False

        return True

    def print_board(self):
        print('  '.join([str(idx) for idx in range(self.dim)]))
        print()
        for r in range(self.dim - 1, -1, -1):
            print('  '.join(map(lambda x: ' ' if x is None else ('X' if x else 'O'), self.board[r])))

        print('\n\n')

    def play(self):
        while not self.winner:
            self.play_turn()

        self.print_board()
        print(f'{self.winner.name} Wins!')


def main():
    player1_name = input('Player 1 name: ')
    player2_name = input('Player 2 name: ')
    dim = int(input('Enter n dimension of n x n grid: '))
    seq_len = int(input('Enter sequence length: '))
    game = Game(player1_name, player2_name, dim, seq_len)
    game.play()

main()


