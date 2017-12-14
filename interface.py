import pygame, sys, airplane, map, enemy,time


class Interface(object):
    __window = [512, 768]
    __instance = None
    __first = True
    caption = '飞机大战'
    icon_img = 'res/game.ico'
    bg_img = 'res/img_bg_level_2.jpg'
    bg_music = 'res/bg.wav'

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if Interface.__first:
            Interface.__first = False
            pygame.init()
            self.window = pygame.display.set_mode(Interface.__window)
            self.player_plane = None
            # self.bg_img = pygame.image.load(Interface.bg_img)
            self.logo_img = pygame.image.load(Interface.icon_img)
            self.map = map.Map()
            self.enemy = [enemy.Enemy() for i in range(6)]




    def set_win(self):
            pygame.display.set_caption(Interface.caption)

            pygame.display.set_icon(self.logo_img)

            # self.window.blit(self.bg_img, (0, 0))
            self.start_music()
            self.update()

    def update(self):
        pygame.display.update()

    def start_music(self):
        pygame.mixer.music.load(Interface.bg_music)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def add_player(self):
        self.player_plane = airplane.Airplane('player', self)
        x = (self.__window[0] - self.player_plane.plane_rect[2]) / 2
        y = self.__window[1] - self.player_plane.plane_rect[3] - 50
        self.player_plane.plane_rect.move_ip(x, y)
        self.window.blit(self.player_plane.plane, (x, y))

    def show_plane(self):
        x = self.player_plane.plane_rect[0]
        y = self.player_plane.plane_rect[1]

        self.window.blit(self.player_plane.plane, (x, y))

    def show_bullt(self):
        for bullet in self.player_plane.bullet:
            if bullet.is_shot:
                self.window.blit(bullet.bullet_img, (bullet.bullet_rect[0], bullet.bullet_rect [1]))


    def map_down(self):
        self.map.move_down()
        self.window.blit(self.map.map_img2, (0, self.map.map_img2_y ))
        self.window.blit(self.map.map_img1, (0, self.map.map_img1_y))

    def bullet_move(self):
        for bullet in self.player_plane.bullet:
            if bullet.is_shot:
                bullet.move_up()

    def enemy_move(self):
        for enemy_plane in self.enemy:
            enemy_plane.enemy_move()

    def show_enemy(self):
        print('show   enemy')
        for enemy_plane in self.enemy:
            self.window.blit(enemy_plane.img, (enemy_plane.rect[0], enemy_plane.rect[1]))
            print(enemy_plane.rect[0], enemy_plane.rect[1])

    def boom(self):
        for bullet in self.player_plane.bullet:
            for enemy_plane in self.enemy:
                if pygame.Rect.colliderect(enemy_plane.rect, bullet.bullet_rect):
                    enemy_plane.enemy_boom()
                    enemy_plane.reset()
                    bullet.bullet_rect[0] = -bullet.bullet_rect[2]
                    bullet.bullet_rect[1] = -bullet.bullet_rect[3]
                    bullet.is_shot = False


    def show_boom(self):
        for enemy_plane in self.enemy:
            if enemy_plane.is_boom:
                print('爆炸绘图')
                self.window.blit(enemy_plane.boom, (enemy_plane.boom_rect[0], enemy_plane.boom_rect[1]))
                time.sleep(0.1)
                enemy_plane.boom_set()



    def event(self):
        while True:
            self.map_down()
            self.show_plane()
            self.bullet_move()
            self.show_bullt()
            self.enemy_move()
            self.show_enemy()
            self.boom()
            self.show_boom()

            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    print('关闭窗口')
                    sys.exit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('按下空格，发射子弹')
                        self.player_plane.shoot()
            pressed_key = pygame.key.get_pressed()

            if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
                print('按下了W和 方向键上')
                self.player_plane.plane_up()
                self.update()
            if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
                print('按下了W或 方向键上')
                self.player_plane.plane_up()
            if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
                print('按下了S或 方向键下')
                self.player_plane.plane_down()
            if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
                print('按下了A或 方向键左')
                self.player_plane.plane_left()
            if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
                print('按下了D或 方向键右')
                self.player_plane.plane_right()

            if pressed_key[pygame.K_n]:
                self.stop_music()
                print('按下N 关闭背景音乐')
            if pressed_key[pygame.K_s]:
                print('按下s 开启背景音乐')
                self.start_music()
            self.update()





