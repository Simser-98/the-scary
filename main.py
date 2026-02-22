import pygame

from game import Game

def main():
    """the main function that starts the game"""
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()