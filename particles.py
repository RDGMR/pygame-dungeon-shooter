from random import randint
import pygame

class Particle_manager:
    def __init__(self, screen):
        self.screen = screen
        self.particles = []

    def add(self, pos):
        self.particles.append(self.Particle(pos))

    def update(self):
        for particle in self.particles:
            if particle.radius <= 0:
                self.particles.remove(particle)
            particle.update()

    def render(self):
        for particle in self.particles:
            pygame.draw.circle(self.screen, "WHITE", (particle.x, particle.y), int(particle.radius))

    class Particle:
        def __init__(self, pos):
            self.x, self.y = pos
            self.x_vel = randint(0, 20) / 10 - 1
            self.y_vel = randint(-4, -2)
            self.radius = randint(4, 6)

        def update(self):
            self.x += self.x_vel
            self.y += self.y_vel
            self.y_vel += 0.1
            self.radius -= 0.5
