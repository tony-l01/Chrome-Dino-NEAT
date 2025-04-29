import pygame
import os
import random

# BG IMG
TRACK = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

class Track:
    def __init__(self):
        self.x = 0
        self.y = 380
        self.image = TRACK
        self.width = self.image.get_width()
    
    def update(self, speed):
        if self.x <= -self.width:
            self.x = 0
        self.x -= speed
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.width + self.x, self.y))

class Cloud:
    def __init__(self):
        self.x = 1100 + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
        
    def update(self, speed):
        self.x -= speed
        if self.x < -self.width:
            self.x = 1100 + random.randint(0, 500)
            self.y = random.randint(50, 100)
            
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))