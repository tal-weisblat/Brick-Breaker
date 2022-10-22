from game_setting import *

                
            
# ----------------------------------------  Bullets -------------------------------------------------
class BulletList():

    def __init__(self, velocity, color, bul_width, bul_height): 

        self.list = []
        self.velocity = velocity 
        self.color = color 
        self.width  = bul_width 
        self.height = bul_height

    def draw(self):
        for bullet in self.list:
            bullet.y -= self.velocity
            pygame.draw.rect(WIN, self.color, bullet)

    # bullet fired - limited time version (according to gift)
    def bullet_fired(self, keys, paddle, spaceBar_pressed, giftTime):
        if keys[pygame.K_SPACE] and (spaceBar_pressed == False) and (time.time() - giftTime < 3):
            BULLETFIRED_SOUND.play()
            spaceBar_pressed = True 
            x = paddle.rect.x + paddle.width/2
            y = paddle.rect.y 
            bullet = pygame.Rect(x,y, self.width, self.height)
            self.list.append(bullet)
            return spaceBar_pressed

    # bullet-brick collision 
    def collide_brick(self, brick_list):
        for bullet in self.list:
            for brick in brick_list:
                if bullet.colliderect(brick):                
                    pygame.event.post(pygame.event.Event(BLOCKS_HIT_EVENT))
                    brick_list.remove(brick)
                    self.list.remove(bullet)
