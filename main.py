import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    # seting groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    
    # seting screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # seting player sprite
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # setting asteroid field
    asteroid_field = AsteroidField()
    
    # cli starting confirmaion
    print("Starting asteroids!")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    
    # main game loop
    while True:
        # exit from the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black", rect=None)
        for object in updatable:
            object.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    
if __name__ == "__main__":
    main()