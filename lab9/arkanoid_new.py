import pygame
import random
import sys

pygame.init()

# Screen dimensions and FPS
W, H = 1200, 800
FPS = 60

# Initialize the screen and clock
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle settings
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball settings
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1  # Initialize ball movement direction

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
path = r"C:\Users\nurzh\Desktop\pp2\lab8\sounds\catch.mp3"
collision_sound = pygame.mixer.Sound(path)

# Lives
max_lives = 3
lives = max_lives
heart_img = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\images\small_heart.png")
heart_spacing = 40

# Function to draw hearts indicating remaining lives
def draw_hearts():
    for i in range(lives):
        screen.blit(heart_img, (W - 90 - i * heart_spacing, 15))

# Function to handle collision detection between the ball and other objects
def detect_collision(dx, dy, ball, rect):
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
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Menu functions
menu_font = pygame.font.SysFont('comicsansms', 40)

# Main menu function
def main_menu():
    global done
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_s:
                    settings_menu()

        screen.fill(bg)
        title_text = menu_font.render('Main Menu', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(W // 2, H // 2 - 100))
        start_text = menu_font.render('Press "ENTER" to start', True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(W // 2, H // 2))
        settings_text = menu_font.render('Press "S" for settings', True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(W // 2, H // 2 + 100))

        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(settings_text, settings_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Settings menu function
def settings_menu():
    global paddleSpeed, ballSpeed
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_UP:
                    paddleSpeed += 1
                elif event.key == pygame.K_DOWN:
                    paddleSpeed -= 1
                elif event.key == pygame.K_RIGHT:
                    ballSpeed += 1
                elif event.key == pygame.K_LEFT:
                    ballSpeed -= 1

        screen.fill(bg)
        title_text = menu_font.render('Settings', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(W // 2, 50))
        paddle_text = menu_font.render(f'Paddle Speed: {paddleSpeed}', True, (255, 255, 255))
        paddle_rect = paddle_text.get_rect(center=(W // 2, H // 2 - 50))
        ball_text = menu_font.render(f'Ball Speed: {ballSpeed}', True, (255, 255, 255))
        ball_rect = ball_text.get_rect(center=(W // 2, H // 2 ))
        back_text = menu_font.render('Press "ESC" to go back', True, (255, 255, 255))
        back_rect = back_text.get_rect(center=(W // 2, H - 50))

        screen.blit(title_text, title_rect)
        screen.blit(paddle_text, paddle_rect)
        screen.blit(ball_text, ball_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Pause menu function
def pause_menu():
    global done
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_s:
                    settings_menu()

        screen.fill(bg)
        pause_text = menu_font.render('Game Paused', True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(W // 2, H // 2 - 100))
        resume_text = menu_font.render('Press ENTER to resume', True, (255, 255, 255))
        resume_rect = resume_text.get_rect(center=(W // 2, H // 2))
        settings_text = menu_font.render('Press S for settings', True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(W // 2, H // 2 + 100))

        screen.blit(pause_text, pause_rect)
        screen.blit(resume_text, resume_rect)
        screen.blit(settings_text, settings_rect)

        pygame.display.flip()
        clock.tick(FPS)


# Main game loop
def game_loop():
    global done, dx, dy, ballSpeed, paddleSpeed, paddle, ball, game_score, block_list, color_list, lives
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu()

        screen.fill(bg)

        # Draw blocks, paddle, and ball
        [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

        # Move the ball
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        # Ball collision with walls
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        if ball.centery < ballRadius + 50:
            dy = -dy

        # Ball collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        # Ball collision with blocks
        hitIndex = ball.collidelist(block_list)
        if hitIndex != -1:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()

        # Update game score display
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        # Handle ball falling off the screen
        if ball.bottom > H:
            lives -= 1
            ball.x = random.randrange(ball_rect, W - ball_rect)
            ball.y = H // 2
            dx, dy = 1, -1
            if lives == 0:
                screen.fill((0, 0, 0))
                screen.blit(losetext, losetextRect)
                pygame.display.flip()
                pygame.time.delay(2000)  # Delay before closing the game
                done = True

        # Check if all blocks are destroyed
        if not len(block_list):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)
            pygame.display.flip()
            pygame.time.delay(2000)  # Delay before closing the game
            done = True

        # Move the paddle based on key input
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

        # Draw remaining lives
        draw_hearts()

        pygame.display.flip()
        clock.tick(FPS)

# Start the main menu and then the game loop
main_menu()
game_loop()

# Clean up and exit
pygame.quit()
sys.exit()



