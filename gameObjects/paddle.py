
from gameSetting import *


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

    def collide_gift(self, gift):
        if gift != None: 
            if self.rect.colliderect(gift):                
                pygame.event.post(pygame.event.Event(FIREBULLET_EVENT))
                PUDDLEGIFT_SOUND.play()
                
