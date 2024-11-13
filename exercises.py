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
            print(f" {row} |", end="")
            for col in ['a', 'b', 'c']:
                key = f"{col}{row}"
                value = self.board[key]
                if value is None:
                    print("   |", end="")
            else:
                print(f" {value} |", end="")
        print()
        print("  ---------")