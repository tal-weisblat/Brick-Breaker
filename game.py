


import pygame 
import os
pygame.init()


from classes import Ball
from classes import Paddle
from classes import BrickList



# COLORS 
BLACK = (0,0,0)
RED   = (255,0,0) 


# SOUNDS 
#COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'click_sound.mp3'))


# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 700                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()


# BALL
BALL_RADIUS   = 10 
BALL_X_VEL    = 0
BALL_Y_VEL    = 10
BALL_COLOR  = BLACK 
BALL_POSITION = (WIN_WIDTH/2 - BALL_RADIUS, WIN_HEIGHT/2)
ball = Ball(BALL_POSITION, BALL_RADIUS, BALL_X_VEL, BALL_Y_VEL, BALL_COLOR)


# PADDLE 
PAD_WIDTH  = 200
PAD_HEIGHT = 12
PAD_VEL    = 7
PAD_COLOR  = RED 
PAD_POSITION = (WIN_WIDTH/2, WIN_HEIGHT - PAD_HEIGHT- 2)
paddle = Paddle(PAD_POSITION, PAD_WIDTH, PAD_HEIGHT, PAD_VEL, RED)



# BRICKS 
ROW_NUM = 1 
COL_NUM = 3
BRICK_WIDTH  =  50
BRICK_HEIGHT =  30 
BRICK_COLOR  = BLACK
GAP = 30
brick_list = BrickList(ROW_NUM, COL_NUM, BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR, GAP) 






def game():
    
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
            
            
        # collisions 
        ball.collide_walls()  
        ball.collide_paddle(paddle)      
        brick_list.collide_ball(ball)
        

        # move 
        ball.move()
        paddle.move()
        
        # draw     
        WIN.fill('white')
        ball.draw()
        paddle.draw()
        brick_list.draw()
        pygame.display.update()

    pygame.quit()


game()





