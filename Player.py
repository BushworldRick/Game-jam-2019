class Player:
    def __init__(self,screenwidth, img):
        player_x =  screenwidth // 2
        x_direction
        y_direction
        player_y = 500
        player_speed = 150
        bullets = []        # bullet class objects
        player_hitbox = depends on sprite
        





    def update(self,dt):
        self.dt = dt



    def input(self,keys):
        # Moving player_ship
        x_direction = 0
        y_direction = 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_direction -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_direction += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            y_direction -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y_direction += 1
        self.player_x += self.player_speed * self.dt * x_direction  # may need t go to input secton
        self.player_y += self.player_speed * self.dt * y_direction
