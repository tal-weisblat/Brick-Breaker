

# packages 
import pygame 
import pymunk                   # physics 
import pymunk.pygame_util
import math 


# COLORS 
BLACK = (0,0,0)


# WINDOW 
WIN_WIDTH  = 500                                                
WIN_HEIGHT = 650  
WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))     
pygame.display.set_caption('Gravity')                    
pygame.init()

# SPACE 
space = pymunk.Space()       
space.gravity = (0,900)      
draw_options = pymunk.pygame_util.DrawOptions(WIN)



# PAD 
GAP = 2 
PAD_VEL = 5
PAD_WIDTH   = 60
PAD_HEIGHT  = 20 
size = (PAD_WIDTH, PAD_HEIGHT)

# PAD-BODY
pad_body = pymunk.Body(body_type = pymunk.Body.STATIC)   
pad_body.position = (WIN_WIDTH/2, WIN_HEIGHT - PAD_HEIGHT - GAP)     # POSITON ....... 

# PAD-SHAPE 
pad_shape = pymunk.Poly.create_box(pad_body, size)        
pad_shape.color = BLACK
pad_shape.elasticity = 0.4                               
pad_shape.friction = 0.5

# ADD-TO-SPACE
space.add(pad_body,pad_shape)                        



# MOVEMENT  
# def pad_movement():
#     keys = pygame.key.get_pressed()         
#     if keys[pygame.K_RIGHT]: 
#         x = WIN_WIDTH/2 + PAD_VEL
#         y = WIN_HEIGHT - PAD_HEIGHT - GAP
#         pad_body.position = (x,y)

#     if keys[pygame.K_LEFT]:  
#         x = WIN_WIDTH/2 - PAD_VEL
#         y = WIN_HEIGHT - PAD_HEIGHT - GAP
#         pad_body.position = (x,y)

        



# STATIC-BODY 
def create_boundaries(space, size):

    # BODY 
    body = pymunk.Body(body_type = pymunk.Body.STATIC)    # first definition of a body (of static type)
    body.position = (50,400)                              # body's initial position 
    
    # SHAPE 
    shape = pymunk.Poly.create_box(body, size)            # shape is a box the wrap the body 
    shape.color = (255,0,0,100)                           # color 
    shape.elasticity = 0.4                                # elasticity & friction  
    shape.friction = 0.5
    

    # ADD TO SPACE 
    space.add(body,shape)                                 # add both body & shape to SPACE 

# DYNAMIC
def create_ball(space, radius, mass, position):

    # BODY 
    body = pymunk.Body(body_type = pymunk.Body.DYNAMIC)
    body.position = position     

    # SHAPE 
    shape = pymunk.Circle(body, radius) 
    shape.color = (255,0,0, 50) 
    shape.elasticity = 0.9
    shape.friction = 0.5
    shape.mass = mass

    # ADD TO SPACE 
    space.add(body,shape)
    return shape               # enable us to interfere while dynamic-body on screen 

    




def game(WIN):
    
    
    
    
    #create_boundaries(space, (30,40))                         # boundaries 
    ball = create_ball(space, 25, 10, (WIN_WIDTH/2, 30))       # ball 
    

    # settings 
    run = True                     
    clock = pygame.time.Clock()    
    fps = 60                       
    dt = 1/fps                      




    while run:

        space.step(dt)    
        clock.tick(fps)   




        # EVENTs
        for event in pygame.event.get():
            
            # QUIT 
            if event.type == pygame.QUIT:
                run = False 
                break 

            

        #pad_movement()    


        # DRAW 
        WIN.fill('white')
        #pygame.draw.rect(WIN, BLACK, pad)
        space.debug_draw(draw_options)
        pygame.display.update()


    pygame.quit()





game(WIN)