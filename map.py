from Enemy import *
from random import randint

max_stars = 220
stars = []
for i in range(max_stars):
    x,y = randint(0, 800), randint(0, 600)
    rad,spd = randint(2, 5), randint(100, 150)
    star = [x, y, rad, spd]
    stars.append(star)

class Map:
    def __init__(self):
        self.mStars = stars
        self.Enemy = Enemy(400, 300)

    def update(self, dt):

        # STAR UPDATE
        for star in self.mStars:
            star[1] += star[3] * dt
            if star[1] > star[2] + 600:
                star[1] = -star[2]

        # ENEMY UPDATE
        self.Enemy.update(dt)

    def input(self, evt):
        pass

    def draw(self, win):

        # STAR DRAW
        for star in self.mStars:
            x = star[0]
            y = star[1]
            pygame.draw.circle(win, (220, 220, 220), (int(x), int(y)), star[2],)

        self.Enemy.draw(win)