from train_neat import *

def run_best(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        config_file)
    
    with open("Results/winner.pkl", "rb") as f:
        genome = pickle.load(f)
    
    genomes = [(1, genome)]
    eval_genomes(genomes, config, False)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    
    run_best(config_path)
