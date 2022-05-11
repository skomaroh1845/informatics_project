# + Nick 12 05
import pygame

# игровой интерфейс
class Interface():

    # инициализация интерфейса
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (135, 195, 74)
        self.font = pygame.font.SysFont(None, 28)
        self.bg_color = (0, 0, 0)

    # рендер интерфейса
    def image_interface(self, tense):
        self.tense_img = self.font.render(tense, True, self.text_color, self.bg_color)
        self.tense_rect = self.score_img.get_rect()
        self.tense_rect.centerx = self.screen_rect.centerx
        self.tense_rect.centery = self.screen_rect.centery

    # отрисовка интерфейса
    def show_interface(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.tense_img, self.tense_rect)

    # заставка перехода на новый уровень
    def next_lvl(self):
        pass

    # меню игры
    def menu(self):
        pass

    # проверка выхода
    def exit(self):
        pass

    # окно паузы
    def pause(self):
        pass

# - Nick 12 05