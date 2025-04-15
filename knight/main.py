import pygame
from player import Player
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock() 


my_player = Player(300, 300)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.animation_state == "Walk":
        my_player.change_animation("Walk")
    elif my_player.animation_state == "Idle":
        my_player.change_animation("Idle")
    
    screen.fill(WHITE)
    my_player.update(screen)
    pygame.display.update()
    clock.tick(FPS)