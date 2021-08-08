import pygame
from pygame.locals import *
from player import Player
from bullet import Bullet
from map import Map

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

size = width, height = 426, 240 # sei la man
screen = pygame.display.set_mode(size)
running = True
bullets = []
Map = Map(screen)
Player = Player(screen, Map)

rectfodase = pygame.Rect(10, 10, 20, 10)

# Game loop.
while running:
    screen.fill("BLACK")

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_a:
                if not Player.Hit.active:
                    Player.damage()
            elif event.key == pygame.K_f:
                bullets.append(Bullet(Player))

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

        elif event.type == KEYUP:
            if event.key == pygame.K_RIGHT:
                Player.right = False
            elif event.key == pygame.K_LEFT:
                Player.left = False
            elif event.key == pygame.K_UP:
                Player.up = False
            elif event.key == pygame.K_DOWN:
                Player.down = False

    # Update.
    Player.update()
    for bullet in bullets:
        bullet.update()
        # this is ugly
        if bullet.x < 0 - 5 or bullet.y < 0 - 5 or bullet.x > width or bullet.y > height: # hardcoded
            bullets.remove(bullet)
 
    # Draw.
    Map.render()
    Player.render()
    for bullet in bullets:
        bullet.render()
    
    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()