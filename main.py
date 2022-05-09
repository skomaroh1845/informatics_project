import pygame
import controls
from star_ship import StarShip
# + Nick 08 05
from pygame.sprite import Group
# - Nick 08 05

# + Nick 07 05
# функция запуска игры
def run():
    # инициализация
    pygame.init()
    screen = pygame.display.set_mode((500, 500))  # Dima changed: так у меня помещается окно на компе
    pygame.display.set_caption("Space defenders")
    bg_color = (0, 0, 0)
    ship = StarShip(screen)
    # + Nick 08 05
    bullets = Group()
    # - Nick 08 05

    # + Dima 09 05
    aliens = Group()
    controls.create_army(screen, aliens)
    # - Dima 09 05

    # цикл
    while True:
        controls.events(screen, ship, bullets)
        ship.update_ship()
        # + Nick 08 05
        bullets.update()
        # - Nick 08 05
        controls.update(bg_color, screen, ship, bullets, aliens)
        # + Dima 09 05
        controls.update_bullets(bullets)
        controls.update_aliens(aliens)
        # + Dima 09 05


if __name__ == '__main__':
    run()
# - Nick 07 05