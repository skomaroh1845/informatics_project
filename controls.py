import pygame
import sys
from bullet import Bullet
from alien import Alien
import time
from random import randint
from bonuses import Bonus


# обработка событий
# + Nick 07 05
def events(screen, ship, bullets):
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
                if ship.bonus_guns > 0:
                    bullets.add(Bullet(screen, ship, shift=15))
                    bullets.add(Bullet(screen, ship, shift=-15))
                    ship.bonus_guns -= 1
                if ship.bonus_guns > 10:
                    bullets.add(Bullet(screen, ship, shift=30))
                    bullets.add(Bullet(screen, ship, shift=-30))
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
def update (bg_color, screen, ship, bullets, aliens, bonuses, stats):
    screen.fill(bg_color)
    # + Nick 08 05
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # - Nick 08 05
    ship.output()

    # + Dima 09 05
    aliens.draw(screen)
    # - Dima 09 05

    # + Nick 12 05
    bonuses.update()
    bonuses.draw(screen)
    bonuses_catch(ship, bonuses, stats)
    # - Nick 12 05

    pygame.display.flip()
# - Dima 08 05

# + Dima 09 05
def update_bullets (aliens, bullets, screen, bonuses):
    # обновляет позиции пуль и удаляет их
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # + Nick 10 05
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # + Nick 12 05
    for alien_list in collisions.values():
        for alien in alien_list:
            if alien.type == 2:
                new_bonus = Bonus(screen, alien.rect.centerx, alien.y, 'extra_life')
                bonuses.add(new_bonus)
            if alien.type == 3:
                new_bonus = Bonus(screen, alien.rect.centerx, alien.y, 'super_gun')
                bonuses.add(new_bonus)
    # - Nick 12 05
    # если всех убили, создаем новых
    if len(aliens) == 0:
        pass  # дописать 

    # - Nick 10 05
# - Dima 09 05

# + Dima 09 05
def update_aliens (ship, aliens, stats, bullets, screen, bonuses):
    # обновляет позиции пришельцев
    aliens.update()
    # + Nick 10 05
    for alien in aliens:
        if pygame.sprite.collide_mask(ship, alien):
            ship_death(stats, aliens, screen, ship, bullets, bonuses)
    aliens_check(stats, screen, ship, aliens, bullets)
    # - Nick 10 05
# - Dima 09 05

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
            a = randint(1, 15)
            if a > 3:
                alien = Alien(screen)
            else:
                alien = Alien(screen, a)
            alien.x = alien_width + alien_width * alien_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height*row_number

            aliens.add(alien)

    # - Dima 09 05
# - Nick 08 05

# + Nick 10 05
# столкновение пришельцев с кораблем
def ship_death(stats, aliens, screen, ship, bullets, bonuses):
    stats.lifes -= 1
    ship.bonus_guns = 0
    time.sleep(1)
    bonuses.empty()
    bullets.empty()
    aliens.empty()
    create_army(screen, aliens)
    ship.reset()

# проверка, дошли ли пришельцы до края
def aliens_check(stats, screen, ship, aliens, bullets):
    pass

# - Nick 10 05

# + Nick 12 05
def bonuses_catch(ship, bonuses, stats):
    for bonus in bonuses:
        if pygame.sprite.collide_mask(ship, bonus):
            if bonus.type == 'extra_life':
                if stats.lifes < 5:
                    stats.lifes += 1
            if bonus.type == 'super_gun':
                if ship.bonus_guns > 10 or ship.bonus_guns == 0:
                    ship.bonus_guns += 10
                else:
                    ship.bonus_guns = 20
            bonuses.remove(bonus)
# - Nick 12 05