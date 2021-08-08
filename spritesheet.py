import pygame
from pygame import sprite

class Spritesheet:
    def __init__(self, file):
        self.file = file
        self.sprite_sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((255, 0, 255))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return sprite

    def load_sprites(self):
        sprites = [None]
        for y in range(self.sprite_sheet.get_rect().height // 16):
            for x in range(self.sprite_sheet.get_rect().width // 16):
                sprites.append(self.get_sprite(x * 16, y * 16, 16, 16))
        return sprites