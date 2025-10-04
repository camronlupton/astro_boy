import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameTick = 1
    while gameTick >= 0 :
        gameTick +=1
        ## allows user to close window (copy pasted from course)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        ##print(gameTick)

        screen.fill((0, 0, 0))


if __name__ == "__main__":
    main()
