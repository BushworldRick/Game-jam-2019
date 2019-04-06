import pygame
from Player import *
from config import *
from random import randint
from Enemy import *
from bullet import *
from copy import deepcopy

NUM_ENEMIES = 5

class Map:
    def __init__(self):
        self.Player = Player((800,600), SHIP)
        self.mPreset_enemies = []
        for i in range(NUM_ENEMIES):
            spwn_x = randint(0, win_width)
            self.mPreset_enemies.append(Enemy(spwn_x, -50))
        self.mEnemies = [deepcopy(self.mPreset_enemies[0])]
        self.Enemy_delay = 0.5
        self.Enemy_index = 1
        self.bullet_list = []
        self.mDel_enemies = False
        self.mBoss_phase = False
        self.mAdd_phase = True

    def update(self, dt):

        if self.Enemy_index < NUM_ENEMIES:
            self.Enemy_delay -= dt
            if self.Enemy_delay < 0:
                self.mEnemies.append(deepcopy(self.mPreset_enemies[self.Enemy_index]))
                self.Enemy_index += 1
                self.Enemy_delay = 0.5

        self.Player.update(dt)

        print(len(self.mEnemies), "number of enemies")
        if len(self.mEnemies) > 0:
            for e in self.mEnemies:
                e.update(dt)
                print(e.mPos[1])
                if e.mPos[1] > 810:
                    self.mEnemies.remove(e)

    def reset(self):
        self.Enemy_index = 1
        self.mBoss_phase = False
        self.mAdd_phase = True
        self.Enemy_delay = 0.5
        self.mDel_enemies = False

    def input(self, evt, keys):
        self.Player.input(evt,keys)
        print(len(self.mEnemies))
        print(self.Enemy_index, "enemy index")
        if len(self.mEnemies) == 0:
            self.mEnemies = [deepcopy(self.mPreset_enemies[0])]
            return True,False
        return self.mBoss_phase, self.mAdd_phase

    def draw(self, win):

        self.Player.draw(win)

        if len(self.mEnemies) > 0:
            for e in self.mEnemies:
                e.draw(win)
