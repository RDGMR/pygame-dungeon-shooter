import pygame
import math

class Bullet_manager:
    def __init__(self, Player, enemies, particle_manager, tiles):
        self.Player = Player
        self.enemies = enemies
        self.particle_manager = particle_manager
        self.tiles = tiles
        self.bullets = []

    def update(self):
        if self.Player.shooting:
            self.spawn()

        for bullet in self.bullets:
            bullet.x += bullet.vel_x
            bullet.y += bullet.vel_y
            bullet.rect.x = bullet.x
            bullet.rect.y = bullet.y
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy):
                    enemy.hp -= 1
                    bullet.hp -= 1
                    self.particle_manager.explode((bullet.x, bullet.y))
            for tile in self.tiles:
                if bullet.rect.colliderect(tile) and tile.solid:
                    bullet.hp = 0
                    self.particle_manager.explode((bullet.x, bullet.y))
            if bullet.hp <= 0 or bullet.x < 0 - 5 or bullet.x > 426 or bullet.y < 0 - 5 or bullet.y > 240:
                self.bullets.remove(bullet)
    
    def render(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.Player.screen, "BLUE", bullet.rect)

    def spawn(self):
        self.bullets.append(self.Bullet(self.Player.rect.center))

    class Bullet:
        def __init__(self, origin):
            self.x = origin[0]
            self.y = origin[1]
            self.rect = pygame.Rect(self.x, self.y, 5, 5)
            self.hp = 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance_x = mouse_x - self.x
            distance_y = mouse_y - self.y
            angle = math.atan2(distance_y, distance_x)
            vel = 1.5

            self.vel_x = vel * math.cos(angle)
            self.vel_y = vel * math.sin(angle)
