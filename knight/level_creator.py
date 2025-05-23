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
COLS = 150
ROWS = HEIGHT // TILE_SIZE

selected_btn_index = 0

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
for img in tile_images:
    buttons_list.append(
        Button(
            WIDTH + 20 + c * 80,
            10 + r  * 80,
            img,
            "tile"
        )
    )
    c +=1
    if c == 5:
        r += 1
        c = 0

level = 1
world_data = []

for i in range(ROWS):
    temp = [-1] * COLS
    world_data.append(temp)

def draw_world(level):
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:
                screen.blit(buttons_list[world_data[i][j]].image, (j * TILE_SIZE, i * TILE_SIZE))


def draw_lines():
    for i in range(COLS + 1):
        pygame.draw.line(screen, "brown", (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT))
    for j in range(ROWS + 1):
        pygame.draw.line(screen, "brown", ( 0, j * TILE_SIZE), (WIDTH, j * TILE_SIZE))

screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT+ LOWER_MARGIN))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    
    screen.fill((255,255,255))
    draw_lines()
    pygame.draw.rect(screen, "lightblue", (WIDTH, 0, SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
    pygame.draw.rect(screen, "lightblue", (0, HEIGHT, SIDE_MARGIN + WIDTH, LOWER_MARGIN))
    for i,btn in enumerate(buttons_list):
        if btn.update(screen):
            selected_btn_index = i
    mouse_pos = pygame.mouse.get_pos()
    r = mouse_pos[1]//TILE_SIZE
    c = mouse_pos[0]//TILE_SIZE
    
    if pygame.mouse.get_pressed()[0] and mouse_pos[0] < WIDTH and mouse_pos[1] < HEIGHT:
        world_data[r][c] = selected_btn_index
    draw_world(level)
    pygame.draw.rect(screen, "red", buttons_list[selected_btn_index].rect, 3)
    pygame.display.update()
    clock.tick(FPS)