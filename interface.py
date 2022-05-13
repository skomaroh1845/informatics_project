# + Nick 12 05
import pygame

# игровой интерфейс
class Interface():

    # инициализация интерфейса
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (0, 0, 0)
        self.active_color = (204, 155, 8)
        self.font = pygame.font.SysFont(None, 36)
        self.font2 = pygame.font.SysFont(None, 48)
        self.bg_color = (145, 31, 31)
        self.text = {'SD': 'Space defenders',
                     'S': 'Start',
                     'E': 'Exit',
                     'lvl': 'Level ',
                     'GJ': 'Good job, you beat them!',
                     'B': 'But that is not all...',
                     'GL': 'Good luck!',
                     'win': 'You saved the Earth!',
                     'L': 'Aliens beat you!'}
        self.what_now = None
        self.rects_now = {}
        self.buttons = {'S': 0, 'E': 0, 'win': 0, 'L': 0}

    # рендер текста
    def interface_image(self, key, pos_x, pos_y, text_color, font='small', lvl=''):
        if font == 'small':
            self.text_img = self.font.render(self.text[key] + lvl, True, text_color, self.bg_color)
        elif font == 'big':
            self.text_img = self.font2.render(self.text[key] + lvl, True, text_color, self.bg_color)
        self.text_rect = self.text_img.get_rect()
        self.text_rect.centerx = pos_x
        self.text_rect.centery = pos_y
        if font == 'small' or key == 'win' or key == 'L':
            self.rects_now[key] = self.text_rect

    # заставка перехода на новый уровень
    def next_lvl(self, lvl):
        lvl = str(lvl)
        self.screen.fill(self.bg_color)
        # level
        self.interface_image('lvl', self.screen_rect.centerx, self.screen_rect.centery - 50, self.text_color, 'big', lvl)
        self.screen.blit(self.text_img, self.text_rect)
        # text
        if lvl == '1':
            self.interface_image('GL', self.screen_rect.centerx, self.screen_rect.centery, self.text_color, 'small')
            self.screen.blit(self.text_img, self.text_rect)
        else:
            self.interface_image('GJ', self.screen_rect.centerx, self.screen_rect.centery, self.text_color, 'small')
            self.screen.blit(self.text_img, self.text_rect)
            self.interface_image('B', self.screen_rect.centerx, self.screen_rect.centery + 50, self.text_color, 'small')
            self.screen.blit(self.text_img, self.text_rect)

    # меню игры
    def menu(self):
        self.what_now = 'menu'
        self.screen.fill(self.bg_color)
        # Name game
        self.interface_image('SD', self.screen_rect.centerx, self.screen_rect.centery - 60, self.text_color, 'big')
        self.screen.blit(self.text_img, self.text_rect)
        # Start
        if self.buttons['S'] == 1:
            color_start = self.active_color
        else:
            color_start = self.text_color
        self.interface_image('S', self.screen_rect.centerx, self.screen_rect.centery, color_start, 'small')
        self.screen.blit(self.text_img, self.text_rect)
        # Exit
        if self.buttons['E'] == 1:
            color_exit = self.active_color
        else:
            color_exit = self.text_color
        self.interface_image('E', self.screen_rect.centerx, self.screen_rect.centery + 40, color_exit, 'small')
        self.screen.blit(self.text_img, self.text_rect)

    # заставка победы
    def win(self):
        self.what_now = 'win'
        self.screen.fill(self.bg_color)
        # win
        if self.buttons['win'] == 1:
            color = self.active_color
        else:
            color = self.text_color
        self.interface_image('win', self.screen_rect.centerx, self.screen_rect.centery, color, 'big')
        self.screen.blit(self.text_img, self.text_rect)

    # заставка проигрыша
    def lose(self):
        self.what_now = 'lose'
        self.screen.fill(self.bg_color)
        # win
        if self.buttons['L'] == 1:
            color = self.active_color
        else:
            color = self.text_color
        self.interface_image('L', self.screen_rect.centerx, self.screen_rect.centery, color, 'big')
        self.screen.blit(self.text_img, self.text_rect)



    # проверяет положения курсора
    def check_mouse(self, pos):
        if self.what_now is None:
            self.rects_now.clear()
            return None
        else:
            for key in self.rects_now:
                for i in self.buttons:
                    self.buttons[i] = 0
                if self.rects_now[key].collidepoint(pos[0], pos[1]):
                    self.buttons[key] = 1
                    self.rects_now.clear()
                    self.what_now = None
                    return key

# - Nick 12 05