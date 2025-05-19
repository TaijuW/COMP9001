from board import Board
from character import choose_stone
from position import convert_position

def main():
    #  Stone selection
    b_options = ["⚫", "🦍", "⬛", "💣", "🐧", "🎱", "🌑"]
    w_options = ["⚪", "🐑", "⬜", "👻", "🍥", "🕊️ ", "🥚"]
    b_stone = choose_stone("black", b_options)
    w_stone = choose_stone("white", w_options)

    stone_display = {"b": b_stone, "w": w_stone, "empty": "."}

    board = Board()
    turn = 0

    print(f'\nStarting the game! Black: {b_stone}, White: {w_stone}')
    print('Enter coordinates in "row-column" format (e.g., a1, b3, h8)')
    print("Type 'q' to quit the game.")
    board.display(stone_display)

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
            board.display(stone_display)

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