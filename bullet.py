import pygame

# + Nick 08 05
class Bullet(pygame.sprite.Sprite):

    # создание пули в позиции пушки
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 255, 153, 0
        self.speed = 0.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # движение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # рисование пули
        pygame.draw.rect(self.screen, self.color, self.rect)

# - Nick 08 05