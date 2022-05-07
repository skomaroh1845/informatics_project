import pygame

# + Nick 07 05
class StarShip():

    # инициализация
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/star_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    # рисование пушки
    def output(self):
        pass

    # обновление позиции корабля
    def update_ship(self):
        pass

# - Nick 07 05