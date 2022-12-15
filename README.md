## Class Description 
#### Nikolay Komarov, Dmitry Vladimirtsev

### class StarShip
The class of the ship the player plays as
#### Fields
Inherits the fields of the `pygame.Sprite` class and has the fields:
1. `self.screen` - stores reference to the screen object
2. `self.image` - stores the picture of the object
3. `self.rect` - stores rectangle, which interprets the picture, and its coordinates
4. `self.screen_rect` - stores rectangle interpreting the screen and its coordinates
5. `self.mright` - `True` when moving to the right, by default `False`.
6. `self.mleft` - `True` when moving to the left, by default `False`.
7. `self.bonus_guns` - the number of bonus shots 
#### Methods
Inherits methods from the class `pygame.Sprite` and has:
1. `__init__(self, screen, size='big')` - initializes class, `screen` screen object and `size` ship size (`big` is big, `small` is small) are passed as arguments.
2. `Output(self)` - draws on the screen a picture of the ship
3. `update_ship(self)` - updates ship position
4. `Reset(self)` - returns ship to initial position

### class Bullet
Class of bullets which are fired by the ship
#### Fields
Inherits the fields of class `pygame.Sprite` and has fields:
1. `self.screen` - stores reference to the screen object
2. `Self.rect` - stores rectangle, and its coordinates
3. `self.color` - the color of the bullet
4. `self.speed` - speed of the bullet
5. `self.y` - stores real coordinate value (needed for smooth motion)
#### Methods
Inherits methods from pygame.Sprite class and has:
1. `__init__(self, screen, ship, shift=0)` method initializes the class, passing as arguments a screen object - `screen`, a player ship object - `hip` and a bullet offset relative to the bow of the ship in pixels - `shift`.
2. `update(self)` - update bullet's position (overritted).
3. `draw_bullet(self)` - draws the bullet on the screen

### class Bonus
Bonus class
#### Fields
Inherits the fields of the class `pygame.Sprite` and has fields:
1. `self.screen` - stores reference to screen object
2. `self.type` - type of bonus 
3. `self.image` - stores the picture of the object
4. `self.rect` - stores rectangle, and its coordinates
5. `self.x` - stores real coordinate value (needed for smooth movement)
7. `self.y` - stores real value of coordinate (it's necessary for smooth movement)
#### Methods
Inherits the methods of the pygame.Sprite class and has:
1. `__init__(self, screen, x, y, bun_type)` - initializes class, passing as arguments screen object - `screen`, coordinates - `x, y`, and bonus type - `bun_type` (`'extra_life'` - extra life, `'super_gun'` - bonus gun)
2. `update(self)` - update the position of the bonus (overritted)
3. `draw(self)` - draws bonus on the screen

### class Stats
The class responsible for keeping game stats
#### Fields
1. `self.run_game` - `True` if game started, `False` by default
2. `Self.lifes` - number of lives.
3. `self.score` - current score
4. `self.win` - True if player wins, False by default 
5. `self.lose` - True if player lost, False by default.
7. `self.lvl` - Current level
8. `self.high_score` - record score
#### Methods
Inherits the methods of the pygame.Sprite class and has:
1. `__init__(self)` - initializes the class
2. `update_stats(self)` - sets the initial stats

### class Scores.
The class responsible for displaying the information of class `Stats` on the screen
#### Fields
1. `self.screen` - stores reference to the screen object
2. `self.screen_rect` - stores rectangle interpreting the screen and its coordinates
3. `self.stats` - stores reference to an object of class
4. `self.text_color` - color of the text.
5. `self.font` - font
6. `self.score_img` - render a picture of the account text
7. `self.score_rect` - render rectangle of the score text picture
8. `self.high_score_image` - render picture of the score text
9. `self.high_score_rect` - rectangle renderer of the score text image
10. `self.ships` - array of small ships to draw lives 
#### Methods
1. `__init__(self, screen, stats)` - initializes the class, the arguments passed object of the screen - `screen` and an object of the class `Stats` - `stats`.
2. `Image_score(self)` - Renders a picture of the inscription of the current account
3. `image_high_score(self)` - Renders a picture of the inscription of the record score
4. `show_score(self)` - display pictures on screen
5. `image_ships(self)` - loads an array of pictures to draw lives 

### class Alien
Alien class
#### Fields
Inherits the fields of the `pygame.sprite` class and has fields:
1. `self.screen` - stores reference to the screen object
2. `self.type` - type of alien (1 - purple, 2 - green, 3 - red)
3. `self.image` - stores the picture of the alien.
4. `self.rect` - stores the rectangle of the alien`s picture and its coordinates.
5. `self.x` - stores real coordinate value (needed for smooth movement)
6. `self.y` - stores the real coordinate value (it's necessary for smooth movement)
#### Methods
Inherits methods of the pygame.Sprite class and has:
1. `__init__(self, screen, al_type=1)` - initializes class, arguments passed to the screen object - `screen` and alien type (1 - purple, 2 - green, 3 - red)
2. `update(self)` - updates alien position (overritted)
3. `draw(self)` - draws alien on screen

### class Interface()
The class in charge of the game interface
#### Fields
1. `self.screen` - stores reference to the screen object
2. `self.screen_rect` - stores rectangle interpreting the screen and its coordinates
3. `self.text_color` - text color.
4. `self.active_color` - text color on cursor hovering
5. `self.font` - font (medium)
6. `self.font2` - font 2 (large)
7. `self.bg_color` - interface background color
8. `self.text` - interface text and buttons
9. `self.what_now` - name of the current event of the interface
10. `self.rects_now` - dictionary of rectangles and their encoding keys
11. `self.buttons` - dictionary of active buttons
#### Methods
1. `__init__(self, screen)` - initializes the class, the arguments passed to the screen object - screen
2. `interface_image(self, key, pos_x, pos_y, text_color, font='small', lvl='')` - Renders a picture of the caption of the interface object, arguments: `key` - key of the inscription in the dictionary `self.text`, `pos_x` and `pos_y` - coordinates, `text_color` - text color, `font` - font (`'small'` - medium, `'big'` - large), `lvl` - level number, used only for rendering the title level
3. `next_lvl(self, lvl)` - creates a screen saver to a new level, the argument - `lvl` - number of level
4. `menu(self)` - game menu
5. `win(self)` - Creates a splash screen of victory 
6. `lose(self)` - creates a loser screensaver
7. `check_mouse(self, pos)` - checks if the cursor is on any button, if so, it returns the button key in the dictionary `self.buttons` and changes the corresponding value in the dictionary to 1, otherwise it returns `None`.





