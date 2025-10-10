import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():

    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    
    

    ## groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    asteroidFieldObj = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots, 0)

    while True:
        ## allows user to close window (copy pasted from course)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        ## print(gameTick)

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for entity in asteroids:
            if entity.hasColided(player):
                print(f"You score {score} points!")
                sys.exit("Game Over!")

        
        for entity in asteroids:
            for bullet in shots:
                if entity.hasColided(bullet):
                    entity.split()
                    bullet.kill()
                    score += 1

        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
