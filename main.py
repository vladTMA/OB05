# main.py
# Инициализируем Pygame
import pygame
pygame.init()

from board import initialize_board
from config import FONT_NAME, FONT_SIZE, TILE_SIZE, BOARD_SIZE, WINDOW_SIZE, FPS, BLACK, clock, MARGIN
from ui import draw_board, draw_promotion_menu
from config import MARGIN

from config import COLORS
LIGHT = COLORS['light']
DARK = COLORS['dark']
SELECTED = COLORS['selected']

BACKGROUND = (101, 67, 33)  # тёмно-коричневый

# Шрифт и экран
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Capablanca Chess 10x10")

# Инициализация доски
board = initialize_board()
selected = None
last_move = None

# Основной цикл
running = True
while running:
    screen.fill(BACKGROUND)

    # Подсветка доступных ходов
    highlighted = []
    if selected:
        sel_x, sel_y = selected
        piece = board[sel_y][sel_x]
        if piece:
            highlighted = piece.get_moves(sel_x, sel_y, board, last_move)

    selected_color = (
        'black' if last_move and last_move.get('piece') and last_move['piece'].color == 'white'
        else 'white'
        )

    under_attack = []
    in_check = None

    # клетки с подсветкой
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            piece = board[y][x]
            if piece and piece.color != selected_color:
                moves = piece.get_moves(x, y, board, last_move)
                for mx, my in moves:
                    target = board[my][mx]
                    if target and target.color == selected_color:
                        under_attack.append((mx, my))
                        # проверка шаха
                        if target and target.symbol in ['♔', '♚'] and target.color == selected_color:
                            in_check = (mx, my)

        # Отрисовка доски, фигур и координат
    draw_board(screen, board, selected, highlighted, font, MARGIN, under_attack, in_check)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            cx, cy = (mx - MARGIN) // TILE_SIZE, (my - MARGIN) // TILE_SIZE

            if cx >= BOARD_SIZE or cy >= BOARD_SIZE:
                continue  # Клик вне доски

            if selected:
                from_x, from_y = selected
                moving_piece = board[from_y][from_x]
                target_piece = board[cy][cx]

                if (cx, cy) in moving_piece.get_moves(from_x, from_y, board, last_move):

                    # Взятие на проходе
                    if moving_piece.symbol in ['♙', '♟']:
                        if target_piece is None and cx != from_x:
                            if moving_piece.is_en_passant(from_x, from_y, cx, cy, board, last_move):
                                direction = -1 if moving_piece.symbol == '♙' else 1
                                captured_y = cy - direction
                                board[captured_y][cx] = None
                                print("[MAIN] En passant triggered")

                    # Рокировка
                    if moving_piece.symbol in ['♔', '♚'] and abs(cx - from_x) == 3:
                        if cx < from_x: # длинная рокировка
                            rook_from = 0
                            rook_to = cx + 1
                        else: # короткая рокировка
                            rook_from = from_x + 4 # x = 5 → ладья на x = 9
                            rook_to = cx - 1       # король на x = 8 → ладья на x = 7

                        rook = board[from_y][rook_from]  # извлекаем ладью

                        # условия рокировки
                        if rook and rook.symbol in ['♖',
                                                    '♜'] and rook.color == moving_piece.color and not rook.has_moved:
                            board[from_y][rook_to] = rook
                            board[from_y][rook_from] = None
                            rook.has_moved = True
                        else:
                            print("[CASTLING] ❌ Rook not eligible")

                    # Превращение пешки
                    if moving_piece.symbol in ['♙', '♟']:
                        if (moving_piece.symbol == '♙' and cy == 0) or (moving_piece.symbol == '♟' and cy == 9):
                            chosen = draw_promotion_menu(screen, font, clock, moving_piece.color)
                            moving_piece.symbol = chosen

                    # Перемещение фигуры
                    board[cy][cx] = moving_piece
                    board[from_y][from_x] = None
                    moving_piece.has_moved = True

                    last_move = {
                        'from': (from_x, from_y),
                        'to': (cx, cy),
                        'piece': moving_piece,
                    }

                    selected = None
                else:
                    selected = None

            elif board[cy][cx]:
                selected = (cx, cy)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
