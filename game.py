


import pygame 
import os
pygame.init()


from classes import Ball
from classes import Paddle
from classes import BrickList
from classes import BulletList

from utility import gameStatus_draw
from utility import gameOver_draw

# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 1066                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()



# EVENT 
BLOCKS_HIT_EVENT = pygame.USEREVENT + 1
GAMEOVER_EVENT   = pygame.USEREVENT + 2
NEWGAME_EVENT    = pygame.USEREVENT + 3  


# COLORS 
BLACK = (0,0,0)
RED   = (255,0,0) 
BLUE  = (0,0,102)
     

# SOUNDS 
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))
GAMEOVER_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'game_over.wav'))
BULLETFIRED_SOUND = pygame.mixer.Sound(os.path.join('files/sounds','laser_shot.wav'))

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
PAD_POSITION = (WIN_WIDTH/2 - PAD_WIDTH/2, WIN_HEIGHT - PAD_HEIGHT- 2)

# BALL
BALL_RADIUS   = 10 
BALL_X_VEL    = 0
BALL_Y_VEL    = 10
BALL_COLOR  = BLACK 
BALL_POSITION = (WIN_WIDTH/2 - BALL_RADIUS, WIN_HEIGHT/2)

# BRICKS 
ROW_NUM = 4
COL_NUM = 14
BRICK_WIDTH  =  70
BRICK_HEIGHT =  30 
BRICK_COLOR  = BLACK
GAP = 10



# BULLETS 
bullet_list = [] 
BULLET_VEL = 19
BULLET_COLOR = BLACK
BULLET_WIDTH  = 5
BULLET_HEIGHT = 5





# DRAW 
# def bullets_draw():
#     for bullet in bullet_list:
#         bullet.y -= BULLET_VEL
#         pygame.draw.rect(WIN, BULLET_COLOR, bullet)

# # FIRE 
# def fireBullet(bullet_list, x,y):
#     BULLETFIRED_SOUND.play()
#     bullet = pygame.Rect(x,y, BULLET_WIDTH, BULLET_HEIGHT)
#     bullet_list.append(bullet)

# # COLLISON 
# def bulletCollideBrick(brick_list):
    
#     for bullet in bullet_list:
#         for brick in brick_list:
#             if bullet.colliderect(brick):
#                 # add sound ...
#                 brick_list.remove(brick)
#                 bullet_list.remove(bullet)





def game():
    
    paddle      = Paddle(PAD_POSITION, PAD_WIDTH, PAD_HEIGHT, PAD_VEL, PAD_COLOR)
    ball        = Ball(BALL_POSITION, BALL_RADIUS, BALL_X_VEL, BALL_Y_VEL, BALL_COLOR, PAD_WIDTH)
    brick_list  = BrickList(ROW_NUM, COL_NUM, BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR, GAP) 
    bullet_list = BulletList(BULLET_VEL, BULLET_COLOR, BULLET_WIDTH, BULLET_HEIGHT)


    spaceBar_pressed = False 

    gameOver = False 
    block_hit_num = 0
    run = True                     
    clock = pygame.time.Clock()    
    fps = 60                                          
    

    while run:

        clock.tick(fps)   
        for event in pygame.event.get():
             
            if event.type == pygame.QUIT:
                run = False 
                break 
            
            if event.type == BLOCKS_HIT_EVENT:  
                block_hit_num += 1

            if event.type == GAMEOVER_EVENT: 
                gameOver = True
                GAMEOVER_SOUND.play()
                break

            if event.type == NEWGAME_EVENT:
                game()
                break
                
                
        # game-over 
        if gameOver:
            gameOver_draw(gameOver) 
            continue 
            
            
        # bullet-fired 
        keys = pygame.key.get_pressed()
        spaceBar_pressed = bullet_list.bulletFired(keys, paddle, spaceBar_pressed) 
        if not keys[pygame.K_SPACE]: spaceBar_pressed = False 
    

        # collisions 
        ball.collide_walls()  
        ball.collide_paddle(paddle)      
        brick_list.collide_ball(ball)
        bullet_list.bulletCollideBrick(brick_list.list)
        
        # move 
        ball.move()
        paddle.move()
        
        # draw     
        WIN.blit(BACKGROUNG_IMG, BACKGROUNG_IMG.get_rect()) 
        bullet_list.draw()
        ball.draw()
        paddle.draw()
        brick_list.draw()
        gameStatus_draw(block_hit_num)
        pygame.display.update()

    pygame.quit()


game()





