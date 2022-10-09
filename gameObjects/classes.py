

from gameSetting import *


                
# ----------------------------------------  BrickList -------------------------------------------------
class BrickList():
    def __init__(self, row_number, col_number, brick_width, brick_height, colors, lines_gap):

        self.list = [] 
        self.row_number = row_number
        self.col_number = col_number 
        self.size = self.row_number * self.col_number
        self.brick_width = brick_width 
        self.brick_height = brick_height
        self.colors = colors 
        self.lines_gap = lines_gap 

        #self.giftList = []       # to enable paddle shooting 
        self.fallingGift = None 
        
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

                # FALLING GIFT (for shooting)
                if self.size - len(self.list) == 3:
                    x =  brick.x + brick.width/2
                    y =  brick.y 
                    self.fallingGift = pygame.Rect(x ,y , 8, 8)                

                self.list.remove(brick)
                ball.y_vel = -ball.y_vel


    def collide_bullet(self, bullets):
        
        for brick in self.list: 
            for bullet in bullets.list:
                if brick.colliderect(bullet):
                    # add sound ...                    
                    pygame.event.post(pygame.event.Event(BLOCKS_HIT_EVENT))
                    self.list.remove(brick)
                    bullets.list.remove(bullet)
    

    # VEL = 4    
    def fallingGiftMove(self):
        if self.fallingGift != None: 
            self.fallingGift.y += 4

    def fallingGiftDraw(self):
        if self.fallingGift != None:
            pygame.draw.rect(WIN, self.colors, self.fallingGift)
                


            
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

    # bullet fired  - limited time version (according to gift)
    def bulletFired(self, keys, paddle, spaceBar_pressed, giftTime):
        if keys[pygame.K_SPACE] and (spaceBar_pressed == False) and (time.time() - giftTime < 3):
            BULLETFIRED_SOUND.play()
            spaceBar_pressed = True 
            x = paddle.rect.x + paddle.width/2
            y = paddle.rect.y 
            bullet = pygame.Rect(x,y, self.width, self.height)
            self.list.append(bullet)
            return spaceBar_pressed


    # bullet-brick collision 
    def collideBrick(self, brick_list):
        for bullet in self.list:
            for brick in brick_list:
                if bullet.colliderect(brick):
                    # add sound ...                    
                    pygame.event.post(pygame.event.Event(BLOCKS_HIT_EVENT))
                    brick_list.remove(brick)
                    self.list.remove(bullet)





# # WINDOW 
# WIN_HEIGHT = 600  
# WIN_WIDTH  = 1066                                                
# WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
# pygame.display.set_caption('Bricks Breaker')                    
# pygame.init()

# # SOUNDS
# COLLISION_SOUND = pygame.mixer.Sound(os.path.join('files/sounds', 'tick.mp3'))
# BULLETFIRED_SOUND = pygame.mixer.Sound(os.path.join('files/sounds','laser_shot.wav'))
# PUDDLEGIFT_SOUND  = pygame.mixer.Sound(os.path.join('files/sounds', 'puddle_gift_collision.wav') )

# # EVENTS 
# BLOCKS_HIT_EVENT = pygame.USEREVENT + 1
# GAMEOVER_EVENT   = pygame.USEREVENT + 2
# FIREBULLET_EVENT = pygame.USEREVENT + 4 
