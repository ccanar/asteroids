# this allows us to use code from the open-sourse pygame library throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add a class variable  called containers to the class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # for thing in updatable:
        #     thing.update(dt)
        updatable.update(dt)


        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                exit()


        screen.fill("black")
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        # limit framerate to 60 FPS    
        dt = clock.tick(60) / 1000 # converting from milliseconds to seconds

if __name__ == "__main__":
    main()