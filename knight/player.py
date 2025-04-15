from pygame.sprite import Sprite
import pygame
import os
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_types = os.listdir("assets")
        self.all_images = {}
        for animation in self.animation_types:
            self.all_images[animation] = []
            for image in os.listdir(f"assets/{animation}"):
                img = pygame.image.load(f"assets/{animation}/{image}")
                img = pygame.transform.scale_by(img, 0.4)
                self.all_images[animation].append(img)
        self.current_animation = "Idle"
        self.current_frame = 0
        self.image = self.all_images[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_state = "Idle"
        self.direction = 1
        self.flip = False

    def update(self, screen):
        screen.blit(
            pygame.transform.flip(self.image, self.flip, False) 
            , self.rect)
        self.image = self.all_images[self.current_animation][self.current_frame]
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > 100:
            self.last_animation_time = current_time
            self.current_frame += 1
        if self.current_frame >= len(self.all_images[self.current_animation]):
            self.current_frame = 0

        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.animation_state = "Walk" 
            self.flip = True  
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.animation_state = "Walk"
            self.flip = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.animation_state  = "Idle"
        self.rect.x += dx
        self.rect.y += dy

    def change_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.current_frame = 0
            self.last_animation_time = pygame.time.get_ticks()
