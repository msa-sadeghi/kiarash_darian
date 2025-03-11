import pygame
pygame.init()


WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.line(screen, (255, 0,0) , (100, 200), (100, 400))
    pygame.draw.rect(screen, "green", (300, 300, 150, 150))
    pygame.draw.rect(screen, "green", (50, 360, 150, 150), 4)
    pygame.draw.ellipse(screen, "darkblue", (150, 460, 150, 150), 4)
    pygame.display.update()
