import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000 #limit framerate to 60 fps

if __name__ == "__main__":
    main()
