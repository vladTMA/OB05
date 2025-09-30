# piece.py
from typing import List, Tuple
from config import TILE_SIZE, BOARD_SIZE

class Piece:
    def __init__(self, symbol: str, color: str):
        self.symbol = symbol
        self.color = color
        self.has_moved = False

    def get_moves(self, x: int, y: int, board, last_move) -> List[Tuple[int, int]]:
        moves: List[Tuple[int, int]] = []

        def linear(directions: List[Tuple[int, int]]):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                    target = board[ny][nx]
                    if not target:
                        moves.append((nx, ny))
                    elif target.color != self.color:
                        moves.append((nx, ny))
                        break
                    else:
                        break
                    nx += dx
                    ny += dy

        # Конь
        if self.symbol in ['♞', '♘']:
            for dx, dy in [(1, 2), (2, 1), (-1, 2), (-2, 1),
                           (1, -2), (2, -1), (-1, -2), (-2, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                    target = board[ny][nx]
                    if not target or target.color != self.color:
                        moves.append((nx, ny))

        # Слон
        elif self.symbol in ['♝', '♗']:
            linear([(1, 1), (1, -1), (-1, 1), (-1, -1)])

        # Ладья
        elif self.symbol in ['♜', '♖']:
            linear([(1, 0), (-1, 0), (0, 1), (0, -1)])

        # Ферзь
        elif self.symbol in ['♛', '♕']:
            linear([(1, 0), (-1, 0), (0, 1), (0, -1),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)])

        # Король
        elif self.symbol in ['♚', '♔']:
            # обычные ходы
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                        target = board[ny][nx]
                        if not target or target.color != self.color:
                            moves.append((nx, ny))

            # Рокировка
            # длинная рокировка
            if all(board[y][i] is None for i in [1, 2, 3, 4]):
                rook = board[y][0]
                print(f"[CASTLING] Checking long castling for {self.symbol} at x={x}, y={y}")
                print(f"[CASTLING] Empty cells: {[board[y][i] for i in [1, 2, 3, 4]]}")
                print(f"[CASTLING] Rook at 0: {rook}")
                if rook:
                    print(f"[CASTLING] Rook symbol: {rook.symbol}, color: {rook.color}, has_moved: {rook.has_moved}")
                if rook and rook.symbol in ['♖', '♜'] and rook.color == self.color and not rook.has_moved:
                    moves.append((2, y))  # король идёт на c1

            # короткая рокировка
            if all(board[y][i] is None for i in [6, 7, 8]):
                rook = board[y][9]
                print(f"[CASTLING] Checking short castling for {self.symbol} at x={x}, y={y}")
                print(f"[CASTLING] Empty cells: {[board[y][i] for i in [6, 7, 8]]}")
                print(f"[CASTLING] Rook at 9: {rook}")
                if rook:
                    print(f"[CASTLING] Rook symbol: {rook.symbol}, color: {rook.color}, has_moved: {rook.has_moved}")
                if rook and rook.symbol in ['♖', '♜'] and rook.color == self.color and not rook.has_moved:
                    moves.append((8, y))  # король идёт на i1

        # Канцлер
        elif self.symbol in ['♜♞', '♖♘']:
            linear([(1, 0), (-1, 0), (0, 1), (0, -1)])
            for dx, dy in [(1, 2), (2, 1), (-1, 2), (-2, 1),
                           (1, -2), (2, -1), (-1, -2), (-2, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                    target = board[ny][nx]
                    if not target or target.color != self.color:
                        moves.append((nx, ny))

        # Архиепископ
        elif self.symbol in ['♝♞', '♗♘']:
            linear([(1, 1), (1, -1), (-1, 1), (-1, -1)])
            for dx, dy in [(1, 2), (2, 1), (-1, 2), (-2, 1),
                           (1, -2), (2, -1), (-1, -2), (-2, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                    target = board[ny][nx]
                    if not target or target.color != self.color:
                        moves.append((nx, ny))

        # Пешка (белая)
        elif self.symbol == '♙':
            # Прямой ход
            if y == 8:
                for step in range(1, 4):
                    ny = y - step
                    if ny >= 0 and not board[ny][x]:
                        moves.append((x, ny))
                    else:
                        break
            elif y - 1 >= 0 and not board[y - 1][x]:
                moves.append((x, y - 1))

            # Взятие по диагонали
            for dx in [-1, 1]:
                nx, ny = x + dx, y - 1
                if 0 <= nx < BOARD_SIZE and ny >= 0:
                    target = board[ny][nx]
                    if target and target.color != self.color:
                        moves.append((nx, ny))

            # Взятие на проходе
            if last_move:
                for dx in [-1, 1]:
                    tx = x + dx
                    ty = y - 1
                    if 0 <= tx < BOARD_SIZE and 0 <= ty < BOARD_SIZE:
                        if self.is_en_passant(x, y, tx, ty, board, last_move):
                            moves.append((tx, ty))
        # Пешка (чёрная)
        elif self.symbol == '♟':
            # Прямой ход
            if y == 1:
                for step in range(1, 4):
                    ny = y + step
                    if ny < BOARD_SIZE and not board[ny][x]:
                        moves.append((x, ny))
                    else:
                        break
            elif y + 1 < BOARD_SIZE and not board[y + 1][x]:
                moves.append((x, y + 1))

            # Взятие по диагонали
            for dx in [-1, 1]:
                nx, ny = x + dx, y + 1
                if 0 <= nx < BOARD_SIZE and ny < BOARD_SIZE:
                    target = board[ny][nx]
                    if target and target.color != self.color:
                        moves.append((nx, ny))

            # Взятие на проходе
            if last_move:
                for dx in [-1, 1]:
                    tx = x + dx
                    ty = y + 1
                    if 0 <= tx < BOARD_SIZE and 0 <= ty < BOARD_SIZE:
                        if self.is_en_passant(x, y, tx, ty, board, last_move):
                            moves.append((tx, ty))

        return moves

    def is_en_passant(self, x, y, target_x, target_y, board, last_move) -> bool:
        if not last_move:
            return False

        last_piece = last_move['piece']
        from_x, from_y = last_move['from']
        to_x, to_y = last_move['to']

        if last_piece.symbol not in ['♙', '♟']:
            return False
        if last_piece.color == self.color:
            return False

        delta = abs(to_y - from_y)
        if delta not in [2, 3]:
            return False
        if abs(to_x - x) != 1:
            return False

        # Вариант A — классическое взятие на проходе
        if self.symbol == '♙' and y == 4 and to_y == 4 and target_y == 3:
            if target_x == to_x and board[target_y][target_x] is None:
                return True
        if self.symbol == '♟' and y == 5 and to_y == 5 and target_y == 6:
            if target_x == to_x and board[target_y][target_x] is None:
                return True

        # Вариант B.1 — взятие по клетке, куда пешка пришла после прыжка
        if self.symbol == '♙' and y == 3 and delta == 3 and to_y == 4 and target_y == 2:
            if target_x == to_x and board[target_y][target_x] is None:
                return True
        if self.symbol == '♟' and y == 6 and delta == 3 and to_y == 5 and target_y == 7:
            if target_x == to_x and board[target_y][target_x] is None:
                return True

        # Вариант B.2 — взятие по клетке, которую пешка прошла
        if self.symbol == '♙' and y == 3 and delta == 2 and to_y == 3 and target_y == 2:
            if target_x == to_x and board[target_y][target_x] is None:
                return True
        if self.symbol == '♟' and y == 6 and delta == 2 and to_y == 6 and target_y == 7:
            if target_x == to_x and board[target_y][target_x] is None:
                return True

        return False

    def draw(self, x: int, y: int, screen, font):
        color = (255, 255, 255) if self.color == 'white' else (0, 0, 0)
        text = font.render(self.symbol, True, color)
        screen.blit(text, (
            x + TILE_SIZE // 2 - text.get_width() // 2,
            y + TILE_SIZE // 2 - text.get_height() // 2
        ))

