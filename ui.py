# ui.py
import pygame
from config import TILE_SIZE, SCREEN_SIZE, BOARD_SIZE, LIGHT, DARK, SELECTED, BLACK, WHITE
from piece import Piece

from config import FONT_NAME, FONT_SIZE
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
COORD_FONT = pygame.font.SysFont(FONT_NAME, 14)

from config import COLORS

promotion_choices = ['♕', '♖', '♘', '♗', '♖♘', '♗♘']

def draw_board(screen, board, selected, highlighted, font, margin, under_attack, in_check):

    # Отрисовка клеток
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            rect = pygame.Rect(margin + x * TILE_SIZE, margin + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

            # базовый цвет
            color = COLORS['light'] if (x + y) % 2 == 0 else COLORS['dark']

            # подсветка шаха
            if in_check == (x, y):
                color = COLORS['in_check']

            # подсветка под ударом
            if (x, y) in under_attack:
                color = COLORS['under_attack']

            pygame.draw.rect(screen, color, rect)

            # подсветка выбранной клетки
            if (x, y) in highlighted or selected == (x, y):
                pygame.draw.rect(screen, COLORS['selected'], rect, 4)

    # Отрисовка фигур
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            piece = board[y][x]
            if piece:
                piece.draw(margin + x * TILE_SIZE, margin + y * TILE_SIZE, screen, font)

    # Координаты по горизонтали (буквы)
    for x in range(BOARD_SIZE):
        letter = chr(ord('A') + x)
        text = COORD_FONT.render(letter, True, COLORS['white'])

        # верх
        screen.blit(text, (
            margin + x * TILE_SIZE + TILE_SIZE // 2 - text.get_width() // 2,
            margin // 2 - text.get_height() // 2
        ))

        # низ
        screen.blit(text, (
            margin + x * TILE_SIZE + TILE_SIZE // 2 - text.get_width() // 2,
            margin + BOARD_SIZE * TILE_SIZE + margin // 2 - text.get_height() // 2
        ))

    # Координаты по вертикали (цифры)
    for y in range(BOARD_SIZE):
        number = str(BOARD_SIZE - y)
        text = COORD_FONT.render(number, True, COLORS['white'])

        # слева
        screen.blit(text, (
            margin // 2 - text.get_width() // 2,
            margin + y * TILE_SIZE + TILE_SIZE // 2 - text.get_height() // 2
        ))

        # справа
        screen.blit(text, (
            margin + BOARD_SIZE * TILE_SIZE + margin // 2 - text.get_width() // 2,
            margin + y * TILE_SIZE + TILE_SIZE // 2 - text.get_height() // 2
        ))

def draw_promotion_menu(screen, font, clock, color) -> str:
    menu_width = TILE_SIZE * len(promotion_choices)
    menu_height = TILE_SIZE
    menu_x = (SCREEN_SIZE - menu_width) // 2
    menu_y = (SCREEN_SIZE - menu_height) // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, symbol in enumerate(promotion_choices):
                    rect = pygame.Rect(menu_x + i * TILE_SIZE, menu_y, TILE_SIZE, TILE_SIZE)
                    if rect.collidepoint(mx, my):
                        return symbol

        screen.fill(BLACK)
        for i, symbol in enumerate(promotion_choices):
            rect = pygame.Rect(menu_x + i * TILE_SIZE, menu_y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, LIGHT, rect)
            pygame.draw.rect(screen, SELECTED, rect, 2)
            text = font.render(symbol, True, WHITE if color == 'white' else BLACK)
            screen.blit(text, (rect.x + 20, rect.y + 20))

        pygame.display.flip()
        clock.tick(60)
