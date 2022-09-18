


import pygame 
import os


pygame.init()



# COLORS 
BLACK = (0,0,0)
RED   = (255,0,0) 


# SOUNDS 
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'click_sound.mp3'))


# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 700                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()








class Ball():

    def __init__(self, position, radius, x_vel, y_vel, color ):
        
        self.x = position[0]
        self.y = position[1]
        self.radius   = radius 
        self.color    = color 
        self.x_vel = x_vel           
        self.y_vel = y_vel 

    def draw(self): 
        pygame.draw.circle(WIN, self.color, [self.x,self.y], self.radius)
        
    def move(self):
        self.x += self.x_vel  
        self.y += self.y_vel 


    def collision_walls(self): 
        if ball.y + ball.radius >= WIN_HEIGHT: # button 
            self.y_vel = -self.y_vel 
            #COLLISION_SOUND.play()
        if self.x + self.radius >= WIN_WIDTH:  # right-wall 
            self.x_vel = -self.x_vel
            #COLLISION_SOUND.play()
        if self.y - self.radius  <= 0:         # top 
            self.y_vel = -self.y_vel
            #COLLISION_SOUND.play()
        if self.x - self.radius <= 0 :         # left-wall 
            self.x_vel = -self.x_vel  
            #COLLISION_SOUND.play()


# BALL
BALL_RADIUS   = 10 
BALL_X_VEL    = 5
BALL_Y_VEL    = 6
BALL_COLOR  = BLACK 
BALL_POSITION = (WIN_WIDTH/2 - BALL_RADIUS, WIN_HEIGHT/2)
ball = Ball(BALL_POSITION, BALL_RADIUS, BALL_X_VEL, BALL_Y_VEL, BALL_COLOR)




class Puddle():

    def __init__ (self, position, width, height, velocity, color ):

        self.x = position[0]
        self.y = position[1]
        self.color = color 
        self.width = width 
        self.height = height 
        self.velocity = velocity 

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity


# PADDLE 
PAD_WIDTH  = 50
PAD_HEIGHT = 10
PAD_VEL    = 6
PAD_COLOR  = RED 
PAD_POSITION = (WIN_WIDTH/2 - PAD_WIDTH/2, WIN_HEIGHT - PAD_HEIGHT- 2)
paddle = Puddle(PAD_POSITION, PAD_WIDTH, PAD_HEIGHT, PAD_VEL, PAD_COLOR)




def game():
    
    # settings
    run = True                     
    clock = pygame.time.Clock()    
    fps = 60                                          
    
    while run:

        clock.tick(fps)   

        # EVENTs
        for event in pygame.event.get():
            
            # QUIT 
            if event.type == pygame.QUIT:
                run = False 
                break 
            
            
        # physics 
        ball.collision_walls() 
        ball.move()
        paddle.move()
        
        
        # draw     
        WIN.fill('white')
        ball.draw()
        paddle.draw()
        pygame.display.update()

    pygame.quit()



game()





