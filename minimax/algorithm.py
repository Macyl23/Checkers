from copy import deepcopy
from checkers import board
import pygame


RED = (255,0,0)
BLUE = (46,115,154)


# Algorithme minimax sans alpha beta 
def minimax(position, profondeur, max_player, game):
    if profondeur == 0 or position.winner() != None:
        return position.evaluate_level_one(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, profondeur-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimax(move, profondeur-1,True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
    
# algorithme avec élegage alpha beta pour réduire le l'arbre de recherche
def alpha_beta(position, profondeur,alpha, beta, max_player, game):
    if profondeur == 0 or position.winner() != None:
        return position.evaluate_level_three(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = alpha_beta(move, profondeur-1,alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, maxEval)
            if alpha >= beta:
                best_move = move
                return maxEval, best_move
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = alpha_beta(move, profondeur-1,alpha,beta, True, game)[0]
            minEval = min(minEval, evaluation)
            beta = min(minEval,beta)
            if alpha >= beta:
                best_move = move
                return minEval, best_move
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
        

# Fonction qui change l'état du BOARD pour calculer evaluer le cout d'un coup       
def simulate_move(piece, move, board, game, skip):
    board.change_position_sur_grille(piece, move[0], move[1])
    if skip:
        board.remove(skip)
        
    return board
        
# Fonction qui recupere les coups valides pour une pièce pour ensuite estimer le meilleur coup 
# dans l'algorithme minimax 
def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.valid_moves(piece)
        for move, skip in valid_moves.items():
            
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


