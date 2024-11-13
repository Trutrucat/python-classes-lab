class Game:
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }

    def welcome_message(self):
        print("Welcome to Tic-Tac-Toe!")

    def print_board(self):
        print("  A | B | C")
        print("  ---------")
        for row in ['1', '2', '3']:
            for col in ['a', 'b', 'c']:
                key = f"{col}{row}"
                value = self.board[key]
                if value is None:
                    print("   |", end="")
                else:
                    print(f" {value} |", end="")
            print()
            if row != '3':
                print("  ---------")

    def get_move(self):
        while True:
            move = input(f"It's player {self.turn}'s turn. Enter a valid move (example: A1): ").strip().lower()
            if len(move) != 2:
                print("Invalid move. Please enter a letter and a number (e.g. A1).")
                continue
            col, row = move
            if col not in 'abc' or row not in '123':
                print("Invalid move. Please enter a letter between A and C and a number between 1 and 3.")
                continue
            key = f"{col}{row}"
            if self.board[key] is not None:
                print("Invalid move. That cell is already occupied.")
                continue
            return key

    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def play_game(self):
        self.welcome_message()
        while True:
            self.print_board()
            move = self.get_move()
            self.board[move] = self.turn
            if self.check_for_winner():
                self.print_board()
                print(f"Player {self.turn} wins!")
                break
            elif self.check_for_tie():
                self.print_board()
                print("It's a tie!")
                break
            self.switch_turn()

    def check_for_winner(self):
        # Check rows
        for row in ['1', '2', '3']:
            if self.board['a' + row] == self.board['b' + row] == self.board['c' + row] and self.board['a' + row] is not None:
                self.winner = self.board['a' + row]
                return True

        # Check columns
        for col in ['a', 'b', 'c']:
            if self.board[col + '1'] == self.board[col + '2'] == self.board[col + '3'] and self.board[col + '1'] is not None:
                self.winner = self.board[col + '1']
                return True

        # Check diagonals
        if self.board['a1'] == self.board['b2'] == self.board['c3'] and self.board['a1'] is not None:
            self.winner = self.board['a1']
            return True
        if self.board['c1'] == self.board['b2'] == self.board['a3'] and self.board['c1'] is not None:
            self.winner = self.board['c1']
            return True

        return False

    def check_for_tie(self):
        for key in self.board:
            if self.board[key] is None:
                return False
        self.tie = True
        return True

if __name__ == "__main__":
    game = Game()
    game.play_game()