import pygame
import math
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, LOGO, BACKGROUND, PLAY, BLUE, RED, IA
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax_red, minimax_blue

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
play_button_rect = PLAY.get_rect()
play_button_rect.x = math.ceil(WIDTH/2.6)
play_button_rect.y = math.ceil(HEIGHT/2)
ia_button_rect = IA.get_rect()
ia_button_rect.x = math.ceil(WIDTH/2.6)
ia_button_rect.y = math.ceil(HEIGHT/1.6)
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col

# Fonction main qui gère l'exécution du jeu
# Boucle principale qui contient le menu d'accueil
# selon le clique de l'utilisateur on lance les différents jeux (humain,ia) (ia,ia)
# 
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    home_screen = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (ia_button_rect.collidepoint(event.pos)) and home_screen:
                    game.ia_ia = True
                elif (play_button_rect.collidepoint(event.pos)) and home_screen:
                    game.human_ia = True
                home_screen = False 
                if game.human_ia:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.choisir_piece(row, col)
                
            
        WIN.blit(BACKGROUND, (0, 0))
        
        #ia vs ia
        if game.ia_ia and game.winner() == None:   
            if game.turn == RED:
                value, new_board = minimax_red(game.get_board(), 2,float('-inf'), float('+inf'), RED, game)
                game.ai_move(new_board)
                    
            elif game.turn == BLUE:
                value, new_board = minimax_blue(game.get_board(), 2,float('-inf'), float('+inf'), BLUE, game)
                game.ai_move(new_board)
        
        #humain vs ia
        elif game.human_ia and game.winner() == None:
             if game.turn == RED:
                value, new_board = minimax_red(game.get_board(), 2,float('-inf'), float('+inf'), RED, game)
                game.ai_move(new_board)
                    
        if game.winner() != None:
            run = False
         
        if game.ia_ia or game.human_ia:
            game.update() 

        else:
            WIN.blit(LOGO, (225, 100))
            WIN.blit(PLAY, play_button_rect)
            WIN.blit(IA, ia_button_rect)
        pygame.display.flip()

    pygame.quit()


main()
