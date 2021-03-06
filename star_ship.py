import pygame
from pygame.sprite import Sprite

# + Nick 07 05
class StarShip(Sprite):

    # инициализация
    def __init__(self, screen, size='big'):
        super(StarShip, self).__init__()
        self.screen = screen
        if size == 'big':
            self.image = pygame.image.load('images/star_ship.png')
        elif size == 'small':
            self.image = pygame.image.load('images/star_ship_small.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx) # Dima changed: явно указал тип float для центра прямоугольника, символизирующего корабль
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.bonus_guns = 0

    # рисование пушки
    def output(self):
        # + Dima 08.05
        self.screen.blit(self.image, self.rect)
        # - Dima 08.05

    # обновление позиции корабля
    def update_ship(self):
        # + Dima 08.05
        if (self.mright) and (self.rect.right < self.screen_rect.right):
            self.center += 3.5

        if (self.mleft) and (self.rect.left > 0):
            self.center -= 3.5

        self.rect.centerx = self.center
        # - Dima 08.05

    # + Nick 10 05
    # перезагрузка корабля после столкновения
    def reset(self):
        self.center = self.screen_rect.centerx
    # - Nick 10 05


# - Nick 07 05