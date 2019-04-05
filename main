import pygame

# Pygame startup
win_width = 800
win_height = 600
pygame.init()
screen = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 16)
done = False

while not done:
    # Update
    dt = clock.tick() / 1000.0

    # Input
    evt = pygame.event.poll()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True

    # Drawing
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
