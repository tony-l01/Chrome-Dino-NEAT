# Chrome-Dino-NEAT

An AI developed to play the Chrome dinosaur game by utilizing the NEAT algorithm in Python.

## How does it work

### AI Inputs

The ai gets 6 inputs from the game.

* Distance between the dino and obstacle
* Dino Y position
* Obstacle width
* Obstacle height
* Obstacle Y position
* Speed

### AI Outputs

Inputs are processed by the neural network. The network's output dictates the dino's action by identifying the highest output values.

### Fitness function

The fitness function is the score of the dino.
It's calculated using the following rules:

* +1 if the dino successfully passed the obstacle
* -1 if the dino collide with the obstacle
* +0.01 for every frame the dino is alive
* stop the game if all the dino dies

## Getting Started

### Installation

1. Clone the repo
   ```
   git clone https://github.com/DocusDukus/Chrome-Dino-NEAT.git
   ```

2. Install the requirements
   ```
   pip install -r requirements.txt
   ```
## Running the code

There are three executable files: `run_game.py`, `run_neat.py`, `train_neat.py`

### Playing the game

Play the game by entering the command in the terminal

    python run_game.py

### Training NEAT

Train the neural network by entering the command in the terminal

    python train_neat.py

### Running best result

Run the best generated Dino by entering the command in the terminal

    python run_neat.py

### Demo

Fully Trained AI:

![438997338-bd1f0b01-5b3f-4512-a76b-f73cd675cb2f](https://github.com/user-attachments/assets/24b3c1d9-dd96-43f5-b5ac-e9189e613c17)


Debug Mode: `F1`:

![438997592-4acac6c8-4ca7-4e52-90ba-1cca0df7b150](https://github.com/user-attachments/assets/748340b0-e78f-465a-a603-24f37fe58c99)
