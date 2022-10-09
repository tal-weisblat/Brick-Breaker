
from gameSetting import *

from gameObjects.ball   import Ball
from gameObjects.paddle import Paddle
from gameObjects.brickList import BrickList
from gameObjects.bulletList import BulletList
from gameDraw.drawGame import drawGame, drawGameStatus
from gameDraw.drawGameOver import drawGameOver



def game():
    
    paddle  = Paddle(PAD_POSITION, PAD_WIDTH, PAD_HEIGHT, PAD_VEL, PAD_COLOR)
    ball    = Ball(BALL_POSITION, BALL_RADIUS, BALL_X_VEL, BALL_Y_VEL, BALL_COLOR, PAD_WIDTH)
    bricks  = BrickList(ROW_NUM, COL_NUM, BRICK_WIDTH, BRICK_HEIGHT, BRICK_COLOR, GAP) 
    bullets = BulletList(BULLET_VEL, BULLET_COLOR, BULLET_WIDTH, BULLET_HEIGHT)

    giftTime = 0
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
                
            if event.type == FIREBULLET_EVENT:
                giftTime = time.time()
                
    
        # game-over 
        if gameOver:
            drawGameOver(gameOver) 
            continue 
            
        # collisions 
        ball.collide_walls()  
        ball.collide_paddle(paddle)      
        bricks.collide_ball(ball)
        bricks.collide_bullet(bullets)
        paddle.collide_gift(bricks.fallingGift)

        # bullet-fired 
        keys = pygame.key.get_pressed()
        spaceBar_pressed = bullets.bulletFired(keys, paddle, spaceBar_pressed, giftTime) 
        if not keys[pygame.K_SPACE]: spaceBar_pressed = False 
    
        # move 
        ball.move()
        paddle.move()
        bricks.fallingGiftMove()
        
        # draw     
        drawGame(bricks,bullets,ball,paddle,block_hit_num)

    pygame.quit()


game()





