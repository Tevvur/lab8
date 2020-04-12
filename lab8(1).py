import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ballsurface = pygame.Surface((50,50))     
ballsurface.set_colorkey((0,0,0))         
pygame.draw.circle(ballsurface, (255,0,0), (25,25),25) 
ballsurface = ballsurface.convert_alpha()      
ballrect = ballsurface.get_rect()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ballrect.y >= 20:
                    ballrect.move_ip(0, -20)
            elif event.key == pygame.K_DOWN:
                if ballrect.y <= screen.get_size()[1] - 80:
                    ballrect.move_ip(0, 20)
            elif event.key == pygame.K_LEFT:
                if ballrect.x >= 20 :
                    ballrect.move_ip(-20, 0)
            elif event.key == pygame.K_RIGHT:
                if ballrect.x <= screen.get_size()[0] -80:
                    ballrect.move_ip(20, 0)
    screen.fill((255,255,255))
    screen.blit(ballsurface,ballrect)
    pygame.display.update()  # Or pygame.display.flip()