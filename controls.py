import pygame
import sys
# + Nick 08 05
from bullet import Bullet
# - Nick 08 05

# обработка событий
# + Nick 07 05
def events(screen, ship, bullets):  # Nick 08 05 added parameters: screen, bullets
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # + Dima 08 05
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.mright = True
            if event.key == pygame.K_a:
                ship.mleft = True
            # + Nick 08 05
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
            # - Nick 08 05
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.mright = False
            if event.key == pygame.K_a:
                ship.mleft = False
        # - Dima 08 05

# - Nick 07 05

# + Dima 08 05
# функция, делающая обновление экрана
def update (bg_color, screen, ship, bullets):  # Nick 08 05 added parameters: screen, bullets
    screen.fill(bg_color)
    # + Nick 08 05
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # - Nick 08 05
    ship.output()
    pygame.display.flip()
# - Dima 08 05


# + Nick 08 05
# создание армии пришельцев
def create_army(screen, aliens):
    pass
# - Nick 08 05