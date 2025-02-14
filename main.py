import pygame
from constants import *
from player import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable,)


    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")


    while True:
        dt = clock.tick(60) / 1000 #limit framerate to 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        
        
        

if __name__ == "__main__":
    main()
