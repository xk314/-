import pygame
class Bullet(object):
    def __init__(self):
        self.bullet_img = pygame.image.load('res/hero_bullet_7.png')
        self.bullet_rect = self.bullet_img.get_rect()
        self.is_shot = False
        self.speed = 5

    def move_up(self):
         self.bullet_rect.move_ip(0, -self.speed)
         if self.bullet_rect[1] < -self.bullet_rect[3]:
             self.is_shot = False