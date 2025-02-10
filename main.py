# this allows us to use code from the open-sourse pygame library throughout this file
import pygame
import pygame.freetype
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
from scoring_system import ScoringSystem
from animation import Animation

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    animations = pygame.sprite.Group()

    background_image = pygame.image.load(f"content/background/background_image.png")

    # add a class variable  called containers to the class
    ScoringSystem.containers = (drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Animation.containers = (updatable, drawable, animations)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_MAX_LIVES)

    scoring_system = ScoringSystem()
    asteroid_field = AsteroidField()

    game_status = GAME_STATUS_RUNNING
    while True:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        if game_status == GAME_STATUS_RUNNING:    
            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    player.take_damage()

            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collides_with(shot):
                        asteroid.split()
                        scoring_system.add_score(asteroid.get_value())
                        shot.kill()

            screen.blit(background_image, (0, 0)) # no fill black cos bg img hast black background

            for thing in drawable:
                thing.draw(screen)

        status = player.get_status()
        if status == PLAYER_STATUS_DEAD:
            screen.fill("black")
            game_over(screen)
            scoring_system.draw(screen, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2)
            game_status = GAME_STATUS_PLAYER_DEAD
        elif status == PLAYER_STATUS_TOOK_DAMAGE:
            for animation in animations:
                animation.kill()
            for asteroid in asteroids:
                asteroid.kill()
            player.reset()

        pygame.display.flip()
        
        # limit framerate to 60 FPS    
        dt = clock.tick(60) / 1000 # converting from milliseconds to seconds

def game_over(screen: pygame.Surface):
    text_font = pygame.freetype.SysFont(None, 42)
    # text_font.render_to(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), "GAME OVER", "white")
    text_surf, text_rect = text_font.render("GAME OVER", "white")
    screen.blit(text_surf, (SCREEN_WIDTH / 2 - text_rect.width / 2, SCREEN_HEIGHT / 3 - text_rect.height / 2))

if __name__ == "__main__":
    main()