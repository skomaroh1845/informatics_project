import pygame
import sys
# + Nick 08 05
from bullet import Bullet
# - Nick 08 05
from alien import Alien

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
def update (bg_color, screen, ship, bullets, aliens):  # Nick 08 05 added parameters: screen, bullets
    screen.fill(bg_color)
    # + Nick 08 05
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # - Nick 08 05
    ship.output()

    # + Dima 09 05
    aliens.draw(screen)
    # - Dima 09 05

    pygame.display.flip()
# - Dima 08 05


# + Nick 08 05
# создание армии пришельцев
def create_army(screen, aliens):
    # + Dima 09 05
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((500 - 2*alien_width)/alien_width)

    for alien_number in range(number_alien_x):
        alien = Alien(screen)
        alien.x = alien_width + alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


    # - Dima 09 05
# - Nick 08 05