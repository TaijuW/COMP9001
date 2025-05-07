class Board:
    def __init__(self):
        # 8x8のボードを作成
        self.rows = [[None] * 8 for _ in range(8)]
        # 初期配置（中央の4マス）
        center = 3
        self.rows[center][center] = 'w'
        self.rows[center][center+1] = 'b'
        self.rows[center+1][center] = 'b'
        self.rows[center+1][center+1] = 'w'
        
    def is_valid_move(self, row, col, color):
        # すでに石が置かれている場合は無効
        if self.rows[row][col] is not None:
            raise ValueError("すでに石が置かれています")

        # 8方向の差分
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        valid = False
        for dx, dy in directions:
            # 隣接するマスをチェック
            x, y = row + dx, col + dy
            if not (0 <= x < 8 and 0 <= y < 8):
                continue
            if self.rows[x][y] is None:
                continue
                
            # 相手の石が隣接している場合、その方向をさらにチェック
            if self.rows[x][y] != color:
                x += dx
                y += dy
                while 0 <= x < 8 and 0 <= y < 8 and self.rows[x][y] is not None:
                    if self.rows[x][y] == color:
                        valid = True
                        break
                    x += dx
                    y += dy

        if not valid:
            raise ValueError("ここには置けません（相手の石を挟めません）")
        return True

    def place_stone(self, row, col, color):
        if self.is_valid_move(row, col, color):
            self.rows[row][col] = color
            self._flip_stones(row, col, color)
    
    def _flip_stones(self, row, col, color):
        """置いた石に隣接する相手の石を反転させる"""
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for dx, dy in directions:
            stones_to_flip = []
            x, y = row + dx, col + dy
            
            # その方向に石を探索
            while 0 <= x < 8 and 0 <= y < 8 and self.rows[x][y] is not None:
                if self.rows[x][y] == color:
                    # 自分の石が見つかったら、間の石を反転
                    for flip_x, flip_y in stones_to_flip:
                        self.rows[flip_x][flip_y] = color
                    break
                else:
                    # 相手の石を記録
                    stones_to_flip.append((x, y))
                x += dx
                y += dy
    
    def count_colors(self):
        black = sum(1 for row in self.rows for cell in row if cell == 'b')
        white = sum(1 for row in self.rows for cell in row if cell == 'w')
        return black, white

    def get_valid_moves(self, color):
        """指定した色の石が置ける場所のリストを返す"""
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
        """ボードの状態を視覚的に表示"""
        print("\n現在のボード状態:")
        # 列番号を表示（1-8）
        print("     " + "    ".join(str(i+1) for i in range(8)))
        print("    " + "─" * 38)
        # ボードの内容を表示（a-h）
        for i, row in enumerate(self.rows):
            print(f" {chr(97+i)} │", end="")
            for cell in row:
                if cell == 'b':
                    print(" ●   ", end="")  # 黒を●に修正
                elif cell == 'w':
                    print(" ○   ", end="")  # 白を○に修正
                else:
                    print(" ・  ", end="")
            print("│")
        print("    " + "─" * 38)
        print()

def convert_position(pos):
    """入力された位置（例：'a1'）を行と列の添字に変換"""
    if len(pos) != 2:
        raise ValueError("無効な入力です")
    
    try:
        row = ord(pos[0].lower()) - ord('a')
        col = int(pos[1]) - 1
    except ValueError:
        raise ValueError("無効な入力形式です（例：a1, b3, h8）")
    
    if not (0 <= row < 8 and 0 <= col < 8):
        raise ValueError("無効な位置です（a1からh8の範囲で指定してください）")
    
    return row, col

def main():
    board = Board()
    turn = 0
    
    print("オセロゲームを開始します！")
    print("座標を「行列」の形式で入力してください（例：a1, b3, h8）")
    print("終了するには 'q' を入力してください")
    
    board.display()

    while True:
        color = 'b' if turn % 2 == 0 else 'w'  # 黒から始める
        player = 'Black' if color == 'b' else 'White'  # 日本語表示に統一
        
        # 置ける場所があるかチェック
        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            print(f"{player}の置ける場所がありません。スキップします。")
            turn += 1
            continue
        
        # 置ける場所を表示
        valid_positions = [f"{chr(row + ord('a'))}{col + 1}" for row, col in valid_moves]
        print(f"置ける場所: {', '.join(valid_positions)}")
        
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

# このコードが動かない理由は、`main()` 関数が定義されていないためです。
def main():
    print("終了するには 'q' を入力してください")
    
    board.display()

    turn = 0
    while True:
        color = 'b' if turn % 2 == 0 else 'w'  # 黒から始める
        player = 'Black' if color == 'b' else 'White'  # 日本語表示に統一
        
        # 置ける場所があるかチェック
        valid_moves = board.get_valid_moves(color)
        if not valid_moves:
            print(f"{player}の置ける場所がありません。スキップします。")
            turn += 1
            continue
        
        # 置ける場所を表示
        valid_positions = [f"{chr(row + ord('a'))}{col + 1}" for row, col in valid_moves]
        print(f"置ける場所: {', '.join(valid_positions)}")
        
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