import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, BLACK, WHITE, GREEN

class Board:
    def __init__(self):
        self.board = []
        
    def start_game_board(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(window, GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                
    