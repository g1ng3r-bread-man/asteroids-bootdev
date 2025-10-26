from constants import *
import random
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import *
from shots import Shot
import pygame
from turret import Turret

# this is the real main

def render_text(text="null", x=150, y=100, fontsize=34, colour=(255,255,255), fontstr="Times New Roman"):
    font = pygame.font.SysFont(fontstr, fontsize)
    textSurface = font.render(text, False, colour)
    textRect = textSurface.get_rect()
    textRect.center = (x,y)
    return (textSurface, textRect)

def main():
    pygame.init()
    pygame.font.init()
    currentScore = 0
    next_turret_score = 0
    available_turrets = 0
    turretDelay = 0
    pygame.display.set_caption('Asteroids: "Better than Space Cursors!"')
    pygame.display.set_icon(pygame.image.load("asteroidicon.ico"))
    scoreSurface, scoreRect = render_text("Score: 0", 65, 30)
    FrameSurf, FrameRect = render_text("FPS: 0", 50, 70, 25)
    TurretSurf, TurretRect = render_text("Turrets: 0", 65, 110)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    turrets = pygame.sprite.Group()
    frameClock = pygame.time.Clock()
    colourlist = ("white", "green", "blue", "yellow", "red", "pink", "brown")
    AsteroidField.containers = (updatable)
    Asteroid.containers = (drawable, asteroids, updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (drawable, updatable, shots)
    Turret.containers = (drawable, updatable, turrets)

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
        keys = pygame.key.get_pressed()
        FrameSurf, FrameRect = render_text(f"FPS: {int(frameClock.get_fps())}", 50, 70, 25)
        scoreSurface, scoreRect = render_text(f"Score: {currentScore}", 65, 30)
        TurretSurf, TurretRect = render_text(f"Turrets: {available_turrets}", 70, 110)
        turretDelay += dt
        if keys[pygame.K_e]:
            if available_turrets >= 1 and turretDelay >= 0.5:
                turretDelay = 0
                available_turrets -= 1
                turret = Turret(playerchar.position.x, playerchar.position.y, asteroids)
                turrets.add(turret)
                updatable.add(turret)
                drawable.add(turret)
        if currentScore >= next_turret_score:
            available_turrets += 1
            next_turret_score += 30
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
                    asteroid.split()
                    bullet.kill()

        if playerchar.rainbowmode == True:
            SCREEN.fill(random.choice(colourlist))
        else:
            SCREEN.fill("black")
        SCREEN.blit(scoreSurface, scoreRect)
        SCREEN.blit(FrameSurf, FrameRect)
        SCREEN.blit(TurretSurf, TurretRect)
        updatable.update(dt)

        for drawble in drawable:
            drawble.draw(SCREEN)
        pygame.display.flip()
        frameClock.tick(60)
        frame = frameClock.tick(60)
        dt = frame / 1000


if __name__ == "__main__":
    main()