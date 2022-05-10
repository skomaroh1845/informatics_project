import pygame


# + Nick 12 05
class Bonus(pygame.sprite.Sprite):

    # инициализация бонуса
    def __init__(self, screen, x, y, bun_type):
        super(Bonus, self).__init__()
        self.screen = screen
        self.type = bun_type
        if bun_type == 'extra_life':
            self.image = pygame.image.load('images/extra_life.png')
        elif bun_type == 'super_gun':
            self.image = pygame.image.load('images/super_gun.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # рисование бонуса
    def draw(self):
        self.screen.blit(self.image, self.rect)

    # движение бонуса
    def update(self):
        self.y += 1.5
        self.rect.y = self.y


# - Nick 12 05