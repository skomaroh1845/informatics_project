import pygame
import controls
from star_ship import StarShip
from pygame.sprite import Group
from game_stats import Stats
from scores import Scores # added by Dima 11 05
from interface import Interface
import time  # для отладки

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

    # + Nick 10 05
    # для задания скорости обновления
    clock = pygame.time.Clock()
    # статистика
    stats = Stats()
    # - Nick 10 05

    # + Nick 12 05
    bonuses = Group()
    game_interface = Interface(screen)

    # - Nick 12 05

    # + Dima 11 05
    sc = Scores(screen, stats)
    # - Dima 11 05

    # цикл
    while True:
        controls.events(screen, ship, bullets, game_interface, stats, bonuses, sc)
        # + Nick 13 05
        if not stats.run_game:
            if stats.win:
                game_interface.win()
            elif stats.lose:
                game_interface.lose()
            else:
                game_interface.menu()
            pygame.display.flip()
        # - Nick 13 05
        # + Dima 11 05
        if stats.run_game:
            ship.update_ship()
            # + Nick 08 05
            bullets.update()
            # - Nick 08 05
            controls.update(bg_color, screen, ship, bullets, aliens, stats, sc, bonuses)
            # + Dima 09 05
            controls.update_bullets(screen, aliens, bullets, stats,  sc, bonuses, game_interface)
            controls.update_aliens(ship, aliens, stats, bullets, screen, sc, bonuses, game_interface)
            # - Dima 09 05
        # - Dima 11 05
        # + Nick 10 05
        clock.tick(60)  # 60 FPS
        # - Nick 10 05

if __name__ == '__main__':
    run()
# - Nick 07 05