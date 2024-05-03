import pygame as pg
import random

pg.init()

w, h, fps = 400, 600, 60
is_running = True
screen = pg.display.set_mode((w, h))
pg.display.set_caption('racer')
clock = pg.time.Clock()
y = 0
ry = 2
step, enemy_step, enemy_step2, score, score_coin = 5, 5, 6, 0, 0
game_over_image = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\images\gameover.jpg")
game_over_image = pg.transform.scale(game_over_image, (w, h))
bg = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\AnimatedStreet.png")
bg = pg.transform.scale(bg, (w, h))
score_font = pg.font.SysFont("Verdana", 20)
score_coins = pg.font.SysFont("Verdana", 20)
pg.mixer.music.load(r"C:\Users\nurzh\Desktop\pp2\lab8\background.wav")
pg.mixer.music.play(-1)

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step)
        if self.rect.bottom > h + 90:
            score += 1
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\Enemy2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step2)
        if self.rect.bottom > h + 90:
            score += 1
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pg.K_a]:
            self.rect.move_ip(-step, 0)
        if self.rect.right < w and pressed_keys[pg.K_d]:
            self.rect.move_ip(step, 0)
        if self.rect.top > 0 and pressed_keys[pg.K_w]:
            self.rect.move_ip(0, -step)
        if self.rect.bottom < h and pressed_keys[pg.K_s]:
            self.rect.move_ip(0, step)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__(self, value=1):
        super().__init__()
        if value == 1:
            self.image = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\images\coin.png")
        elif value == 5:
            self.image = pg.image.load(r"C:\Users\nurzh\Desktop\pp2\lab8\images\coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130))
        self.value = value

    def draw(self):
        screen.blit(self.image, self.rect)

p = Player()
e = Enemy()
e2 = None
enemies = pg.sprite.Group()
enemies.add(e)
coins = pg.sprite.Group()

crash_sound = pg.mixer.Sound(r"C:\Users\nurzh\Desktop\pp2\lab8\crash.wav")

def spawn_coin():
    coin_values = [1, 5]
    coin_value = random.choice(coin_values)
    new_coin = Coin(coin_value)
    coins.add(new_coin)

spawn_coin()

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    screen.blit(bg, (0, y % h))
    screen.blit(bg, (0, -h + (y % h)))
    y += ry

    p.update()

    for coin in coins:
        coin.draw()
        if pg.sprite.collide_rect(p, coin):
            score_coin += coin.value
            coin.kill()
            spawn_coin()

    e.update()
    e.draw(screen)
    p.draw(screen)
    
    if score_coin > 20 and e2 is None:
        e2 = Enemy2()
        enemies.add(e2)

    if e2:
        e2.update()
        e2.draw(screen)

    if pg.sprite.spritecollideany(p, enemies) or p.rect.left <= 0 or p.rect.right >= w:
        crash_sound.play()
        pg.mixer.music.stop()
        screen.blit(game_over_image, (0, 0))
        pg.display.flip()
        pg.time.wait(2000)
        is_running = False

    score_coins_rendered = score_coins.render(f'Coins: {score_coin}', True, 'white')
    screen.blit(score_coins_rendered, (300, 10))

    pg.display.flip()

pg.quit()
