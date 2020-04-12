from __future__ import print_function, division
import pygame
import random
class Ball:
    def __init__(self, x, y, width, height,dx,dy,radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.radius = radius
        self.ballsurface = pygame.Surface((width,height))
        self.ballsurface.set_colorkey((0,0,0))
def wildPainting(background,screenrect):
    pygame.draw.circle(background, (random.randint(0,255),
                       random.randint(0,255), random.randint(0,255)),
                       (random.randint(0,screenrect.width),
                       random.randint(0,screenrect.height)),
                       random.randint(50,500))
def move(ball,seconds,screenrect):
    ball.x += ball.dx * seconds
    ball.y += ball.dy * seconds 
    if ball.x < 0:
        ball.x = 0
        ball.dx *= -1 
    elif ball.x + ball.width > screenrect.width:
        ball.x = screenrect.width - ball.width
        ball.dx *= -1
    if ball.y < 0:
        ball.y = 0
        ball.dy *= -1
    elif ball.y + ball.height > screenrect.height:
        ball.y = screenrect.height - ball.height
        ball.dy *= -1
def run(width, height, fps):
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    screenrect = screen.get_rect()
    ball = Ball(10,10,50,50,60,50,25)
    screen.blit(ball.ballsurface, (ball.x, ball.y))
    background = pygame.Surface(screen.get_size()) 
    background.fill((255,255,255)) 
    background = background.convert()
    background2 = background.copy()
    screen.blit(background, (0,0))  
    pygame.draw.circle(ball.ballsurface, (0,0,255), (ball.width//2,ball.height//2), ball.radius)
    clock = pygame.time.Clock()
    mainloop = True
    FPS = fps
    playtime = 0
    paint_big_circles = False
    cleanup = True
    while mainloop:
        milliseconds = clock.tick(FPS)
        seconds = milliseconds / 1000.0 
        playtime += seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                elif event.key == pygame.K_1: 
                    FPS = 5
                elif event.key == pygame.K_2:
                    FPS = 20
                elif event.key == pygame.K_3:
                    FPS = 30
                elif event.key == pygame.K_4:
                    FPS = 40
                elif event.key == pygame.K_5:
                    FPS = 50
                elif event.key == pygame.K_6:
                    FPS = 60
                elif event.key == pygame.K_7:
                    FPS = 70
                elif event.key == pygame.K_8:
                    FPS = 80
                elif event.key == pygame.K_9:
                    FPS = 90
                elif event.key == pygame.K_0:
                    FPS = 1000 
                elif event.key == pygame.K_x:
                    paint_big_circles =  not paint_big_circles
                elif event.key == pygame.K_y:
                    cleanup = not cleanup
                elif event.key == pygame.K_w:
                    background.blit(background2, (0,0))
        pygame.display.set_caption("x: paint ({}) y: cleanup ({}) ,"
                   " w: white, 0-9: limit FPS to {}"
                   " (now: {:.2f})".format(
        paint_big_circles, cleanup, FPS,clock.get_fps()))
        if cleanup:
            screen.blit(background, (0,0))
        if paint_big_circles:
           wildPainting(background,screenrect)
        move(ball,seconds,screenrect)
        screen.blit(ball.ballsurface, (round(ball.x,0), round(ball.y,0 )))
        pygame.display.flip()
    print("This 'game' was played for {:.2f} seconds".format(playtime))
run(640,480,60)