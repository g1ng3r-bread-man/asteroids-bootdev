from constants import *
from player import *
import pygame


def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    dt = 0
    print("Starting Asteroids!")
    print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    playerchar = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for drawble in drawable:
            drawble.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        frame = pygame.time.Clock().tick(60)
        dt = frame / 1000



if __name__ == "__main__":
    main()











