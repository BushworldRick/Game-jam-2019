from map import *
from boss import *

# Pygame startup
clock = pygame.time.Clock()
done = False

my_map = Map()
boss = Boss(win_width/2, -300, my_map)

boss_phase = False
add_phase = True

max_stars = 200
stars = []
for i in range(max_stars):
    x,y = randint(0, 800), randint(0, 600)
    rad,spd = randint(2, 5), randint(100, 150)
    star = [x, y, rad, spd]
    stars.append(star)

while not done:
    # Update
    dt = clock.tick() / 1000.0
    if add_phase:
        my_map.update(dt)
    elif boss_phase:
        boss.update(dt)
    for star in stars:
        star[1] += star[3] * dt
        if star[1] > star[2] + 600:
            star[1] = -star[2]

    # Input
    evt = pygame.event.poll()
    keys = pygame.key.get_pressed()
    if add_phase:
        list2 = my_map.input(evt, keys)
        boss_phase = list2[0]
        add_phase = list2[1]
        if add_phase == False:
            my_map.reset()
            boss_phase = True
            add_phase = False
    elif boss_phase:
        list = boss.input(evt, keys)
        boss_phase = list[0]
        add_phase = list[1]
        if boss_phase == False:
            boss.reset()
            boss_phase = False
            add_phase = True

    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True

    # Drawing
    win.fill((0, 0, 0))
    for star in stars:
        x = star[0]
        y = star[1]
        pygame.draw.circle(win, (220, 220, 220), (int(x), int(y)), star[2], )
    if add_phase:
        my_map.draw(win)
    elif boss_phase:
        boss.draw(win)
    pygame.display.flip()

pygame.quit()
