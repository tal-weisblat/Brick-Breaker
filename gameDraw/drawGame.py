

from gameSetting import *


def drawGameStatus(block_hit_num):
    x = 10
    y = WIN_HEIGHT/2
    color = BLUE 
    phont_size = 20
    BLOCKS_FONT = pygame.font.SysFont('comicsans', phont_size)
    blocks_text = BLOCKS_FONT.render('Blocks: ' + str(block_hit_num),1, color)
    WIN.blit(blocks_text, (x,y))

def drawGame(bricks,bullets,ball,paddle,block_hit_num):
    WIN.blit(BACKGROUNG_IMG, BACKGROUNG_IMG.get_rect()) 
    bricks.fallingGiftDraw()
    bullets.draw()
    ball.draw()
    paddle.draw()
    bricks.draw()
    drawGameStatus(block_hit_num)
    pygame.display.update()


