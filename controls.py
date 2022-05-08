import pygame
import sys


# обработка событий
# + Nick 07 05
def events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # + Dima 08 05
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.mright = True
            if event.key == pygame.K_a:
                ship.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.mright = False
            if event.key == pygame.K_a:
                ship.mleft = False
        # - Dima 08 05

# - Nick 07 05

# + Dima 08 05

# функция, делающая обновление экрана
def update (bg_color, screen, ship):
    screen.fill(bg_color)
    ship.output()
    pygame.display.flip()

# - Dima 08 05