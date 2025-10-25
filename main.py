from constants import *
import random
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import *
from shots import Shot
import pygame

def render_text(text="null", x=150, y=100, fontsize=34, colour=(255,255,255), fontstr="Times New Roman"):
    font = pygame.font.SysFont(fontstr, fontsize)
    textSurface = font.render(text, False, colour)
    textRect = textSurface.get_rect()
    textRect.center = (x,y)
    return (textSurface, textRect)

def main():
    pygame.init()
    pygame.font.init()
    global CurrentPlayerShootCooldown, CurrentPlayerShotSpeed
    currentScore = 0
    scoreSurface, scoreRect = render_text("Score: 0", 65, 30)
    FrameSurf, FrameRect = render_text("FPS: 0", 50, 70, 25)
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
        FrameSurf, FrameRect = render_text(f"FPS: {int(dt * 1000)}", 50, 70, 25)
        for asteroid in asteroids:
            if asteroid.collisioncheck(playerchar) == True:
                print("Game over!")
                run = False
            for bullet in shots:
                if asteroid.collisioncheck(bullet) == True:
                    if asteroid.isUpgrade == True:
                        currentScore += 4
                        playerchar.current_shoot_cooldown = max(0.05, playerchar.current_shoot_cooldown * 0.8)
                    currentScore += 1
                    scoreSurface, scoreRect = render_text(f"Score: {currentScore}", 65, 30)
                    asteroid.split()
                    bullet.kill()

        if playerchar.rainbowmode == True:
            screen.fill(random.choice(colourlist))
        else:
            screen.fill("black")
        screen.blit(scoreSurface, scoreRect)
        screen.blit(FrameSurf, FrameRect)
        updatable.update(dt)

        for drawble in drawable:
            drawble.draw(screen)
        pygame.display.flip()
        frame = pygame.time.Clock().tick(60)
        dt = frame / 1000


if __name__ == "__main__":
    main()