import pygame
import math

win_width = 800
win_height = 600
pygame.init()
win = pygame.display.set_mode((win_width, win_height))

# Player Sprite
SHIP = pygame.image.load("Sprites/spritesheetSpaceship.png")
img_w = SHIP.get_width()
img_h = SHIP.get_height()
SHIP = pygame.transform.scale(SHIP, (img_w, img_h)).convert()
SHIP = pygame.transform.rotate(SHIP, math.pi / 2)
SHIP.set_colorkey((0, 0, 0))
ship_directions = {"frameheight": 100, "framewidth": 65}

# Enemy Sprite
ENEMY = pygame.image.load("Sprites/enemy_sprites.PNG")
img_w = ENEMY.get_width()
img_h = ENEMY.get_height()
ENEMY = pygame.transform.scale(ENEMY, (img_w, img_h)).convert()
ENEMY = pygame.transform.rotate(ENEMY, math.pi)
ENEMY.set_colorkey((0, 0, 0))
enemy_directions = {"left": 1, "right": 3, "up": 0, "down": 2, "frameheight": 64, "framewidth": 64, "frames_wide": 8,
                     "x_offset": 15, "y_offset": 5}

# Boss Sprite
BOSS = pygame.image.load("Sprites/PossibleBoss1.png")
img_w = BOSS.get_width()
img_h = BOSS.get_height()
BOSS = pygame.transform.scale(BOSS, (img_w, img_h)).convert()
BOSS.set_colorkey((255, 0, 255))
BOSS.set_alpha(255)
boss_directions = {"left": 1, "right": 3, "up": 0, "down": 2, "frameheight": 64, "framewidth": 64, "frames_wide": 8,
                     "x_offset": 15, "y_offset": 5}

# Terminal Image
TERM = pygame.image.load("Sprites/futuristicScreen.jpg")
img_w = TERM.get_width()
img_h = TERM.get_height()
width_scalar = .94
height_scalar = 1.25
img_w = int(img_w * width_scalar)
img_h = int(img_h * height_scalar)
TERM = pygame.transform.scale(TERM, (img_w, img_h))

# dictionary of the keys
Keys = {"a":(0,0), "b":(0, 1), "c":(0, 2), "d":(0, 3), "e":(0, 4), "f":(0,5), "g":(0,6), "h":(1,0),"i":(1,1),
"j":(1,2),"k":(1,3),"l":(1,4), "m":(1,5),"n":(1,6),"o":(2,0),"p":(2,1),"q":(2,2),"r":(2,3),"s":(2,4),"t":(2,5),"u":(2,6),
"v":(3,0),"w":(3,1),"x":(3,2),"y":(3,3),"z":(3,4)}
