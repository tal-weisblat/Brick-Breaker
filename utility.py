

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
        
        # settings
        phont_size = 50 
        color = BLUE
        GAMEOVER_FONT = pygame.font.SysFont('comicsans', phont_size)
        gameOver_text = GAMEOVER_FONT.render('Game Over',1, color)
        width  = gameOver_text.get_width()
        heigth = gameOver_text.get_height() 
        x = WIN_WIDTH/2 - width/2
        y = WIN_HEIGHT/2 - heigth/2
        
        # draw 
        WIN.blit(BACKGROUNG_IMG, BACKGROUNG_IMG.get_rect())
        WIN.blit(gameOver_text, (x,y))
        pygame.display.update()
