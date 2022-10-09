
from gameSetting import *


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
