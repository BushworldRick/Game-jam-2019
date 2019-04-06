from map import *
from boss import *
from terminal import *
import random

# Pygame startup
clock = pygame.time.Clock()
done = False

my_map = Map()
boss = Boss(win_width/2, -200, my_map)
term = Terminal()

boss_phase = False
add_phase = True
terminal_phase = False

max_stars = 200
stars = []
for i in range(max_stars):
    x, y = randint(0, 800), randint(0, 600)
    rad, spd = randint(2, 5), randint(100, 150)
    star = [x, y, rad, spd]
    stars.append(star)

while not done:
    # Update
    dt = clock.tick() / 1000.0
    if add_phase:
        my_map.update(dt)
    elif boss_phase:
        boss.update(dt)
    elif terminal_phase:
        term.update(dt)
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
        if not add_phase:
            my_map.reset()
            boss_phase = True
            add_phase = False
    elif boss_phase:
        list = boss.input(evt, keys)
        boss_phase = list[0]
        add_phase = list[1]
        if not boss_phase:
            boss.reset()
            boss_phase = False
            add_phase = True

    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True
        if terminal_phase:
            term.input(evt, keys)
        if evt.key == pygame.K_p and boss_phase is not True:
            terminal_phase = True
            add_phase = False
        if terminal_phase:
            if evt.key == pygame.K_TAB:
                terminal_phase = False
                add_phase = True

    # Drawing
    win.fill((0, 0, 0))
    for star in stars:
        x = star[0]
        y = star[1]
        rgb = random.randint(100, 255)
        pygame.draw.circle(win, (rgb, rgb, rgb), (int(x), int(y)), star[2])

    pcent = my_map.Player.health / my_map.Player.max_health
    color = my_map.hp_bar.get_at((int((my_map.hp_bar.get_width() - 1) * pcent), 0))
    width = 150 * pcent
    outer_width = 153
    pygame.draw.rect(win, (255, 255, 255), (618, 18, outer_width, 15), 2)
    pygame.draw.rect(win, color, (620, 20, width, 12))

    if add_phase:
        my_map.draw(win)
    elif boss_phase:
        boss.draw(win)
    elif terminal_phase:
        term.draw(win)
    pygame.display.flip()

pygame.quit()
