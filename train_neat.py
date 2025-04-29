from dinosaur import Dinosaur
from background import *
from obstacle import *

import pygame
import sys
import random
import math
import neat
import pickle

# INIT
pygame.init()
FONT = pygame.font.Font(None, 20)
pygame.key.set_repeat(500, 100)

# GLOBAL VAR
WIDTH, HEIGHT = 1100, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino NEAT")
GEN = 0

def get_score():
    global score, speed
    score += 1
    if score % 100 == 0:
        # Capped due to physics
        if speed < 51:
            speed += 1
    
    text = FONT.render(f"score: {str(score)}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    SCREEN.blit(text, text_rect)
    
def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx**2 + dy**2)

def render_bg(cloud, track):
    cloud.draw(SCREEN)
    cloud.update(speed)
    track.draw(SCREEN)
    track.update(speed)

def stats():
    global GEN, dinosaurs, speed
    
    text_1 = FONT.render(f"Generation: {str(GEN)}", True, (255, 255, 255))
    text_2 = FONT.render(f"Dinosaurs Alive: {str(len(dinosaurs))}", True, (255, 255, 255))
    text_3 = FONT.render(f"Game Speed: {str(speed)}", True, (255, 255, 255))

    SCREEN.blit(text_1, (50, 450))
    SCREEN.blit(text_2, (50, 480))
    SCREEN.blit(text_3, (50, 510))

def eval_genomes(genomes, config, training=True):
    global GEN, score, speed, dinosaurs, ge
    clock = pygame.time.Clock()
    score = 0
    speed = 20
    
    dinosaurs = []
    obstacles = []
    ge = []
    nets = []
    
    cloud = Cloud()
    track = Track()
    
    for genome_id, genome in genomes:
        dinosaurs.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0
        
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
        
        # End generation training
        if len(dinosaurs) == 0 or ge[0].fitness > 500 and training:
            GEN += 1
            break
        
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
                    ge[dinosaurs.index(dino)].fitness -= 1
                    dinosaurs.pop(i)
                    ge.pop(i)
                    nets.pop(i)
        
        for i, dino in enumerate(dinosaurs):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                match dino.debug:
                    case True:
                        dino.debug = False
                    case False:
                        dino.debug = True
                
            output = nets[i].activate((distance(dino.rect, obstacle.rect), dino.rect.y , obstacle.rect.width, obstacle.rect.height, obstacle.rect.y, speed))
            
            # Jump output
            if output[0] > 0.5 and dino.rect.y == dino.Y_POS:
                dino.ducking = False
                dino.running = False
                dino.jumping = True

            # Duck output
            elif output[1] > 0.5 and dino.rect.y == dino.Y_POS:
                dino.ducking = True
                dino.running = False
                dino.jumping = False
            
            # Unduck output
            elif output[1] < 0.5 and dino.rect.y == 340:
                dino.ducking = False
                dino.running = True
                dino.jumping = False
            
            # Add fitness after successful pass
            if not obstacle.passed and obstacle.rect.x < dino.rect.x:
                obstacle.passed = True
                for genome in ge:
                    genome.fitness += 1

            ge[i].fitness += 0.01
            text_4 = FONT.render(f'Fitness: {ge[i].fitness:.2f}', True, (255, 255, 255))
        
        SCREEN.blit(text_4, (50, 540))
        
        stats()
        get_score()
        render_bg(cloud, track)
        clock.tick(30)
        pygame.display.update()

def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_file)

    p = neat.Population(config)
    
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, 100)

    print('\nBest genome:\n{!s}'.format(winner))
    
    with open("Results/winner.pkl", "wb") as f:
        pickle.dump(winner, f)            
        
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    
    run(config_path)