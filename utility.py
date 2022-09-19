

import pygame 


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
