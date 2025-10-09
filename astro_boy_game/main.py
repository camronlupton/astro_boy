import pygame
from constants import *
from player import Player


def main():

    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    
    

    ## groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        ## allows user to close window (copy pasted from course)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        ## print(gameTick)

        screen.fill((0, 0, 0))
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
