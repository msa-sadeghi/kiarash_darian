# import os
# files_names_list = os.listdir('./knight')
# for file_name in files_names_list:
#     os.rename(f'./knight/{file_name}',
#                 f'./knight/{file_name}'.replace(" ","").replace("(", "").replace(")", "")
#                 )



import pygame
from player import Player
pygame.init()
my_player = Player(100, 200)
WIDTH = 1000
HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
moving_left, moving_right, moving_up, moving_down = (False, False, False, False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

   
    screen.fill((120, 230,240)) 
    my_player.move()  
    my_player.draw(screen)
    
    pygame.display.update()
    clock.tick(FPS)
