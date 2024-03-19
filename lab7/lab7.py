import pygame
import datetime

pygame.init()

HEIGHT = 800
WIDTH = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mickeyclock")
clock = pygame.time.Clock()

mickeyclock = pygame.image.load("lab7/images/main-clock.png")
minure_arrow = pygame.image.load("lab7/images/right-hand.png")
second_arrow = pygame.image.load("lab7/images/left-hand.png")


def time(t):
    return 360 - t * 6


def rotateee(surface, image, left_pos, angle):
    transformed_image = pygame.transform.rotate(image, angle)
    new_figure = transformed_image.get_rect(center=image.get_rect(topleft=left_pos).center)

    surface.blit(transformed_image, new_figure)


running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    if (running == False):
        break

    screen.blit(mickeyclock, (0, 0))
    t = datetime.datetime.now()
    angle_sec = time(t.second)
    angle_min = time(t.minute)
    rotateee(screen, second_arrow, (400, 400), angle_sec)
    rotateee(screen, minure_arrow, (400, 400), angle_min)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


