import pygame
class Player:
    def __init__(self, x,y):
        self.image = pygame.image.load("./knight/Attack1.png")
        self.image = pygame.transform.scale_by(self.image, 0.3)
        self.rect = self.image.get_rect(center = (x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        
        self.rect.x += dx
        self.rect.y += dy

    def animation(self):
        pass