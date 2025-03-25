# import os
# files_names_list = os.listdir('./knight')
# for file_name in files_names_list:
#     os.rename(f'./knight/{file_name}',
#                 f'./knight/{file_name}'.replace(" ","").replace("(", "").replace(")", "")
#                 )



import pygame
pygame.init()


WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_image = pygame.image.load("./knight/Idle1.png")
player_image = pygame.transform.scale_by(player_image,  0.5)
player_rect = player_image.get_rect(topleft=(100,10))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.blit(player_image, player_rect)
    pygame.draw.rect(screen, "purple", player_rect, 2)
    pygame.display.update()
