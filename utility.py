

import pygame 
import os 

# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 1066                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()


# COLORS 
BLUE  = (0,0,102)


# EVENTS 
NEWGAME_EVENT    = pygame.USEREVENT + 3  




def gameStatus_draw(block_hit_num):
    x = 10
    y = WIN_HEIGHT/2
    color = BLUE 
    phont_size = 20
    BLOCKS_FONT = pygame.font.SysFont('comicsans', phont_size)
    blocks_text = BLOCKS_FONT.render('Blocks: ' + str(block_hit_num),1, color)
    WIN.blit(blocks_text, (x,y))




# GAME-OVER 
SCALE = 0.6
BACKGROUNG_IMG = pygame.image.load(os.path.join('files/images', 'background_5.jpg'))
BACKGROUNG_IMG = pygame.transform.scale(BACKGROUNG_IMG, (BACKGROUNG_IMG.get_width()*SCALE,(BACKGROUNG_IMG.get_height()*SCALE)) ) 
BACKGROUNG_IMG.get_rect().topleft = (0,0)

def gameOver_draw(gameOver):
    if gameOver: 
        
        # game-over
        phont_size = 50 
        color = BLUE
        GAMEOVER_FONT = pygame.font.SysFont('comicsans', phont_size)
        gameOver_text = GAMEOVER_FONT.render('Game Over',1, color)
        gameOver_width  = gameOver_text.get_width()
        gameOver_heigth = gameOver_text.get_height() 
        gameOver_x = WIN_WIDTH/2 - gameOver_width/2
        gameOver_y = WIN_HEIGHT/2 - gameOver_heigth/2
        
        # New game ?  
        newGame_text = GAMEOVER_FONT.render('New game ?',1, color)
        newGame_width  = gameOver_text.get_width()
        newgame_height = gameOver_text.get_height()
        newGame_x = WIN_WIDTH/2 - newGame_width/2
        newGame_y = WIN_HEIGHT/2 + gameOver_heigth/2 + 10

        # Yes 
        yes_text = GAMEOVER_FONT.render('yes',1, color)
        yes_x = WIN_WIDTH/2 - yes_text.get_width()/2
        yes_y = WIN_HEIGHT/2 + gameOver_heigth/2 + newgame_height + 20
        
        yes_rect = yes_text.get_rect()
        yes_rect.topleft = (yes_x,yes_y)


        pos = pygame.mouse.get_pos()
        if yes_rect.collidepoint(pos) and (pygame.mouse.get_pressed()[0] == 1):
            pygame.event.post(pygame.event.Event(NEWGAME_EVENT))


        # draw 
        WIN.blit(BACKGROUNG_IMG, BACKGROUNG_IMG.get_rect())
        WIN.blit(newGame_text, (newGame_x,newGame_y))
        WIN.blit(gameOver_text, (gameOver_x,gameOver_y))
        WIN.blit(yes_text,(yes_x,yes_y))
        pygame.display.update()
