import pygame
from random import randint

pygame.init()

BACK = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\AnimatedStreet.png")
WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Racer Game')

font_score = pygame.font.SysFont("Verdana", 22)
font_over = pygame.font.SysFont("Verdana", 30)

pygame.mixer.music.load(r"C:\Users\nurzh\Desktop\pp2\lab8\sounds\music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 60)

    def update(self):

        pressed_keys = pygame.key.get_pressed()

        if self.rect.x > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-car_speed, 0)
        if self.rect.x < WIDTH - 115:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(car_speed, 0)


class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\images\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, WIDTH - 40), 0)

    def reset_pos(self):
        self.rect.y = 0
        self.rect.x = randint(40, WIDTH - 40)

    def update(self):
        self.rect.move_ip(0, coin_speed)
        if self.rect.y > 800:
            self.reset_pos()
            pygame.mixer.music.stop()
            screen.fill((0, 0, 0))
            game_over = font_over.render(f'GAME OVER, YOU LOSE', True, (255, 0, 0))
            screen.blit(game_over, (73, 350))
            pygame.display.flip()
            # Remove the time.sleep(2) call
            # time.sleep(2)
            pygame.quit()


P1 = Player()
C1 = Coin()

coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)

score = 0
level = 1
coin_speed = 7
car_speed = 8

done = True
while done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.blit(BACK, (0, 0))
    clock.tick(60)

    for i in all_sprites:
        screen.blit(i.image, i.rect)
        i.update()

    point_add = pygame.sprite.spritecollide(P1, coins, False)
    score_add = font_score.render(f'Score {str(score)}', True, (255, 255, 255))
    level_add = font_score.render(f'Level {str(level)}', True, (255, 255, 255))
    screen.blit(score_add, (42, 8))
    screen.blit(level_add, (150, 8))

    for i in point_add:
        C1.reset_pos()
        score += 1
        if score == 10 or score == 20 or score == 30 or score == 40 or score == 50:
            level += 1
            coin_speed += 3
            car_speed += 1.5
        sound = pygame.mixer.Sound(r"C:\Users\nurzh\Desktop\pp2\lab8\sounds\coin.mp3")
        pygame.mixer.Sound.play(sound)

    if level == 5:
        pygame.mixer.music.stop()
        screen.fill((0, 0, 0))
        game_over = font_over.render(f'GAME OVER, YOU WIN', True, (255, 0, 0))
        screen.blit(game_over, (75, 350))
        pygame.display.flip()
        # Remove the time.sleep(2) call
        # time.sleep(2)
        done = False

    pygame.display.update()

pygame.quit()
