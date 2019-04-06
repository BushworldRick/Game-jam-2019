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
ship_directions = {"left": 1, "right": 3, "up": 0, "down": 2, "frameheight": 100, "framewidth": 100, "frames_wide": 8}

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
