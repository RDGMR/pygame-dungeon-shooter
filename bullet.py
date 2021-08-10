import pygame
import math

class Bullet:
    def __init__(self, Player):
        self.Player = Player
        self.screen = self.Player.screen
        self.x = self.Player.rect.x
        self.y = self.Player.rect.y

        mouse_x, mouse_y = pygame.mouse.get_pos()
        distance_x = mouse_x - self.Player.rect.x
        distance_y = mouse_y - self.Player.rect.y
        angle = math.atan2(distance_y, distance_x)
        vel = 1.5
        self.vel_x = vel * math.cos(angle)
        self.vel_y = vel * math.sin(angle)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def render(self):
        pygame.draw.rect(self.screen, "BLUE", (self.x, self.y, 5, 5))
