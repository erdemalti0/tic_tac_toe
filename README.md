# Tic-Tac-Toe Game

This Python program is a simple implementation of the classic Tic-Tac-Toe game, where the player competes against the computer. The game allows for turn-based moves and checks for winning conditions or a tie after each move.

## Features

- **Player vs Computer**: You play against an AI that randomly selects its moves.
- **Customizable Symbols**: Player and computer are assigned symbols (`X` or `O`) based on who starts first.
- **Win/Tie Detection**: Automatically detects and announces if there is a winner or the game ends in a tie.
- **Exit Option**: Players can exit the game anytime by entering `00`.

## How It Works

1. **Start of the Game**:
   - The game randomly decides whether the player or the computer starts.
   - Symbols (`X` or `O`) are assigned accordingly.

2. **Player Input**:
   - The player enters their move as a combination of a row number (1, 2, or 3) and a column letter (`a`, `b`, or `c`). For example, `1a` for the top-left corner.

3. **Computer's Turn**:
   - The computer randomly selects an empty cell for its move.

4. **Winning Conditions**:
   - A player wins if they get three of their symbols in a row, column, or diagonal.

5. **Tie Condition**:
   - If all cells are filled and no player has won, the game ends in a tie.

6. **Exit Option**:
   - The player can exit the game at any time by entering `00`.

## Functions

### `read_the_player_move()`
- Handles player's input, validates the move, and updates the game board.

### `read_the_computer_move()`
- Generates a random move for the computer and updates the board.

### `win_or_tie()`
- Checks the board for winning conditions or a tie after every move.

### `draw_the_game()`
- Displays the current state of the game board in a visually appealing format.

## Example Gameplay

```
Welcome to Game of Tic-Tac-Toe
By Yusuf Erdem ALTINSOY
------------------------------
You will start the game
------------------------------
     |  a  |  b  |  c  |
-----+-----+-----+-----|
  1  |     |     |     |
-----+-----+-----+-----|
  2  |     |     |     |
-----+-----+-----+-----|
  3  |     |     |     |
-----------------------|
Your move (Enter 00 to Exit)? 1a
```

## How to Run

1. Copy the script into a Python file (e.g., `tic_tac_toe.py`).
2. Run the script using Python 3.x.
3. Follow the on-screen instructions to play the game.

---
Developed by **Yusuf Erdem Altınsoy**

