import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 253, 208)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
GREEN = (1, 150, 32)
DARKGREEN = (1, 120, 30)

CROWN = pygame.transform.scale(pygame.image.load('checkers/yellow-k3.webp'), (45, 45))
LFC = pygame.transform.scale(pygame.image.load('checkers/LFC.png'), (65, 65))
CFC = pygame.transform.scale(pygame.image.load('checkers/CFC.png'), (65, 65))