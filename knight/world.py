import pygame
from bomb import Bomb
from energy import Energy
from box import Box
class World:
    def __init__(self, world_data, images, scroll, TILE_SIZE,bomb_group, energy_group, box_group):
        self.obstacle= []
        self.keys = []
        self.boxes = []
        self.bomb = []
        self.energy = []
        print(world_data)
        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] == 0:
                    
                    bomb = Bomb(images[world_data[i][j]], j * TILE_SIZE - scroll, i * TILE_SIZE, bomb_group)
                    self.bomb.append(bomb)
                elif world_data[i][j] == 1:
                    energy = Energy(images[world_data[i][j]], j * TILE_SIZE - scroll, i * TILE_SIZE, energy_group)
                    self.energy.append(energy)
                    
                elif world_data[i][j] in (2,3,4,5,7,8):
                    pass
                    # TODO create key and append it to the list
                elif world_data[i][j] in (6,21):
                    pass
                elif world_data[i][j] in (13,14,15,16,31,32,33,34,35):
                    box = Box(images[world_data[i][j]], j * TILE_SIZE - scroll, i * TILE_SIZE, box_group)
                    self.boxes.append(box)