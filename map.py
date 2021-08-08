import pygame
from spritesheet import Spritesheet
import json

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.Spritesheet = Spritesheet("spritesheet.png")
        self.sprites = self.Spritesheet.load_sprites()
        with open("map.json") as mapJson:
            self.map = json.load(mapJson)
            mapJson.close()
        self.tiles = []
        self.solid_tiles = [8, 9, 10, 15, 16, 17, 22, 23, 24, 49, 50, 56, 57, 63, 64]
        for layer in self.map["layers"]:
            a, b = 0, 0
            for sprite in layer["data"]:
                if a >= 192:
                    a = 0
                    b += 16
                if sprite != 0:
                    x = a + (self.screen.get_rect().width / 2) - (192 / 2)
                    y = b + (self.screen.get_rect().height / 2) - (192 / 2) - (12 / 2)
                    self.tiles.append(self.Tile(self.sprites[sprite], sprite, x, y))
                a += 16
        for tile in self.tiles:
            if tile.id - 1 in self.solid_tiles:
                tile.solid = True

    def render(self):
        for tile in self.tiles:
            self.screen.blit(tile.image, tile.rect)

    class Tile:
        def __init__(self, image, id, x, y):
            self.image = image
            self.id = id
            self.solid = False
            self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
