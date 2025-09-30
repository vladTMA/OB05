# config.py
import pygame

# Размеры доски
BOARD_SIZE = 10
TILE_SIZE = 80
SCREEN_SIZE = BOARD_SIZE * TILE_SIZE
FPS = 60

MARGIN = 40
WINDOW_SIZE = BOARD_SIZE * TILE_SIZE + 2 * MARGIN

# Цвета доски и интерфейса
THEME = 'classic'  # или 'dark', 'blue', 'wood'

THEMES = {
    'classic': {
        'light': (240, 217, 181),
        'dark': (181, 136, 99),
        'selected': (0, 255, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
    },
    'dark': {
        'light': (60, 60, 60),
        'dark': (30, 30, 30),
        'selected': (255, 0, 0),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
    }
}

COLORS = THEMES[THEME]

# Используемые цвета
LIGHT = (190, 160, 120) # песочный цвет
DARK = (139, 69, 19) # коричневый цвет
SELECTED = (0, 255, 0)
UNDER_ATTACK = (255, 150, 150),   # светло-красный
IN_CHECK = (180, 0, 0),           # тёмно-красный
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

COLORS = {
    'light': (190, 160, 120),
    'dark': (139, 69, 19),
    'selected': (0, 255, 0),
    'under_attack': (255, 150, 150),
    'in_check': (180, 0, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
}

# Шрифт
FONT_NAME = "Segoe UI Symbol"
FONT_SIZE = 36

# Таймер
pygame.init()
clock = pygame.time.Clock()
clock.tick(FPS)

# Цвет основы
BACKGROUND = (101, 67, 33)  # тёмно-коричневый


