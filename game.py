


import pygame 
import os
pygame.init()


from classes import Ball
from classes import Paddle
from classes import BrickList

from utility import gameStatus_draw

# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 1066                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()



# EVENT 
BLOCKS_HIT = pygame.USEREVENT + 1



# COLORS 
BLACK = (0,0,0)
RED   = (255,0,0) 
BLUE  = (0,0,102)
     


# SOUNDS 
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))

# IMAGES
SCALE = 0.6
BACKGROUNG_IMG = pygame.image.load(os.path.join('files/images', 'background_5.jpg'))
BACKGROUNG_IMG = pygame.transform.scale(BACKGROUNG_IMG, (BACKGROUNG_IMG.get_width()*SCALE,(BACKGROUNG_IMG.get_height()*SCALE)) ) 
BACKGROUNG_IMG.get_rect().topleft = (0,0)





# PADDLE 
PAD_WIDTH  = 135
PAD_HEIGHT = 14
PAD_VEL    = 7
PAD_COLOR  = BLUE  
PAD_POSITION = (WIN_WIDTH/2, WIN_HEIGHT - PAD_HEIGHT- 2)
paddle = Paddle(PAD_POSITION, PAD_WIDTH, PAD_HEIGHT, PAD_VEL, PAD_COLOR)


# BALL
BALL_RADIUS   = 10 
BALL_X_VEL    = 0
BALL_Y_VEL    = 10
BALL_COLOR  = BLACK 
BALL_POSITION = (WIN_WIDTH/2 - BALL_RADIUS, WIN_HEIGHT/2)
ball = Ball(BALL_POSITION, BALL_RADIUS, BALL_X_VEL, BALL_Y_VEL, BALL_COLOR, PAD_WIDTH)


# BRICKS 
ROW_NUM = 3
COL_NUM = 9
BRICK_WIDTH  =  70
BRICK_HEIGHT =  30 
BRICK_COLOR  = BLACK
GAP = 10
brick_list = BrickList(ROW_NUM, COL_NUM, BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR, GAP) 





def game():
    
    block_hit_num = 0
    run = True                     
    clock = pygame.time.Clock()    
    fps = 60                                          
    
    while run:

        clock.tick(fps)   

        # events 
        for event in pygame.event.get():
             
            if event.type == pygame.QUIT:
                run = False 
                break 
            
            if event.type == BLOCKS_HIT:  block_hit_num += 1
                
                

            
        # collisions 
        ball.collide_walls()  
        ball.collide_paddle(paddle)      
        brick_list.collide_ball(ball)
        

        # move 
        ball.move()
        paddle.move()
        
        # draw     
        WIN.fill('white')
        WIN.blit(BACKGROUNG_IMG, BACKGROUNG_IMG.get_rect())
        ball.draw()
        paddle.draw()
        brick_list.draw()
        gameStatus_draw(block_hit_num)
        pygame.display.update()

    pygame.quit()


game()





