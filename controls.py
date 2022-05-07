import pygame
import sys


# обработка событий
# + Nick 07 05
def events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # дописать обработку клавишь
        # вправо
        # влево

# - Nick 07 05