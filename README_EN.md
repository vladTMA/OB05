# Capablanca Chess 10x10

A Capablanca Chess game on a 10x10 board with a graphical interface built in Python using Pygame.

## Description

This is an implementation of Capablanca Chess - a chess variant with an enlarged 10x10 board and additional pieces. The game includes all classical chess rules plus special rules for the new pieces.

## Features

- **10x10 Board**: Extended chess board with additional squares
- **Additional Pieces**:
  - **Chancellor** (♜♞/♖♘): Combination of rook and knight
  - **Archbishop** (♝♞/♗♘): Combination of bishop and knight
- **Classical Rules**: All standard chess rules are preserved
- **Special Moves**:
  - Castling (long and short)
  - En passant capture
  - Pawn promotion
- **Visual Effects**:
  - Available moves highlighting
  - Under attack squares highlighting
  - Check highlighting
  - Coordinate grid

## Project Structure

```
OB05/
├── main.py          # Main game file
├── board.py         # Board initialization
├── piece.py         # Piece logic and move calculations
├── ui.py           # Graphical interface
├── config.py       # Game configuration
└── README_EN.md    # Documentation (English)
```

## Installation and Running

### Requirements

- Python 3.7+
- Pygame

### Installing Dependencies

```bash
pip install pygame
```

### Running the Game

```bash
python main.py
```

## Controls

- **Select Piece**: Left-click on a piece
- **Make Move**: Click on an available square (highlighted in green)
- **Cancel Selection**: Click on an empty square or another piece

## Game Rules

### Initial Setup

```
a  b  c  d  e  f  g  h  i  j
10 ♜ ♞ ♝♞ ♝ ♛ ♚ ♝ ♜♞ ♞ ♜
9  ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
8  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
7  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
6  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
5  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
4  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
3  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
2  ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
1  ♖ ♘ ♗♘ ♗ ♕ ♔ ♗ ♖♘ ♘ ♖
```

### Pieces

| Piece | Symbol | Description |
|-------|--------|-------------|
| Pawn | ♙/♟ | Can move 1-3 squares forward from starting position |
| Knight | ♘/♞ | Moves in L-shape |
| Bishop | ♗/♝ | Moves diagonally |
| Rook | ♖/♜ | Moves horizontally and vertically |
| Queen | ♕/♛ | Combination of rook and bishop |
| King | ♔/♚ | Moves one square in any direction |
| Chancellor | ♖♘/♜♞ | Combination of rook and knight |
| Archbishop | ♗♘/♝♞ | Combination of bishop and knight |

### Special Rules

- **Castling**: King can castle with rook (long and short)
- **En Passant**: Pawn can capture opponent's pawn "en passant"
- **Pawn Promotion**: When reaching the last rank, pawn promotes to any piece

## Technical Details

- **Language**: Python 3.7+
- **Graphics Library**: Pygame
- **Architecture**: Modular structure with separation of logic and interface
- **Window Size**: 880x880 pixels
- **Frame Rate**: 60 FPS

## Development Plans

- Animation of moves and captures
- Support for SVG shapes
- Saving and loading games

## Author

Project created as part of learning Python programming and game development.

## License

This project is intended for educational purposes.
