import pygame
from pathlib import Path

class Player:
    def __init__(self, screen, Map):
        self.Hit = self.Hit()
        self.screen = screen
        self.tiles = Map.tiles
        self.last_x = 1
        self.last_y = 1
        self.x = 0
        self.y = 0
        self.current_sprite = 0
        self.sprites = []
        for sprite in Path("player/idle").glob("*.png"):
            for num in range(10):
                self.sprites.append(pygame.image.load(f"player/idle/{sprite.name}"))
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.height = self.rect.width

        self.rect.center = self.screen.get_rect().center
        self.run_sprites = []
        for sprite in Path("player/run").glob("*.png"):
            for num in range(10):
                self.run_sprites.append(pygame.image.load(f"player/run/{sprite.name}"))
        self.flipped = False
        self.can_control = True
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.vel = 1
        # self.running = False
        self.run_counter = 0

    class Hit:
        def __init__(self):
            self.active = False
            self.vel = .5
            self.right = False
            self.left = False
            self.up = False
            self.down = False
            self.counter = 0
            self.sprites = []
            for sprite in Path("player/hit").glob("*.png"):
                for num in range(50):
                    self.sprites.append(pygame.image.load(f"player/hit/{sprite.name}")) 

    def collide_test(self, rect, tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile) and tile.solid:
                collisions.append(tile)
        return collisions

    def move(self, rect, movement):
        print(movement)
        rect.x += movement[0]
        collisions = self.collide_test(rect, self.tiles)
        for tile in collisions:
            if movement[0] > 0:
                rect.right = tile.rect.left
            elif movement[0] < 0:
                rect.left = tile.rect.right
        rect.y += movement[1]
        collisions = self.collide_test(rect, self.tiles)
        for tile in collisions:
            if movement[1] > 0:
                rect.bottom = tile.rect.top
            elif movement[1] < 0:
                rect.top = tile.rect.bottom

        return rect

    def update(self):
        if self.Hit.active:
            self.Hit.counter += 1
            movement = [0, 0]

            if self.Hit.right:
                movement[0] -= self.Hit.vel
                # self.x -= self.Hit.vel
            elif self.Hit.left:
                movement[0] += self.Hit.vel
                # self.x += self.Hit.vel

            if self.Hit.up:
                movement[1] += self.Hit.vel
                # self.y += self.Hit.vel
            elif self.Hit.down:
                movement[1] -= self.Hit.vel
                # self.y -= self.Hit.vel

            self.rect = self.move(self.rect, movement)
        
            if self.Hit.counter >= len(self.Hit.sprites):
                self.Hit.counter = 0
                self.Hit.active = False
                self.can_control = True

                self.Hit.right = False
                self.Hit.left = False
                self.Hit.up = False
                self.Hit.down = False

            self.image = self.Hit.sprites[self.Hit.counter]

        else:    
            movement = [0, 0]
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0

            if self.can_control:
                if self.right:
                    movement[0] += self.vel
                if self.left:
                    movement[0] -= self.vel
                if self.up:
                    movement[1] -= self.vel
                if self.down:
                    movement[1] += self.vel

                self.rect = self.move(self.rect, movement)

            if self.right or self.left or self.up or self.down:
                # self.running = True
                self.image = self.run_sprites[self.run_counter]
                self.run_counter += 1
                if self.run_counter >= len(self.run_sprites):
                    self.run_counter = 0
            else:
                # self.running = False
                self.image = self.sprites[self.current_sprite]

    def damage(self):
        self.Hit.active = True
        self.can_control = False

        if self.right:
            self.Hit.right = True
        elif self.left:
            self.Hit.left = True

        if self.up:
            self.Hit.up = True
        elif self.down:
            self.Hit.down = True

    def render(self):
        pygame.draw.rect(self.screen, "RED", (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        self.screen.blit(self.image, (self.rect.x, self.rect.y - 12))
