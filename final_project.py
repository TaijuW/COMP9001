class Board:
    def __init__(self):
        self.rows = [[None] * 8 for _ in range(8)]
        center = 3
        self.rows[center][center] = 'w'
        self.rows[center][center+1] = 'b'
        self.rows[center+1][center] = 'b'
        self.rows[center+1][center+1] = 'w'

    def is_valid_move(self, row, col, color):
        if self.rows[row][col] is not None:
            raise ValueError('This place is alrady taken.')
    
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1), (1, -1),
            (1, 0), (1, 1)
        ]

        valid = False
        for dx, dy in directions:
            # Check adjacent squares
            x, y = col + dx, row + dy
            if not (0 <= x < 8 and 0 <= y < 8):
                continue
            if self.rows[y][x] is None:
                continue

            # Check if opponent's stone is adjacent
            if self.rows[y][x] != color:
                x += dx
                y += dy
                while 0 <= x < 8 and 0 <= y < 8 and self.rows[y][x] is not None:
                    if self.rows[y][x] == color:
                        valid = True
                        break
                    x += dx
                    y += dy

        if not valid:
            raise ValueError('You cannot place the stone here.')
        return valid
    
    def place_stone(self, row, col, color):
        if self.is_valid_move(row, col, color):
            self.rows[row][col] = color
            self._flip_stones(row, col, color)
    
    def _flip_stones(self, row, col, color):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1), (1, -1),
            (1, 0), (1, 1)
        ]

        for dx, dy in directions:
            stones_to_flip = []
            x, y = col + dx, row + dy

            # Search for stones to flip in this direction
            while 0 <= x < 8 and 0 <= y < 8 and self.rows[y][x] is not None:
                if self.rows[y][x] == color:
                    # Flip all opponent's stones between current and found stone
                    for flip_x, flip_y in stones_to_flip:
                        self.rows[flip_y][flip_x] = color
                    break
                else:
                    # Add opponent's stone to flip list
                    stones_to_flip.append((x, y))
                x += dx
                y += dy

    def count_colors(self):
        # Count black and white stones
        black = sum(1 for row in self.rows for cell in row if cell == 'b')
        white = sum(1 for row in self.rows for cell in row if cell == 'w')
        return black, white

    def get_valid_moves(self, color):
        # Find all valid moves for the current player
        valid_moves = []
        for i in range(8):
            for j in range(8):
                if self.rows[i][j] is None:
                    try:
                        if self.is_valid_move(i, j, color):
                            valid_moves.append((i, j))
                    except ValueError:
                        continue
        return valid_moves
    
    def display(self):
        # Display the current board state
        print('\nThe current board:')
        print("     " + "    ".join(str(i+1) for i in range(8)))
        print("    " + "─" * 40)
        for i, row in enumerate(self.rows):
            print(f" {chr(97+i)} │", end="")
            for cell in row:
                if cell == 'b':
                    print(" ●   ", end="")  # Black stone
                elif cell == 'w':
                    print(" ○   ", end="")  # White stone
                else:
                    print(" ・  ", end="")  # Empty cell
            print("│")
        print("    " + "─" * 40)
        print()

def convert_position(pos):
    # Validate input format
    if len(pos) != 2:
        raise ValueError('Expected example: a1, b2, e3')
    
    try:
        # Convert letter to row number (a=0, b=1, etc.)
        row = ord(pos[0].lower()) - ord('a')
        # Convert number to column number (1=0, 2=1, etc.)
        col = int(pos[1]) - 1
    except ValueError:
        raise ValueError('Invalid place: Select from a1 to h8')
    
    return row, col
    

def main():
    board = Board()
    turn = 0

    print('Starting the game! Black: ●, White: ○')
    print('Enter coordinates in "row-column" format (e.g., a1, b3, h8)')
    print("Type 'q' to quit the game.")

    board.display()

    while True:
        color = 'b' if turn % 2 == 0 else 'w'
        player = 'Black' if color == 'b' else 'White'

        # Check if there are any valid moves
        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            print(f"{player} has no valid moves. Skipping turn.")
            turn += 1
            continue

        # Displaying all valid moves
        valid_positions = [f"{chr(row + ord('a'))}{col + 1}" for row, col in valid_moves]
        print(f"Valid moves: {', '.join(valid_positions)}")

        move = input(f"\n{player}'s turn > ").strip()

        if move.lower() == 'q':
            break

        try:
            row, col = convert_position(move)
            board.place_stone(row, col, color)
            board.display()

            black, white = board.count_colors()
            print(f"Current Score - Black: {black}, White: {white}")

            turn += 1

        except ValueError as e:
            print(f"Error: {str(e)}")
            continue

    black, white = board.count_colors()
    print(f"\nResult:")
    print(f"Black: {black}")
    print(f"White: {white}")
    if black > white:
        print("Black wins！")
    elif white > black:
        print("White wins！")
    else:
        print("Draw！")

if __name__ == '__main__':
    main()  