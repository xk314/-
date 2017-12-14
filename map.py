import pygame, random
width, hight = 512, 768
class Map(object):
    def __init__(self):
        num = random.randint(1, 5)
        self.map_img1 = pygame.image.load('res/img_bg_level_' + str(num) + '.jpg')
        self.map_img2 = pygame.image.load('res/img_bg_level_' + str(num) + '.jpg')
        self.map_img1_y = -hight
        self.map_img2_y = 0
        self.speed = 2

    def move_down(self):    #在map类的方法中将对象的坐标修改，在拥有该类实例化对象的类中在画图
        if self.map_img1_y >= 0:
            self.map_img1_y = -hight
            self.map_img2_y = 0
        self.map_img1_y += self.speed
        self.map_img2_y += self.speed

