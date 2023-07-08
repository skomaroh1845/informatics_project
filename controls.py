import pygame
import sys
from bullet import Bullet
from alien import Alien
import time
# by Nick branch
from random import randint
from bonuses import Bonus

# -------
# by Dmitrii branch
from game_stats import Stats
# -------

# обработка событий
# + Nick 07 05
def events(screen, ship, bullets, game_interface, stats, bonuses, sc):
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
                stats.bonus_bullets = ship.bonus_guns
            # - Nick 08 05
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.mright = False
            if event.key == pygame.K_a:
                ship.mleft = False
        # - Dima 08 05
        # + Nick 13 05
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            key = game_interface.check_mouse(event.pos)
            if key is not None:
                if key == 'S':  # start
                    stats.update_stats()
                    ship.bonus_guns = 0
                    bonuses.empty()
                    bullets.empty()
                    ship.reset()
                    sc.image_ships()
                    sc.image_score()
                    stats.run_game = True
                    game_interface.next_lvl(stats.lvl)  # заставка 1 уровня
                    pygame.display.flip()
                    time.sleep(1)
                elif key == 'E':  # exit
                    sys.exit()
                elif key == 'win':  # win -> back to menu
                    stats.win = False
                elif key == 'L':  # lose -> back to menu
                    stats.lose = False
        if event.type == pygame.MOUSEMOTION:
            game_interface.check_mouse(event.pos)
        # - Nick 13 05

# - Nick 07 05

# + Dima 08 05
# функция, делающая обновление экрана
def update (bg_color, screen, ship, bullets, aliens, stats, sc, bonuses):  # Nick 08 05 added parameters: screen, bullets
    screen.fill(bg_color)
    sc.show_score()
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
    bonuses_catch(ship, bonuses, stats, sc)
    # - Nick 12 05

    pygame.display.flip()
# - Dima 08 05

# + Dima 09 05
def update_bullets (screen, aliens, bullets, stats, sc, bonuses, game_interface):
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

    # + Dima 11 05
    if collisions:
        for aliens in collisions.values():
            stats.score += 10*len(aliens)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_ships()
    # - Dima 11 05

    # если всех убили, создаем новых
    if len(aliens) == 0:
        # + Dima 11 05
        bullets.empty()
        bonuses.empty()
        # + Nick 13 05
        stats.lvl += 1
        if stats.lvl > 5:
            game_interface.win()
            pygame.display.flip()
            stats.win = True
            stats.run_game = False
        else:
            game_interface.next_lvl(stats.lvl)
            pygame.display.flip()
            time.sleep(2)
        # - Nick 13 05
        create_army(screen, aliens)
        # - Dima 11 05

    # - Nick 10 05
# - Dima 09 05

# + Dima 09 05
def update_aliens (ship, aliens, stats, bullets, screen, sc, bonuses, game_interface):
    # обновляет позиции пришельцев
    aliens.update()
    # + Nick 10 05
    for alien in aliens:
        if pygame.sprite.collide_mask(ship, alien):
            ship_death(stats, aliens, screen, ship, bullets, sc, bonuses, game_interface)
    aliens_check(stats, aliens, screen, ship, bullets, sc, bonuses, game_interface)
    # - Nick 10 05
# - Dima 09 05

# + Dima 11 05
# проверяем, добрался ли хоть кто-то до края экрана
def aliens_check (stats, aliens, screen, ship, bullets, sc, bonuses, game_interface):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_death(stats, aliens, screen, ship, bullets, sc, bonuses, game_interface)
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
# + Nick 12 05
def bonuses_catch(ship, bonuses, stats, sc):
    for bonus in bonuses:
        if pygame.sprite.collide_mask(ship, bonus):
            if bonus.type == 'extra_life':
                if stats.lifes < 5:
                    stats.lifes += 1
                    sc.image_ships()
            if bonus.type == 'super_gun':
                if ship.bonus_guns > 10 or ship.bonus_guns == 0:
                    ship.bonus_guns += 10
                else:
                    ship.bonus_guns = 20
                stats.bonus_bullets = ship.bonus_guns
                sc.image_score()
            bonuses.remove(bonus)
# - Nick 12 05

def ship_death(stats, aliens, screen, ship, bullets, sc, bonuses, game_interface):
    # + Dima 11 05
    if stats.lifes > 0:
        stats.lifes -= 1
        ship.bonus_guns = 0
        time.sleep(0.5)
        # + Nick 13 05
        if stats.lifes == 0:
            game_interface.lose()
            pygame.display.flip()
            stats.lose = True
            stats.run_game = False
        # - Nick 13 05
        bonuses.empty()
        bullets.empty()
        aliens.empty()
        create_army(screen, aliens)
        ship.reset()
        sc.image_ships()
    # - Dima 11 05

# - Nick 10 05

# + Dima 11 05
def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
# - Dima 11 05
