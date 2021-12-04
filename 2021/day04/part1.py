with open("input", "r") as f:
    lines = f.readlines()

draw_numbers = None

class Board:

    def __init__(self, board, grid_len):
        self.grid_len = grid_len

        self.grid = [[(0,False) for j in range(grid_len)] for i in range(grid_len)]

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                self.grid[i][j] = (int(value), False)

    def mark_number(self, number):
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value[0] == number:
                    self.grid[i][j] = (value[0], True)

    def is_complete(self):
        for row in self.grid:
            if len([True for v in row if v[1] == True]) == len(row):
                return True
        for column in zip(*self.grid):
            if len([True for v in column if v[1] == True]) == len(column):
                return True
        return False

    def get_score(self, last_number):
        score = 0
        for row in self.grid:
            for value in row:
                if not value[1]:
                    score += value[0]
        return score * last_number


def mark_numbers(numbers):
    for number in draw_numbers:
        for board in boards:
            board.mark_number(number)
            if board.is_complete():
                return (board, number)

boards = []
current_board = []
for line in lines:
    line = line.strip()

    if draw_numbers is None:
        draw_numbers = line.split(",")
        draw_numbers = [int(v) for v in draw_numbers]
        continue

    if not line:
        # empty line between boards
        if len(current_board) == 5:
            boards.append(Board(current_board, 5))
        current_board = []
        continue
    
    current_board.append(line.split())

# one last time
boards.append(Board(current_board, 5))

(winner, last_number) = mark_numbers(draw_numbers)
if winner:
    print(winner.get_score(last_number))
