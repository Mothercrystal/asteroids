import pygame
from constants import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()


        dt = clock.tick(60) / 1000 #limit framerate to 60 fps

if __name__ == "__main__":
    main()
