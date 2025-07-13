from constants import *
import pygame


def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill("black")
        pygame.display.flip()



if __name__ == "__main__":
    main()











