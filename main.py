import pygame
from pygame.locals import *
from player import Player
from bullet import Bullet_manager
from map import Map
from particles import Particle_manager
from enemy import Enemy_manager

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

size = width, height = 426, 240 # sei la man
screen = pygame.display.set_mode(size, pygame.SCALED)
running = True
Map = Map(screen)
Player = Player(screen, Map)
particle_manager = Particle_manager(screen)
enemy_manager = Enemy_manager(Player)
bullet_manager = Bullet_manager(Player, enemy_manager.enemies, particle_manager)

# Game loop.
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                if not Player.Hit.active:
                    Player.damage()

            elif event.key == pygame.K_RIGHT:
                Player.right = True
                Player.last_x = 1
            elif event.key == pygame.K_LEFT:
                Player.left = True
                Player.last_x = -1
            elif event.key == pygame.K_UP:
                Player.up = True
                Player.last_y = -1
            elif event.key == pygame.K_DOWN:
                Player.down = True
                Player.last_y = 1

            elif event.key == pygame.K_e:
                enemy_manager.spawn()

        elif event.type == KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.right = False
            elif event.key == pygame.K_LEFT:
                Player.left = False
            elif event.key == pygame.K_UP:
                Player.up = False
            elif event.key == pygame.K_DOWN:
                Player.down = False

        elif event.type == MOUSEBUTTONDOWN:
            Player.shooting = True
        elif event.type == MOUSEBUTTONUP:
            Player.shooting = False

    Player.update()
    enemy_manager.update()
    bullet_manager.update()
    particle_manager.update()

    # Draw.
    screen.fill("BLACK")
    Map.render()
    Player.render()
    enemy_manager.render()
    bullet_manager.render()
    particle_manager.render()
    
    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()
