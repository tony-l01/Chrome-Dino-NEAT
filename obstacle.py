import pygame
import os
import random

# OBS IMG
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
           pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
           pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
           pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
           pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
           pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = 1100
        self.passed = False
        self.debug = False
                
    def update(self, speed, obstacle):
        self.rect.x -= speed
        if self.rect.x < -self.rect.width:
            obstacle.pop()
            
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
            
class SmallCactus(Obstacle):
    def __init__(self, img, type):
        super().__init__(img, type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, img, type):
        super().__init__(img, type)
        self.rect.y = 300
        
class Bird(Obstacle):
    def __init__(self, image, type):
        super().__init__(image, type)
        self.rect.y = random.randint(200, 260)
        self.step_index = 0
        
    def draw(self, screen):
        if self.step_index >= 9:
            self.step_index = 0
        screen.blit(self.image[self.step_index // 5], self.rect)        
        self.step_index += 1