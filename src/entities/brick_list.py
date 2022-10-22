
from game_setting import *

                

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

                # falling gift (for shooting)
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
                    pygame.event.post(pygame.event.Event(BLOCKS_HIT_EVENT))
                    self.list.remove(brick)
                    bullets.list.remove(bullet)
    
    def falling_gift_move(self):
        if self.fallingGift != None: 
            self.fallingGift.y += 4      # VEL = 4    

    def falling_gift_draw(self):
        if self.fallingGift != None:
            pygame.draw.rect(WIN, self.colors, self.fallingGift)
                


