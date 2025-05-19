# COMP9001

# 🦍🐑 Customizable Othello Game (Command Line Version)

This is a Python-based command line Othello (Reversi) game where players can customize the appearance of their stones using fun emojis or symbols.  
It's a two-player game played on an 8x8 board with standard Reversi rules.

---

## 🎮 Features

- 8x8 Reversi board
- Turn-based gameplay (Black vs White)
- Customizable player stone appearance (choose from multiple emojis)
- Valid move checking and automatic stone flipping
- Live score tracking
- Coordinate-based input (e.g., `c4`, `e6`)
- Option to quit the game at any time

---

## 🧩 How to Play

1. When the game starts, each player selects their preferred stone design from a list of emoji options.
2. Players take turns entering a position in the format `rowcolumn` (e.g., `d3`, `e6`).
3. The board will update and flip opponent stones automatically based on the rules.
4. If a player has no valid moves, their turn is skipped.
5. The game ends when neither player has any valid moves left.
6. The player with the most stones wins!

---

## 🕹 Example

BLACK player, choose your stone:
	1. ⚫
	2. 🦍
	3. ⬛
	4. 💣
	5. 🐧
	6. 🎱
	7. 🌑

WHITE player, choose your stone:
	1. ⚪
	2. 🐑
	3. ⬜
	4. 👻
	5. 🍥
	6. 🕊️
	7. 🥚

The current board:
     1   2   3   4   5   6   7   8
    ────────────────────────────────
 a │ .   .   .   .   .   .   .   .  │
 b │ .   .   .   .   .   .   .   .  │
 c │ .   .   .   .   .   .   .   .  │
 d │ .   .   .   🐑  🦍   .   .   .  │
 e │ .   .   .   🦍  🐑   .   .   .  │
 f │ .   .   .   .   .   .   .   .  │
 g │ .   .   .   .   .   .   .   .  │
 h │ .   .   .   .   .   .   .   .  │
    ────────────────────────────────

---

## ▶ Requirements

- Python 3.x
- No external libraries needed

---

## 🚀 How to Run

1. Clone or download the repository
2. Make sure all files (`main.py`, `board.py`, `position.py`, `character.py`) are in the same folder
3. Run the game:

```bash
python3 main.py

project_folder/
├── main.py            # Game loop and player interaction
├── board.py           # Board logic and game rules
├── character.py       # Stone selection interface
├── position.py           # Helper functions (e.g., coordinate conversion)
└── README.md          # This file