from particles import Particle_manager
import pygame
import math

class Bullet_manager:
    def __init__(self, Player, enemies, particle_manager):
        self.Player = Player
        self.enemies = enemies
        self.particle_manager = particle_manager
        self.bullets = []

    def update(self):
        if self.Player.shooting:
            self.spawn()

        for bullet in self.bullets:
            self.particle_manager.add((bullet.x, bullet.y))
            bullet.x += bullet.vel_x
            bullet.y += bullet.vel_y
            for enemy in self.enemies:
                if pygame.Rect(bullet.x, bullet.y, 5, 5).colliderect(enemy):
                    enemy.hp -= 1
                    bullet.hp -= 1
            if bullet.hp <= 0 or bullet.x < 0 - 5 or bullet.x > 426 or bullet.y < 0 - 5 or bullet.y > 240:
                self.bullets.remove(bullet)
    
    def render(self):
        for bullet in self.bullets:
            pygame.draw.rect(self.Player.screen, "BLUE", (bullet.x, bullet.y, 5, 5))

    def spawn(self):
        self.bullets.append(self.Bullet(self.Player.rect))

    class Bullet:
        def __init__(self, origin):
            self.x = origin.x
            self.y = origin.y
            self.hp = 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance_x = mouse_x - origin.x
            distance_y = mouse_y - origin.y
            angle = math.atan2(distance_y, distance_x)
            vel = 1.5

            self.vel_x = vel * math.cos(angle)
            self.vel_y = vel * math.sin(angle)
