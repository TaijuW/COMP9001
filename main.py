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
    pass_count = 0       # count how many turns in a row had no moves

    print(f'\nStarting the game! Black: {b_stone}, White: {w_stone}')

    board.display(stone_display)

    while True:
        #　Calculate valid moves for both players
        moves_b = board.get_valid_moves('b')
        moves_w = board.get_valid_moves('w')

        # If neither player can move, end the game immediately
        if not moves_b and not moves_w:
            break

        # Determine the current player
        color       = 'b' if turn % 2 == 0 else 'w'
        player      = 'Black' if color == 'b' else 'White'
        valid_moves = moves_b if color == 'b' else moves_w

        # If this player has no valid moves, skip 
        if not valid_moves:
            print(f"{player} has no valid moves. Skipping turn.")
            turn += 1
            continue

        # Normal turn flow: show options → get input → update board → display score → advance turn
        valid_positions = [
            f"{chr(r + ord('a'))}{c + 1}"
            for r, c in valid_moves
        ]
        print(f"Valid moves: {', '.join(valid_positions)}")

        move = input(f"\n{player}'s turn > ").strip().lower()
        if move == 'q':
            break

        try:
            row, col = convert_position(move)
            board.place_stone(row, col, color)
            board.display(stone_display)

            black, white = board.count_colors()
            print(f"Current Score - Black: {black}, White: {white}")

            turn += 1
        except ValueError as e:
            print(f"Error: {e}")
            continue


    #  end of game, show final result 
    black, white = board.count_colors()
    print(f"\nGame over! Final Score — Black: {black}, White: {white}")
    if black > white:
        print("Black wins!")
    elif white > black:
        print("White wins!")
    else:
        print("Draw!")

if __name__ == '__main__':
    main()  