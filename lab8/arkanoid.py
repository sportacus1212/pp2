
import pygame
from random import randrange as rnd

# screen
WIDTH, HEIGHT = 1200, 700
fps = 60

# paddle
paddle_w = 250
paddle_h = 35
paddle_s = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT -
                     paddle_h - 10, paddle_w, paddle_h)

# ball
ball_r = 20
ball_s = 6
ball_rect = int(ball_r * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect),
                   HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# bricks
brick_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50)
              for i in range(10) for j in range(4)]
brick_colors = [(rnd(0, 60), rnd(0, 256), rnd(255, 256))
                for i in range(10) for j in range(4)]

pygame.init()

pygame.display.set_caption('Break Ball')
icon = pygame.image.load('breakball/images/break_ball.png')
pygame.display.set_icon(icon)

scr = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 450
text_y = 400


def game_over(x, y):
    message = font.render('The game is over...', True, (0, 0, 255))
    scr.blit(message, (x, y))


def you_win(x, y):
    message = font.render('YOU WIN IT!', True, (0, 0, 255))
    scr.blit(message, (x, y))


def collision_detection(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# keeps the game running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # game screen objects
    scr.fill((250, 235, 255))  # Color the screen (RGB) 150, 155, 160
    [pygame.draw.rect(scr, brick_colors[color], brick)  # give the bricks some color variety! Blue only.
     for color, brick in enumerate(brick_list)]
    pygame.draw.rect(scr, pygame.Color('purple'), paddle)
    pygame.draw.circle(scr, pygame.Color('red'), ball.center, ball_r)

    # ball physics
    ball.x += ball_s * dx
    ball.y += ball_s * dy
    if ball.centerx < ball_r or ball.centerx > WIDTH - ball_r:
        dx = -dx
    if ball.centery < ball_r:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = collision_detection(dx, dy, ball, paddle)
    hit_index = ball.collidelist(brick_list)
    if hit_index != -1:
        hit_rect = brick_list.pop(hit_index)
        hit_color = brick_colors.pop(hit_index)
        dx, dy = collision_detection(dx, dy, ball, hit_rect)
        fps += 5  # let's speed it up >:)

    # game over message
    if ball.bottom > HEIGHT:
        paddle_s = 0
        game_over(text_x, text_y)
    elif not len(brick_list):
        ball_s = 0
        paddle_s = 0
        you_win(text_x, text_y)

    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_s
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_s

    # screen refresh 60hz!
    pygame.display.flip()
    clock.tick(fps)