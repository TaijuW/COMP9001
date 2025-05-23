class Board:
    def __init__(self):
        self.rows = [[None] * 8 for _ in range(8)]
        center = 3
        self.rows[center][center] = 'w'
        self.rows[center][center+1] = 'b'
        self.rows[center+1][center] = 'b'
        self.rows[center+1][center+1] = 'w'

    def is_valid_move(self, row, col, color):
        # Check if the coordinates are within the 8×8 board
        if not (0 <= row < len(self.rows) and 0 <= col < len(self.rows[0])):
            raise ValueError("Move out of bounds.")

        # Ensure the target square is empty
        if self.rows[row][col] is not None:
            raise ValueError("This place is already taken.")

        # Prepare all eight directions to scan for flips
        directions = [
            (-1, -1), (-1,  0), (-1,  1),
            ( 0, -1),           ( 0,  1),
            ( 1, -1), ( 1,  0), ( 1,  1),
        ]

        valid = False
        for dx, dy in directions:
            # start at the adjacent square in this direction
            x, y = col + dx, row + dy

            # skip if out of bounds or empty
            if not (0 <= x < 8 and 0 <= y < 8):
                continue
            if self.rows[y][x] is None:
                continue

            # must be opponent’s stone first
            if self.rows[y][x] != color:
                # keep moving in the same direction
                x += dx
                y += dy
                while 0 <= x < 8 and 0 <= y < 8 and self.rows[y][x] is not None:
                    # if we find our own stone, it’s a valid flip
                    if self.rows[y][x] == color:
                        valid = True
                        break
                    x += dx
                    y += dy

        # If no direction yielded a flip, it’s not a legal move
        if not valid:
            raise ValueError("No discs to flip; invalid move.")

        return True
    
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

    def display(self, stone_config):
        print('\nThe current board:')
        print("     " + "   ".join(str(i+1) for i in range(8)))
        print("    " + "─" * 32)
        
        for i, row in enumerate(self.rows):
            print(f" {chr(97+i)} │", end="")  
            for cell in row:
                if cell == 'b':
                    print(f" {stone_config['b']} " , end="")  
                elif cell == 'w':
                    print(f" {stone_config['w']} ", end="")  
                else:
                    print(f" {stone_config['empty']}  ", end="")  
            print("│")  
        print("    " + "─" * 32)
        print()

