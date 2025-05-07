import sys

def main(lines):
    board = list(lines[0])
    moves = lines[1].strip()

    for turns, direction in enumerate(moves):
        if turns % 2 == 0:
            color = 'b'
        else:
            color = 'w'
        
        if direction == 'L':
            board.insert(0, color)
        elif direction == 'R':
            board.append(color)
        else:
            print(f'Invalid Direction: {direction}')
            return

        board = turn(board)

    black = board.count('b')
    white = board.count('w')
    print(f'{black} {white}')

def turn(board):
    n = len(board)
    i = 0

    while i < n:
        if board[i] == 'b' or board[i] == 'w':
            color = board[i]
            j = i + 1
            while j < n and board[j] != color:
                j += 1
            if j < n:
                for k in range(i+1, j):
                    board[k] = color
            i = j
        else:
            i += 1

    return board

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.strip('\r\n'))
    main(lines) 