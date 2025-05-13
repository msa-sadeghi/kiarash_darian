import pygame
import os
from button import Button
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
FPS = 60
SIDE_MARGIN = 400
LOWER_MARGIN = 100
TILE_SIZE = 50

object_images = [
    
    pygame.transform.scale(
        pygame.image.load(f"./game_world/Objects/{img}"), (TILE_SIZE, TILE_SIZE)
    ) for img in os.listdir("./game_world/Objects")
]

tile_images = []
for img in os.listdir("./game_world/Tiles"):
    tile_images.append(
        
            pygame.transform.scale(pygame.image.load(f"./game_world/Tiles/{img}"), (TILE_SIZE, TILE_SIZE))
        
    )

buttons_list = []
c = 0
r = 0
for img in object_images:
    buttons_list.append(
        Button(
            WIDTH + 20 + c * 80,
            10 + r  * 80,
            img,
            "object"
        )
    )
    c +=1
    if c == 5:
        r += 1
        c = 0

screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT+ LOWER_MARGIN))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    
    screen.fill((255,255,255))
    pygame.draw.rect(screen, "lightblue", (WIDTH, 0, SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
    pygame.draw.rect(screen, "lightblue", (0, HEIGHT, SIDE_MARGIN + WIDTH, LOWER_MARGIN))
    for btn in buttons_list:
        btn.update(screen)


    pygame.display.update()
    clock.tick(FPS)