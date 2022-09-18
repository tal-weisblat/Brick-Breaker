


import pygame 
import os
pygame.init()


# CLASSES 
from classes import Ball
from classes import Paddle



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
BALL_Y_VEL    = 6
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
            
            
        # collision 
        ball.collide_walls()  
        ball.collide_paddle(paddle)      # improve ...     

        # move 
        ball.move()
        paddle.move()
        
        # draw     
        WIN.fill('white')
        ball.draw()
        paddle.draw()
        pygame.display.update()

    pygame.quit()


game()





