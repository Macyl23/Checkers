import pygame
from .constants import ROWS, COLS, SQUARE_SIZE, WHITE, BLUE, RED
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.creer_grille()
        self.red_kings = 0
        self.blue_kings = 0

    def creer_cases(self, window):
        window.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(window, BLUE, (row*SQUARE_SIZE,
                                 col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def creer_grille(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def ajouter_pieces_sur_grille(self, win):
        self.creer_cases(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.create_piece(win)

    def change_position_sur_grille(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move_piece(row, col)
        
        
    def get_piece(self, row, col):
        return self.board[row][col]

    def eliminer_pieces(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    def valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLUE:
            moves.update(self._valid_moves_left(row-1, 0, -1, piece.color, left))
            moves.update(self._valid_moves_right(row-1, 0, -1, piece.color, right))

        if piece.color == RED:
            moves.update(self._valid_moves_left(row+1, ROWS, 1, piece.color, left))
            moves.update(self._valid_moves_right(row+1, ROWS, 1, piece.color, right))

        return moves

    def _valid_moves_left(self, start, stop, step, color, left, pions_manges=[]):
        derniere_piece_tuee = []
        moves = {}
        for r in range(start,stop,step):
            
            if left < 0:
                break
            
            case_adjacente = self.board[r][left]
            if self._est_vide(case_adjacente):
                
                if pions_manges and not derniere_piece_tuee:
                    return moves
                 
                elif pions_manges:
                    moves[(r, left)] = derniere_piece_tuee + pions_manges
                else:
                    moves[(r, left)] = derniere_piece_tuee 
                    if derniere_piece_tuee:
                           
                        moves.update(self._valid_moves_left(r+step, self._direction(step), step, color, left-1,pions_manges=derniere_piece_tuee))
                        moves.update(self._valid_moves_right(r+step, self._direction(step), step, color, left+1,pions_manges=derniere_piece_tuee))

                return moves
            else:
                if case_adjacente.color == color or derniere_piece_tuee:
                    return moves
                else:
                    derniere_piece_tuee = [case_adjacente]
                      
            
            left -= 1
        return moves
              
    
    def _valid_moves_right(self, start, stop, step, color, right, pions_manges=[]):
        derniere_piece_tuee = []
        moves = {}
        for r in range(start,stop,step):
            
            if right >= COLS:
                break
            
            
            case_adjacente = self.board[r][right]
            if self._est_vide(case_adjacente):
                if pions_manges and not derniere_piece_tuee:
                    
                    return moves
                
                elif pions_manges:
                    return moves     
                else:
                    moves[(r, right)] = derniere_piece_tuee +pions_manges
                                        
                    if derniere_piece_tuee:      
                        moves.update(self._valid_moves_left(r+step, self._direction(step), step, color, right-1,pions_manges=derniere_piece_tuee))
                        moves.update(self._valid_moves_right(r+step, self._direction(step), step, color, right+1,pions_manges=derniere_piece_tuee))
                        print(pions_manges)

                return moves
            else:
                if case_adjacente.color == color or derniere_piece_tuee:
                    return moves
                else:
                    derniere_piece_tuee = [case_adjacente]
                    
        
            right += 1
        return moves


    def _next_case_selon_direction(self, step, diagonal,row ):
        if step == -1:
            return self.board[row-1][diagonal-1]
        else:
            return self.board[row+1][diagonal+1]
        
    def _direction(self, step):
        if step == -1:
            return -1
        else:
            return ROWS 
    def _piece_couleur_differente(self, piece, color):
        return piece.color != color
    
    def _est_vide(self, current):
        return current == 0

    # def _valid_moves_right(self, start, stop, step, color, right, skipped=[]):
    #     moves = {}
    #     last = []

    #     for r in range(start, stop,step):
    #         if right >= COLS:
    #             break
    #         current = self.board[r][right]
    #         if current == 0:
    #             if skipped and not last:
    #                 break
    #             elif skipped:
    #                 moves[(r, right)] = last + skipped
    #             else:
    #                 moves[(r, right)] = last

    #                 if last:
    #                     if step == -1:
    #                         row = max(r - 3, 0)
    #                     else:
    #                         row = min(r+3, ROWS)
    #                     moves.update(self._valid_moves_left(
    #                         r+step, row, step, color, right-1, skipped=last))
    #                     moves.update(self._valid_moves_right(
    #                         r+step, row, step, color, right+1, skipped=last))
    #                 break
    #         elif current.color == color:
    #             break
    #         else:
    #             last = [current]

    #         right += 1

    #     return moves
