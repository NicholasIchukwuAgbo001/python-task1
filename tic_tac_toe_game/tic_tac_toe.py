from tic_tac_toe_game.current_state import CurrentState


class TicTacToe:
    def __init__(self):
        self.board = [[CurrentState.EMPTY for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(' '.join([str(cell.name) for cell in row]))

    def make_move(self, symbol, position):
        if position < 1 or position > 9:
            raise ValueError("Invalid position")
        row = (position - 1) // 3
        col = (position - 1) % 3
        if self.board[row][col] == CurrentState.EMPTY:
            self.board[row][col] = symbol

    def get_board(self):
        return self.board

    def check_winner(self):

        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != CurrentState.EMPTY:
                return row[0]


        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != CurrentState.EMPTY:
                return self.board[0][col]


        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != CurrentState.EMPTY:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != CurrentState.EMPTY:
            return self.board[0][2]

        return CurrentState.EMPTY

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == CurrentState.EMPTY:
                    return False
        return True

    def is_tie(self):
        return self.is_board_full() and self.check_winner() == CurrentState.EMPTY
