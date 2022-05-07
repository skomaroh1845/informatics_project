import pygame
import sys

# print ('5')

# функция запуска игры
def run():
    # инициализация
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Space defenders")
    bg_color = (0, 0, 0)

    # цикл
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)


if __name__ == '__main__':
    run()