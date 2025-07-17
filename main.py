from constants import *
import random
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import *
from shots import Shot
import pygame

#SUPERDOOPERMEGAULTRARAINBOWMODE!!!!!
rainbowmode = False

def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    colourlist = ("white", "green", "blue", "yellow", "red", "pink", "brown")
    AsteroidField.containers = (updatable)
    Asteroid.containers = (drawable, asteroids, updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (drawable, updatable, shots)
    dt = 0
    print("Starting Asteroids!")
    print(f"""Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
    playerchar = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    field = AsteroidField()
    print("Asteroids successfully started!")

    #game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if rainbowmode == True:
            screen.fill(random.choice(colourlist))
        else:
            screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisioncheck(playerchar) == True:
                print("Game over!")
                run = False
            for bullet in shots:
                if asteroid.collisioncheck(bullet) == True:
                    asteroid.kill()
                    bullet.kill()
                
        for drawble in drawable:
            drawble.draw(screen)
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        frame = pygame.time.Clock().tick(60)
        dt = frame / 1000



if __name__ == "__main__":
    main()











