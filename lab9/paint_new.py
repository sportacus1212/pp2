# PAINT

import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((700, 700))
FPS = 60
pygame.display.set_caption('Paint')

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

back_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\back.png")
red_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\red.png")
blue_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\blue.png")
green_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\green.png")
white_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\white.png")
yellow_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\yellow.png")
rect_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\rect.png")
tria_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\tria.png")
circle_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\circle.png")
square_choose = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\square.png")
eraser = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab9\image\eraser.png")

pos, cur, rect = None, None, None

select = WHITE
size = 3
x = 0
y = 0

done = True
while done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()

        if pos:
            pygame.draw.line(screen, select, pos, cur, size)
            pos = cur

        if event.type == pygame.MOUSEBUTTONUP:
            pos = None
            rect = None

        elif pos:
            x = pos[0]
            y = pos[1]

            if x >= 20 and x <= 45 and y >= 20 and y <= 45:
                select = RED
            elif x >= 70 and x <= 95 and y >= 20 and y <= 45:
                select = BLUE
            elif x >= 120 and x <= 145 and y >= 20 and y <= 45:
                select = GREEN
            elif x >= 170 and x <= 195 and y >= 20 and y <= 45:
                select = WHITE
            elif x >= 220 and x <= 245 and y >= 20 and y <= 45:
                select = YELLOW
            elif x >= 290 and x <= 350 and y >= 10 and y <= 70:
                pygame.draw.rect(screen, select, (randint(20, 580), randint(95, 600), 120, 80))
            elif x >= 370 and x <= 410 and y >= 10 and y <= 70:
                pygame.draw.polygon(screen, select, [(173, 400), (233, 300), (293, 400)], 0)
            elif x >= 430 and x <= 470 and y >= 10 and y <= 70:
                pygame.draw.ellipse(screen, select, (randint(20, 580), randint(95, 600), 80, 80))
            elif x >= 490 and x <= 530 and y >= 10 and y <= 70:
                pygame.draw.rect(screen, select, (randint(20, 580), randint(95, 600), 80, 80))
            elif x >= 635 and x <= 685 and y >= 10 and y <= 70:
                select = BLACK

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_RIGHT]:
        if size <= 100:
            size = size + 1
        else:
            size = 100
    if pressed[pygame.K_LEFT]:
        if size > 3:
            size = size - 1
        else:
            size = 3

    clock.tick(FPS)

    screen.blit(back_choose, (0, 0))
    screen.blit(red_choose, (20, 20))
    screen.blit(blue_choose, (70, 20))
    screen.blit(green_choose, (120, 20))
    screen.blit(white_choose, (170, 20))
    screen.blit(yellow_choose, (220, 20))
    screen.blit(rect_choose, (300, 20))
    screen.blit(tria_choose, (380, 20))
    screen.blit(circle_choose, (440, 20))
    screen.blit(square_choose, (500, 20))
    screen.blit(eraser, (640, 20))

    pygame.display.flip()