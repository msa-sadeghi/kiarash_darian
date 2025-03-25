import pygame
class Player:
    def __init__(self, x,y):
        self.image = pygame.image.load("./knight/Attack1.png")
        self.rect = self.image.get_rect(center = (x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)