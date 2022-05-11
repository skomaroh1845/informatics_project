import pygame

# + Nick 08 05
# класс пришельца
class Alien(pygame.sprite.Sprite):

    # инициализация
    def __init__(self, screen, al_type=1):
        # + Dima 09 05
        super(Alien, self).__init__()
        self.screen = screen
        # + Nick 12 05
        self.type = al_type
        if al_type == 1:
            self.image = pygame.image.load('images/alien1.png')
        elif al_type == 2:
            self.image = pygame.image.load('images/alien2.png')
        elif al_type == 3:
            self.image = pygame.image.load('images/alien3.png')
        # - Nick 12 05
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
        # + Dima 09 05
        self.y += 1
        self.rect.y = self.y
        # - Dima 09 05


# - Nick 08 05