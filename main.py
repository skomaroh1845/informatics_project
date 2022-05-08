import pygame
import controls
from star_ship import StarShip

# + Nick 07 05
# функция запуска игры
def run():
    # инициализация
    pygame.init()
    screen = pygame.display.set_mode((700, 500))  # Dima changed: так у меня помещается окно на компе
    pygame.display.set_caption("Space defenders")
    bg_color = (0, 0, 0)
    ship = StarShip(screen)

    # цикл
    while True:
        controls.events(ship)
        ship.update_ship()
        controls.update(bg_color, screen, ship)


if __name__ == '__main__':
    run()
# - Nick 07 05