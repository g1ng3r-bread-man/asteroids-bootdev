from constants import *
import random
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import *
from shots import Shot
import pygame
from turret import Turret

# main branch

def render_cool_text(tuple, rot):
    surf = pygame.transform.rotate(tuple[0], rot)
    return (surf, tuple[1])
     


def render_text(text="null", x=150, y=100, fontsize=34, colour=(255,255,255), fontstr="Times New Roman"):
    font = pygame.font.SysFont(fontstr, fontsize)
    textSurface = font.render(text, False, colour)
    textRect = textSurface.get_rect()
    textRect.center = (x,y)
    return (textSurface, textRect)

def render_stats(if_stats_on, frameClock, available_turrets, ShootSpeed, asteroids, shots):
    if if_stats_on is False:
        statsSurf, statsRect = render_text("Press Z for stats", 120, 70)

        SCREEN.blit(statsSurf, statsRect)
        return
    FrameSurf, FrameRect = render_text(f"FPS: {int(frameClock.get_fps())}", 50, 70, 25)
    TurretSurf, TurretRect = render_text(f"Turrets: {available_turrets}", 70, 110)
    MultSurf, MultRect = render_text(f"Shoot speed: {ShootSpeed}x", 110, 150)
    AstNumSurf, AstNumRect = render_text(f"Shot count: {len(shots)}", 100, 190)
    ShotNumSurf, ShotNumRect = render_text(f"Asteroid count: {len(asteroids)}", 125, 230)
    TurretKeySurf, TurretKeyRect = render_text("""Keybinds for turrets: Normal turret: E, Shotgun turret: R, Sniper turret: T, Machinegun turret: Y""", 600, 700, 24)

    SCREEN.blit(TurretKeySurf, TurretKeyRect)
    SCREEN.blit(ShotNumSurf, ShotNumRect)
    SCREEN.blit(AstNumSurf, AstNumRect)
    SCREEN.blit(FrameSurf, FrameRect)
    SCREEN.blit(TurretSurf, TurretRect)
    SCREEN.blit(MultSurf, MultRect)
    return


def main():
    pygame.init()
    pygame.font.init()
    currentScore = 0
    if_stats_on = False
    next_turret_score = 0
    statsCooldown = 0
    available_turrets = 0
    turretDelay = 0
    ShootSpeed = 1
    score_rot = 0
    pygame.display.set_caption('Asteroids: "Better than Space Cursors!"')
    pygame.display.set_icon(pygame.image.load("asteroidicon.ico"))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    turrets = pygame.sprite.Group()
    colourlist = ("white", "green", "blue", "yellow", "red", "pink", "brown")
    AsteroidField.containers = (updatable)
    Asteroid.containers = (drawable, asteroids, updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (drawable, updatable, shots)
    Turret.containers = (drawable, updatable, turrets)

    frameClock = pygame.time.Clock()
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
        if score_rot <= 10:
            scoreSurface, scoreRect = render_cool_text(render_text(f"Score: {currentScore}", 65, 30), score_rot)
            score_rot -= 1
        
        elif score_rot >= 350: 
            scoreSurface, scoreRect = render_cool_text(render_text(f"Score: {currentScore}", 65, 30), score_rot)
            score_rot -= 1
        statsCooldown -= dt
        keys = pygame.key.get_pressed()
        turretDelay += dt
        if keys[pygame.K_e] or keys[pygame.K_r] or keys[pygame.K_t] or keys[pygame.K_y]:
            if available_turrets >= 1 and turretDelay >= 0.4:
                turretDelay = 0
                available_turrets -= 1
                if keys[pygame.K_e]:
                        turret = Turret(playerchar.position.x, playerchar.position.y, asteroids, "normal")
                elif keys[pygame.K_r]:
                        turret = Turret(playerchar.position.x, playerchar.position.y, asteroids, "shotgun")
                elif keys[pygame.K_t]:
                        turret = Turret(playerchar.position.x, playerchar.position.y, asteroids, "sniper")
                elif keys[pygame.K_y]:
                        turret = Turret(playerchar.position.x, playerchar.position.y, asteroids, "machinegun")
                turrets.add(turret)
                updatable.add(turret)
                drawable.add(turret)
        if currentScore >= next_turret_score:
            available_turrets += 10
            next_turret_score += 30

        if keys[pygame.K_z]:
            if statsCooldown > 0:
                continue
            if_stats_on = not if_stats_on
            statsCooldown = 3

        for asteroid in asteroids:
            if asteroid.collisioncheck(playerchar) == True:
                print("Game over!")
                run = False

            for bullet in shots:
                if asteroid.collisioncheck(bullet) == True:
                    if asteroid.isUpgrade == True:
                        currentScore += 4
                        ShootSpeed = round(ShootSpeed * 1.2, 2)
                        playerchar.current_shoot_cooldown = max(0.00, playerchar.current_shoot_cooldown * 0.8)
                    currentScore += 1
                    asteroid.split()
                    bullet.piercing -= 1
                    if bullet.piercing <= 0:
                        bullet.kill()
            if asteroid.homing:
                 asteroid.home

        if playerchar.rainbowmode == True:
            SCREEN.fill(random.choice(colourlist))
        else:
            SCREEN.fill("black")

        
        updatable.update(dt, playerchar)

        for drawble in drawable:
            drawble.draw(SCREEN)
        SCREEN.blit(scoreSurface, scoreRect)
        render_stats(if_stats_on, frameClock, available_turrets, ShootSpeed, asteroids, shots)
        pygame.display.flip()
        frameClock.tick(60)
        frame = frameClock.tick(60)
        dt = frame / 1000


if __name__ == "__main__":
    main()