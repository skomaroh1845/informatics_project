# + Dima 11 05
import pygame.font
from star_ship import StarShip
from pygame.sprite import Group

class Scores():
    '''Отвечает за вывод информации по очкам'''
    def __init__ (self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (135, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_ships()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)

    def image_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.lifes):
            ship = StarShip(self.screen)
            ship.rect.x = 15 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)

# - Dima 11 05