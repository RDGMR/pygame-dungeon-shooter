from random import randint
from pathlib import Path
import pygame
import math

class Enemy_manager:
    def __init__(self, target, bullets):
        self.screen = target.screen
        self.target = target
        self.bullets = bullets
        self.enemies = []

        self.sprites = []
        for sprite in Path("enemy/run").glob("*.png"):
            for num in range(10):
                image = pygame.image.load(f"enemy/run/{sprite.name}").convert()
                image.set_colorkey((255, 0, 255))
                self.sprites.append(image)

        for num in range(10):
            self.enemies.append(self.Enemy(self.screen))

    def spawn(self):
        self.enemies.append(self.Enemy(self.screen))

    def update(self):
        for enemy in self.enemies:
            enemy.update(self.target)

            for bullet in self.bullets:
                if enemy.rect.colliderect((bullet.x, bullet.y, 5, 5)):
                    enemy.hp -= 1
                    self.bullets.remove(bullet)
                    # break

            if enemy.current_sprite >= len(self.sprites):
                enemy.current_sprite = 0

            if enemy.hp <= 0:
                self.enemies.remove(enemy)

    def render(self):
        for enemy in self.enemies:
            enemy.render(self.sprites[enemy.current_sprite])

    class Enemy:
        def __init__(self, screen):
            self.screen = screen
            self.current_sprite = 0

            self.x = randint(0, 426)
            self.y = randint(0, 240)
            self.rect = pygame.Rect(self.x, self.y, 16, 16)
            self.vel = .5
            self.hp = 50

        def update(self, target):
            target_x = target.rect.x
            target_y = target.rect.y
            distance_x = target_x - self.x
            distance_y = target_y - self.y
            angle = math.atan2(distance_y, distance_x)
            vel_x = self.vel * math.cos(angle)
            vel_y = self.vel * math.sin(angle)
            self.x += vel_x
            self.y += vel_y
            self.rect.x = self.x
            self.rect.y = self.y

            self.current_sprite += 1
            
        def render(self, image):
            pygame.draw.rect(self.screen, "YELLOW", self.rect)
            self.screen.blit(image, self.rect)
