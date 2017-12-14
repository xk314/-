import pygame,bullet
width = 512
hight = 768
class Airplane(object):
    __player_plane = ('res/hero.png', 'res/hero2.png')

    def __init__(self, model, win):
        self.model = model
        self.win = win
        self.speed = 3
        if self.model == 'player':
            self.plane = pygame.image.load(Airplane.__player_plane[1])
            self.plane_rect = self.plane.get_rect()  #该函数返回4个元素的列表，分别为左上角的坐标和图片的长宽
            self.bullet = [bullet.Bullet() for i in range(6)]
            # self.plane_rect.move_ip((self.window[0] - self.plane_rect[2]) / 2, self.window[1] - self.plane_rect[3] - 100)

    def plane_up(self):

        if self.plane_rect[1] > 0:
            self.plane_rect.move_ip(0,-self.speed)
            # self.win.window.blit(self.win.bg_img, (0, 0))
            self.win.window.blit(self.plane, (self.plane_rect[0], self.plane_rect[1]))
            # self.win.update()


    def plane_down(self):
        if self.plane_rect[1] <= hight - self.plane_rect[3]:
            self.plane_rect.move_ip(0,self.speed)
            # self.win.window.blit(self.win.bg_img, (0, 0))
            self.win.window.blit(self.plane, (self.plane_rect[0], self.plane_rect[1]))
            # self.win.update()

    def plane_left(self):
        if self.plane_rect[0] > 0:
            self.plane_rect.move_ip(-self.speed,0)
            # self.win.window.blit(self.win.bg_img, (0, 0))
            self.win.window.blit(self.plane, (self.plane_rect[0], self.plane_rect[1]))
            # self.win.update()

    def plane_right(self):
        if self.plane_rect[0] < width - self.plane_rect[2]:
            self.plane_rect.move_ip(self.speed,0)
            # self.win.window.blit(self.win.bg_img, (0, 0))
            self.win.window.blit(self.plane, (self.plane_rect[0], self.plane_rect[1]))
            # self.win.update()

    def shoot(self):
        for bullet in self.bullet:
            if not bullet.is_shot:
                bullet.bullet_rect[0] = self.plane_rect[0] + (self.plane_rect[2] - bullet.bullet_rect[2]) // 2
                bullet.bullet_rect[1] = self.plane_rect[1] - bullet.bullet_rect[3]
                bullet.is_shot = True
                break


