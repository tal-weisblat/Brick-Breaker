


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
        
        # for collision with paddle 
        self.rect = pygame.Rect(self.x, self.y, 2*self.radius, 2*self.radius) 
        self.rect.center = (self.x, self.y)
            

    # BUG: not good enough ...  
    def collide_paddle(self, paddle):
        if paddle.rect.colliderect(self.rect):
            ball.y_vel = - ball.y_vel
        


    def draw(self): 
        pygame.draw.circle(WIN, self.color, [self.x,self.y], self.radius)   # draw circle (NOT rect) 
        
        
    def move(self):
        self.x += self.x_vel  
        self.y += self.y_vel 
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel


    def collide_walls(self): 
        if ball.y + ball.radius >= WIN_HEIGHT: # button 
            self.y_vel = -self.y_vel 
        if self.x + self.radius >= WIN_WIDTH:  # right-wall 
            self.x_vel = -self.x_vel
        if self.y - self.radius  <= 0:         # top 
            self.y_vel = -self.y_vel
        if self.x - self.radius <= 0 :         # left-wall 
            self.x_vel = -self.x_vel  
            


# BALL
BALL_RADIUS   = 10 
BALL_X_VEL    = 5
BALL_Y_VEL    = 6
BALL_COLOR  = BLACK 
BALL_POSITION = (WIN_WIDTH/2 - BALL_RADIUS, WIN_HEIGHT/2)
ball = Ball(BALL_POSITION, BALL_RADIUS, BALL_X_VEL, BALL_Y_VEL, BALL_COLOR)




class Paddle():

    def __init__ (self, position, width, height, velocity, color):

        self.x = position[0]
        self.y = position[1]
        self.color = color 
        self.width = width 
        self.height = height 
        self.velocity = velocity 
        
        # for collision with (the rect of) 'circle' 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.topleft = (self.x, self.y)


    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x += self.velocity
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.x -= self.velocity
            self.rect.x -= self.velocity


# PADDLE 
PAD_WIDTH  = 80
PAD_HEIGHT = 12
PAD_VEL    = 7
PAD_COLOR  = RED 
PAD_POSITION = (WIN_WIDTH/2 - PAD_WIDTH/2, WIN_HEIGHT - PAD_HEIGHT- 2)
paddle = Paddle(PAD_POSITION, PAD_WIDTH, PAD_HEIGHT, PAD_VEL, PAD_COLOR)




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





