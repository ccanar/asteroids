SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_WIDTH = 2
ASTEROID_SPLIT_MIN_ANGLE = 20
ASTEROID_SPLIT_MAX_ANGLE = 50
ASTEROID_SPLIT_VELOCITY_MULTIPLAYER = 1.2
ASTEROID_VALUE_SMALL = 3
ASTEROID_VALUE_MEDIUM = 2
ASTEROID_VALUE_BIG = 1
ASTEROID_SIZE_SMALL = 20
ASTEROID_SIZE_MEDIUM = 40
ASTEROID_SIZE_BIG = 60

ASTEROID_ANIMATION_EXPLOSION_PATH = "./content/asteroid/explosion"
ASTEROID_ANIMATION_EXPLOSION_NAME_OF_FILE = "explosion"
ASTEROID_ANIMATION_EXPLOSION_NUM_OF_SPRITES = 5
ASTEROID_ANIMATION_EXPLOSION_ANIMATION_SPEED = 8 # higher slower
ASTEROID_ANIMATION_EXPLOSION_SCALE = 0.5 # 0 - 1

PLAYER_RADIUS = 20
PLAYER_WIDTH = 2
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

PLAYER_SPAWN_POSITION_X = SCREEN_WIDTH / 2
PLAYER_SPAWN_POSITION_Y = SCREEN_HEIGHT / 2

PLAYER_MAX_LIVES = 3

PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3
PLAYER_SHOT_RADIUS = 5

PLAYER_STATUS_NOMINAL = 0
PLAYER_STATUS_DEAD = -1
PLAYER_STATUS_TOOK_DAMAGE = 1

PLAYER_UI_LIVES_FONT = None
PLAYER_UI_LIVES_FONT_SIZE = 32
PLAYER_UI_LIVES_FONT_COLOR = "white"
PLAYER_UI_LIVES_POSITION_X = 10
PLAYER_UI_LIVES_POSITION_Y = 42

SCORING_SYSTEM_UI_FONT = None
SCORING_SYSTEM_UI_FONT_SIZE = 32
SCORING_SYSTEM_UI_FONT_COLOR = "white"
SCORING_SYSTEM_UI_POSITION_X = 10
SCORING_SYSTEM_UI_POSITION_Y = 10

GAME_STATUS_RUNNING = 1
GAME_STATUS_PLAYER_DEAD = -1
