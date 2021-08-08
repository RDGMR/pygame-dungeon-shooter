import pygame

class Bullet:
    def __init__(self, Player):
        self.Player = Player
        self.screen = self.Player.screen
        self.last_x = self.Player.last_x
        self.last_y = self.Player.last_y
        self.x = self.Player.rect.x
        self.y = self.Player.rect.y
        self.vel = 1.5

    def update(self):
        self.x += self.vel * self.last_x
        self.y += self.vel * self.last_y

    def render(self):
        pygame.draw.rect(self.screen, "BLUE", (self.x, self.y, 5, 5))
