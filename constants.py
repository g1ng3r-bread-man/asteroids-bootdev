import pygame
#SCREEN CONSTANTS
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#ASTEROID CONSTANTS
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 7770.0  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

#PLAYER CONSTANTS
PLAYER_RADIUS = 20
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAYER_TURN_SPEED = 280
PLAYER_SPEED = 200
PLAYER_SHOOT_COOLDOWN = 0.3 #seconds

#SHOT CONSTANTS
SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
TURRET_SHOOT_SPEED = 590
SNIPER_TURRET_SHOOT_SPEED = 1000
SHOTGUN_TURRET_SHOOT_SPEED = 430

#TURRET CONSTANTS
TURRET_RADIUS = 15
NORM_TURRET_SHOT_COOLDOWN = 0.9
SHOTGUN_TURRET_SHOT_COOLDOWN = 1.9
SNIPER_TURRET_SHOT_COOLDOWN = 2.9
MACHINE_GUN_SHOT_COOLDOWN = 0.45
MACHINE_GUN_MIN_COOLDOWN = 0.07
MACHINE_GUN_BURST_SIZE = 40
MACHINE_GUN_RELOAD = 3

#IMAGE FILES
ncar = pygame.transform.scale(pygame.image.load("asteroids car/n.png").convert_alpha(), (55,55))
nwcar = pygame.transform.scale(pygame.image.load("asteroids car/nw.png").convert_alpha(), (55,55))
wcar = pygame.transform.scale(pygame.image.load("asteroids car/w.png").convert_alpha(), (55,55))
swcar = pygame.transform.scale(pygame.image.load("asteroids car/sw.png").convert_alpha(), (55,55))
scar = pygame.transform.scale(pygame.image.load("asteroids car/s.png").convert_alpha(), (55,55))
secar = pygame.transform.scale(pygame.image.load("asteroids car/se.png").convert_alpha(), (55,55))
ecar = pygame.transform.scale(pygame.image.load("asteroids car/e.png").convert_alpha(), (55,55))
necar = pygame.transform.scale(pygame.image.load("asteroids car/ne.png").convert_alpha(), (55,55))