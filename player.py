import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_ACCELERATION
from constants import PLAYER_MAX_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from constants import PLAYER_STATUS_NOMINAL
from constants import PLAYER_STATUS_DEAD
from constants import PLAYER_STATUS_TOOK_DAMAGE
from constants import PLAYER_SPAWN_POSITION_X
from constants import PLAYER_SPAWN_POSITION_Y
from constants import PLAYER_UI_LIVES_FONT
from constants import PLAYER_UI_LIVES_FONT_SIZE
from constants import PLAYER_UI_LIVES_POSITION_X
from constants import PLAYER_UI_LIVES_POSITION_Y
from constants import PLAYER_UI_LIVES_FONT_COLOR


class Player(CircleShape):
    
    
    def __init__(self, x, y, lives):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.acceleration = PLAYER_ACCELERATION
        self.max_speed = PLAYER_MAX_SPEED
        self.velocity = pygame.Vector2(0, 0)
        self.shoot_cooldown = 0 # time to next shot
        self.lives = lives
        self.status = PLAYER_STATUS_NOMINAL
        self.ui_lives_font = pygame.freetype.SysFont(PLAYER_UI_LIVES_FONT, PLAYER_UI_LIVES_FONT_SIZE)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), PLAYER_WIDTH)
        self.ui_lives_font.render_to(
            screen,
            (
                PLAYER_UI_LIVES_POSITION_X, 
                PLAYER_UI_LIVES_POSITION_Y
            ),
            f"Lives: {self.lives}",
            PLAYER_UI_LIVES_FONT_COLOR
            )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * self.acceleration * dt
        self.velocity = self.velocity.clamp_magnitude(self.max_speed)

    def shoot(self):
        if self.shoot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def take_damage(self):
        self.lives -= 1
        self.status = PLAYER_STATUS_TOOK_DAMAGE

    def get_lives(self):
        return self.lives

    def get_status(self):
        if self.status == PLAYER_STATUS_TOOK_DAMAGE:
            if self.lives == 0:
                return PLAYER_STATUS_DEAD
        return self.status

    def reset(self):
        self.position = (PLAYER_SPAWN_POSITION_X, PLAYER_SPAWN_POSITION_Y)
        self.status = PLAYER_STATUS_NOMINAL
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.position += self.velocity * dt
        
        self.shoot_cooldown -= dt       