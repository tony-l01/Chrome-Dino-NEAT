from dinosaur import Dinosaur
from background import *
from obstacle import *

import pygame
import sys
import random
import math

# INIT
pygame.init()
font = pygame.font.Font(None, 20)

# GLOBAL VAR
WIDTH, HEIGHT = 1100, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def get_score():
    global score, speed
    score += 1
    if score % 100 == 0:
        speed += 1
    
    text_1 = font.render(f"Score: {str(score)}", True, (255, 255, 255))
    text_rect = text_1.get_rect()
    text_rect.center = (1000, 40)
    SCREEN.blit(text_1, text_rect)
        
def distance(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    return math.sqrt(dx**2 + dy**2)

def render_bg(cloud, track):
    cloud.draw(SCREEN)
    cloud.update(speed)
    track.draw(SCREEN)
    track.update(speed)
    
def main():
    global score, speed
    clock = pygame.time.Clock()
    score = 0
    speed = 20
    
    dinosaurs = [Dinosaur()]
    obstacles = []
    cloud = Cloud()
    track = Track()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.fill((45, 45, 45))
        
        for dino in dinosaurs:
            dino.update()
            dino.draw(SCREEN, obstacles)
        
        user_input = pygame.key.get_pressed()
        
        if user_input[pygame.K_UP] and not dino.jumping:
            dino.ducking = False
            dino.running = False
            dino.jumping = True
            
        elif user_input[pygame.K_DOWN] and not dino.jumping:
            dino.ducking = True
            dino.running = False
            dino.jumping = False
            
        elif not (dino.jumping or user_input[pygame.K_DOWN]):
            dino.ducking = False
            dino.running = True
            dino.jumping = False
        
        elif user_input[pygame.K_F1]:
            dino.debug = True
                
        if len(dinosaurs) == 0:
            main()
                    
        if len(obstacles) == 0:
            rand_int = random.randint(0, 2)
            if rand_int == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS, random.randint(0, 2)))
            elif rand_int == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS, random.randint(0, 2)))
            elif rand_int == 2:
                obstacles.append(Bird(BIRD, 0))
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(speed, obstacles)
            for i, dino in enumerate(dinosaurs):
                if dino.rect.colliderect(obstacle.rect):
                    dinosaurs.pop(i)

        get_score()
        render_bg(cloud, track)
        clock.tick(30)
        pygame.display.update()
    
if __name__ == "__main__":
    main()