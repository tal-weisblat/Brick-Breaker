
import pygame 
import os



# WINDOW 
WIN_HEIGHT = 600  
WIN_WIDTH  = 1066                                                
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Bricks Breaker')                    
pygame.init()


# SOUNDS
COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))


# EVENTS 
BLOCKS_HIT_EVENT = pygame.USEREVENT + 1
GAMEOVER_EVENT   = pygame.USEREVENT + 2






# ----------------------------------------  BALL  -------------------------------------------------
class Ball():

    def __init__(self, position, radius, x_vel, y_vel, color, pad_width):
        
        self.x = position[0]
        self.y = position[1]
        self.radius   = radius 
        self.color    = color 
        self.x_vel = x_vel           
        self.y_vel = y_vel 
        self.pad_width = pad_width
        
        # for collision with paddle 
        self.circ_rect = pygame.Rect(self.x, self.y, 2*self.radius, 2*self.radius) 
        self.circ_rect.center = (self.x, self.y)
            


    def collide_paddle(self, paddle):
        
        if paddle.rect.colliderect(self.circ_rect):
            COLLISION_SOUND.play()
            self.y_vel = - self.y_vel
            diff = (self.circ_rect.x - paddle.rect.x)/self.pad_width
            
            # BUG: not good enough ...  
            if diff >= 0.5:
                self.x_vel += 4*(diff - 0.5)
            if diff < 0.5:
                self.x_vel -= 4*(0.5 - diff)
            
    def draw(self): 
        pygame.draw.circle(WIN, self.color, [self.x,self.y], self.radius)   # draw circle (NOT rect) 
        
    def move(self):
        self.x += self.x_vel  
        self.y += self.y_vel 
        self.circ_rect.x, self.circ_rect.y = self.x, self.y 
        
    def collide_walls(self): 
        if self.y + self.radius >= WIN_HEIGHT: # hit buttom (game-over)
            self.y_vel = -self.y_vel 
            pygame.event.post(pygame.event.Event(GAMEOVER_EVENT))
            COLLISION_SOUND.play()

        if self.x + self.radius >= WIN_WIDTH:  # right-wall 
            self.x_vel = -self.x_vel
            COLLISION_SOUND.play()

        if self.y - self.radius  <= 0:         # top 
            self.y_vel = -self.y_vel
            COLLISION_SOUND.play()
            
        if self.x - self.radius <= 0 :         # left-wall 
            self.x_vel = -self.x_vel  
            COLLISION_SOUND.play()
        
        self.circ_rect.x, self.circ_rect.y = self.x, self.y 



# ----------------------------------------  PADDLE  -------------------------------------------------
class Paddle():

    def __init__ (self, position, width, height, velocity, color):

        self.width = width 
        self.height = height 
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self.color = color 
        self.velocity = velocity 
        self.rect.topleft = (position[0], position[1])
        
    def draw(self):
        pygame.draw.rect(WIN, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and (self.rect.x + self.width <= WIN_WIDTH):
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT] and (self.rect.x >= 0):
            self.rect.x -= self.velocity



# ----------------------------------------  BrickList -------------------------------------------------
class BrickList():
    def __init__(self, row_number, col_number, brick_width, brick_height, colors, lines_gap):

        self.list = [] 
        self.row_number = row_number
        self.col_number = col_number 
        self.brick_width = brick_width 
        self.brick_height = brick_height
        self.colors = colors 
        self.lines_gap = lines_gap 
        
        same_row_bricks_gap = (WIN_WIDTH - (self.col_number * self.brick_width))/(self.col_number + 1) 
        for row in range(self.row_number):
            for col in range(self.col_number):
                x =  (col+1)*same_row_bricks_gap +  col*self.brick_width + self.brick_width/2
                y =  (row+1)*self.lines_gap + row*self.brick_height + self.brick_height/2
                brick = pygame.Rect(x ,y , self.brick_width, self.brick_height)
                brick.center = (x,y)
                self.list.append(brick)
    

    def draw(self):
        for brick in self.list:
            pygame.draw.rect(WIN, self.colors, brick)

    def collide_ball(self,ball):
        for brick in self.list:
            if brick.colliderect(ball.circ_rect):
                pygame.event.post(pygame.event.Event(BLOCKS_HIT_EVENT))
                COLLISION_SOUND.play()
                self.list.remove(brick)
                ball.y_vel = -ball.y_vel

            
