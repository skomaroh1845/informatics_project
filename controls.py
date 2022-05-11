import pygame
import sys
from bullet import Bullet
from alien import Alien
import time
from game_stats import Stats


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

# + Dima 09 05
def update_bullets (screen, aliens, bullets):
    # обновляет позиции пуль и удаляет их
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # + Nick 10 05
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # если всех убили, создаем новых
    if len(aliens) == 0:
        # + Dima 11 05
        bullets.empty()
        create_army(screen, aliens)
        # - Dima 11 05

    # - Nick 10 05
# - Dima 09 05

# + Dima 09 05
def update_aliens (ship, aliens, stats, bullets, screen):
    # обновляет позиции пришельцев
    aliens.update()
    # + Nick 10 05
    for alien in aliens:
        if pygame.sprite.collide_mask(ship, alien):
            ship_death(stats, aliens, screen, ship, bullets)
    aliens_check(stats, aliens, screen, ship, bullets)
    # - Nick 10 05
# - Dima 09 05

# + Dima 11 05
# проверяем, добрался ли хоть кто-то до края экрана
def aliens_check (stats, aliens, screen, ship, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_death(stats, aliens, screen, ship, bullets)
            break
# - Dima 11 05

# + Nick 08 05
# создание армии пришельцев
def create_army(screen, aliens):
    # + Dima 09 05
    alien = Alien(screen)
    alien_width = alien.rect.width + 5  # Nick 10 05 добавил пустого места между пришельцами
    number_alien_x = int((500 - 2*alien_width)/alien_width)
    alien_height = alien.rect.height + 5  # Nick 10 05 добавил пустого места между пришельцами
    number_alien_y = int((500 - 52 - 2*alien_height) / alien_height)
    for row_number in range(number_alien_y - 2):  # Nick 10 05 уменьшил число рядов
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height*row_number

            aliens.add(alien)

    # - Dima 09 05
# - Nick 08 05

# + Nick 10 05
# столкновение пришельцев с кораблем
def ship_death(stats, aliens, screen, ship, bullets):
    # + Dima 11 05
    if (stats.lifes > 0):
        stats.lifes -= 1
        time.sleep(1)
        bullets.empty()
        aliens.empty()
        create_army(screen, aliens)
        ship.reset()
    else:
        stats.run_game = False
        sys.exit()
    # - Dima 11 05


# - Nick 10 05