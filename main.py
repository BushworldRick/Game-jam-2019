from map import *

# Pygame startup
clock = pygame.time.Clock()
done = False

my_map = Map()

while not done:
    # Update
    dt = clock.tick() / 1000.0
    my_map.update(dt)

    # Input
    evt = pygame.event.poll()
    my_map.input(evt)
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True

    # Drawing
    win.fill((0, 0, 0))
    my_map.draw(win)
    pygame.display.flip()

pygame.quit()
