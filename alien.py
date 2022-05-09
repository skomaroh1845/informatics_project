import pygame

# + Nick 08 05
# класс пришельца
class Alien(pygame.sprite.Sprite):

    # инициализация
    def __init__(self, screen):
        # + Dima 09 05
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # - Dima 09 05

    # рисование пришельца
    def draw(self):
        # + Dima 09 05
        self.screen.blit(self.image, self.rect)
        # - Dima 09 05

    # движение
    def update(self):
        pass


# - Nick 08 05