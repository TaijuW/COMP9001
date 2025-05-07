import sys

class Board:
    def __init__(self, initial_state=None):
        if initial_state is None or initial_state == "2x2":
            # 通常のオセロの初期配置（2x2）
            self.rows = [
                ['w', 'b'],
                ['b', 'w']
            ]
        else:
            # 1行からの入力の場合（後方互換性のため）
            self.rows = [[c] for c in initial_state]
        
    def move(self, direction, color):
        if direction == 'L':
            for row in self.rows:
                row.insert(0, color)
        elif direction == 'R':
            for row in self.rows:
                row.append(color)
        elif direction == 'U':
            new_row = [color] * len(self.rows[0])
            self.rows.insert(0, new_row)
        elif direction == 'D':
            new_row = [color] * len(self.rows[0])
            self.rows.append(new_row)
    
    def turn(self):
        # 横方向の処理
        for row in self.rows:
            self._turn_line(row)
        
        # 縦方向の処理
        for col in range(len(self.rows[0])):
            column = [row[col] for row in self.rows]
            self._turn_line(column)
            # 更新された列を元のボードに反映
            for i, value in enumerate(column):
                self.rows[i][col] = value
    
    def _turn_line(self, line):
        n = len(line)
        i = 0
        while i < n:
            if line[i] in ['b', 'w']:
                color = line[i]
                j = i + 1
                while j < n and line[j] != color:
                    j += 1
                if j < n:
                    for k in range(i+1, j):
                        line[k] = color
                i = j
            else:
                i += 1
    
    def count_colors(self):
        black = sum(row.count('b') for row in self.rows)
        white = sum(row.count('w') for row in self.rows)
        return black, white
    
    def display(self):
        """ボードの状態を視覚的に表示"""
        print("\n現在のボード状態:")
        for row in self.rows:
            print(' '.join(row).replace('b', '●').replace('w', '○'))
        print()

def main(lines):
    # 最初の行が "2x2" の場合は標準の2x2初期配置を使用
    initial_state = lines[0].strip()
    board = Board(initial_state)
    moves = lines[1].strip()
    
    print("初期状態:")
    board.display()

    for turns, direction in enumerate(moves):
        color = 'b' if turns % 2 == 0 else 'w'
        player = '黒' if color == 'b' else '白'
        
        if direction in ['L', 'R', 'U', 'D']:
            print(f"\n手番{turns + 1}: {player}の手番 - {direction}方向")
            board.move(direction, color)
            board.turn()
            board.display()
        else:
            print(f'無効な方向です: {direction}')
            return

    black, white = board.count_colors()
    print(f"\n最終結果:")
    print(f"黒: {black}")
    print(f"白: {white}")
    print(f"{black} {white}")  # 元の出力形式も維持

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.strip('\r\n'))
    main(lines) 