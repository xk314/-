import pygame, random
WIDTH, HIGHT = 512, 768

class Enemy(object):
    def __init__(self):
        num = str(random.randint(1, 7))
        self.img = pygame.image.load('res/img-plane_' + num + '.png')
        self.rect = self.img.get_rect()
        self.boom = pygame.image.load('res/bomb-1.png')
        self.boom_rect = self.boom.get_rect()
        self.is_boom = False
        self.reset()
        self.speed = 0

    def reset(self):
        self.rect[0] = random.randint(0, WIDTH - self.rect[2])
        self.rect[1] = -self.rect[3]
        self.speed = random.randint(3, 5)

        # self.speed = 4
    def boom_set(self):
        self.is_boom = False
        self.boom_rect[0] = -self.boom_rect[2]*2
        self.boom_rect[1] = -self.boom_rect[3]*2

    def enemy_move(self):
        if self.rect[1] >= HIGHT or self.rect[0] < -self.rect[2] or\
                self.rect[2] >= WIDTH + self.rect[2]:
            self.reset()
        self.rect.move_ip(random.randint(-5, 5), self.speed)

    def enemy_boom(self):
        # if not self.is_boom:
        self.boom_rect[0] = self.rect[0]
        self.boom_rect[1] = self.rect[1]
        self.is_boom = True
