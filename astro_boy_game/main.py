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
    hp = 3
    
    HeaderOne = pygame.font.SysFont("Arial", 20, bold = True)
    HeaderTwo = pygame.font.SysFont("Arial", 20, bold = True)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    
    

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
        ##ADDED SCORE
        draw_text(f"SCORE: {score}", HeaderOne, (150,150,150), 15, 15)
        ##ADDED LIVES
        draw_text(f"LIVES: {hp}", HeaderTwo, (150,20,20), 15, 40)
        updatable.update(dt)
        for entity in asteroids:
            if entity.hasColided(player):
                if hp == 1:
                    print(f"You score {score} points!")
                    sys.exit("Game Over!")
                else:
                    ##LOSING LIVES
                    hp -= 1 
                    entity.kill()

        
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
