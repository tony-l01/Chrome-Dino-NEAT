import pygame
import os
import random

# DINO IMG
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]

DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5
    
    def __init__(self, img=RUNNING[0]):
        self.image = img
        self.running = True
        self.jumping = False
        self.ducking = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.step_index = 0
        self.hitbox = (255, 255, 255)
        self.debug = False
        
    def update(self):
        if self.running:
            self.run()
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.step_index >= 10:
            self.step_index = 0
    
    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
    
    def jump(self):
        self.image = JUMPING
        if self.jumping:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.jumping = False
            self.running = True
            self.jump_vel = self.JUMP_VEL
    
    def duck(self):
        self.image = DUCKING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS + 30
        self.step_index += 1
    
    def draw(self, screen, obstacles):
        if self.debug:
            pygame.draw.rect(screen, self.hitbox, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)

            for obstacle in obstacles:
                pygame.draw.line(screen, (255, 0, 0), (self.rect.x + 54, self.rect.y + 12), obstacle.rect.topleft, 2)
                pygame.draw.line(screen, (0, 255, 0), (self.rect.x + 54, self.rect.y + 12), obstacle.rect.topright, 2)
                pygame.draw.line(screen, (0, 0, 255), (self.rect.x + 54, self.rect.y + 12), obstacle.rect.midbottom, 2)
                
                pygame.draw.rect(screen, (255, 255, 255), (obstacle.rect.x, obstacle.rect.y, obstacle.rect.width, obstacle.rect.height), 2)
                
        screen.blit(self.image, (self.rect.x, self.rect.y))        
