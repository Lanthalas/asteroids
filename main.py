# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import * 
from player import * 
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0,0,0)
    fpsClock = pygame.time.Clock()
    dt = 0

    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(color)
        
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = fpsClock.tick(60) / 1000


if __name__ == "__main__":
    main()