import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, BLUE, RED
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.start_game_board()
        
    def squares(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(window, BLUE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
                
    
    def start_game_board(self):
        for row in range (ROWS):
            self.board.append([])
            for col in range (COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
                    
    def draw(self,win):
        self.squares(win)
        for row in range (ROWS):
            for col in range (COLS):
                piece = self.board[row][col]
                if piece != 0:
                   piece.create_piece(win)
                    
        
  
                
                
    