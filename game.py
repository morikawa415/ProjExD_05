import pygame as pg
import sys
import random

WIDTH = 500 # ウィンドウの幅
HEIGHT = 600 # ウィンドウの高さ 
player_speed = 5
clock =pg.time.Clock()

star_points = [
    (0, -50), (14, -20), (47, -15), (23, 7),
    (29, 40), (0, 25), (-29, 40), (-23, 7),
    (-47, -15), (-14, -20)

] #星の生成



class Star:
    """
    スターに関するクラス
    一定の確率で画面外から降ってくる
    """
    def __init__(self):
        self.x = random.randint(-WIDTH, WIDTH)
        self.y = random.randint(-100, 0)
        self.speed_x = random.uniform(1,2)
        self.speed_y = random.uniform(2, 1)
        self.scale = random.uniform(0.5, 1.0)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def draw(self, screen):
        transformed_points = [(point[0] * self.scale + self.x, point[1] * self.scale + self.y) for point in star_points]
        pg.draw.polygon(screen, (255, 255, 0), transformed_points)

stars = []
for _ in range(1):
    stars.append(Star())


def main():
    pg.display.set_caption("あらがえ！幼女ちゃん！")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex05/fig/pg_bg.png")
    bg_img2  = pg.transform.flip(pg.image.load("ex05/fig/pg_bg.png"), False, True)
    player_img = pg.image.load("ex05/fig/player.png")
    enemy_img = pg.image.load("ex05/fig/enemy.png")
    player_x = 250
    player_y = 500
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            player_x -= player_speed
        if keys[pg.K_RIGHT]:
            player_x += player_speed
        if keys[pg.K_UP]:
            player_y -= player_speed
        if keys[pg.K_DOWN]:
            player_y += player_speed

        tmr += 1
        y = tmr % 1200

        screen.blit(bg_img, [0, -y])
        screen.blit(bg_img2, [0, 600-y])
        screen.blit(bg_img, [0, 1200-y])
        screen.blit(player_img, (player_x, player_y))
        screen.blit(enemy_img, [250, 50])
        if random.random() < 0.7:  # 星が出る確率
            star = Star()
            stars.append(star)
            
        for star in stars:
            star.update()
            star.draw(screen)
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()