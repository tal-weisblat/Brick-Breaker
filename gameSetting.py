


import pygame 
import time 
import os
pygame.init()


# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 1066                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()


# COLORS 
BLACK = (0,0,0)
RED   = (255,0,0) 
BLUE  = (0,0,102)


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
BULLET_VEL = 19
BULLET_COLOR = BLACK
BULLET_WIDTH  = 5
BULLET_HEIGHT = 5


# SOUNDS
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('soundFiles', 'tick.mp3'))
BULLETFIRED_SOUND = pygame.mixer.Sound(os.path.join('soundFiles','laser_shot.wav'))
GAMEOVER_SOUND = pygame.mixer.Sound(os.path.join('soundFiles', 'game_over.wav'))
PUDDLEGIFT_SOUND  = pygame.mixer.Sound(os.path.join('soundFiles', 'puddle_gift_collision.wav') )


# EVENTS 
BLOCKS_HIT_EVENT = pygame.USEREVENT + 1
GAMEOVER_EVENT   = pygame.USEREVENT + 2
NEWGAME_EVENT    = pygame.USEREVENT + 3 
FIREBULLET_EVENT = pygame.USEREVENT + 4 


# IMAGES
SCALE = 0.6
BACKGROUNG_IMG = pygame.image.load(os.path.join('imageFiles', 'background.jpg'))
BACKGROUNG_IMG = pygame.transform.scale(BACKGROUNG_IMG, (BACKGROUNG_IMG.get_width()*SCALE,(BACKGROUNG_IMG.get_height()*SCALE)) ) 
BACKGROUNG_IMG.get_rect().topleft = (0,0)


# GAME-OVER 
SCALE = 0.6
BACKGROUNG_IMG = pygame.image.load(os.path.join('imageFiles', 'background.jpg'))
BACKGROUNG_IMG = pygame.transform.scale(BACKGROUNG_IMG, (BACKGROUNG_IMG.get_width()*SCALE,(BACKGROUNG_IMG.get_height()*SCALE)) ) 
BACKGROUNG_IMG.get_rect().topleft = (0,0)
