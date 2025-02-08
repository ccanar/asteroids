import pygame
import pygame.freetype
from constants import SCORING_SYSTEM_UI_FONT
from constants import SCORING_SYSTEM_UI_FONT_SIZE
from constants import SCORING_SYSTEM_UI_FONT_COLOR
from constants import SCORING_SYSTEM_UI_POSITION_X
from constants import SCORING_SYSTEM_UI_POSITION_Y

class ScoringSystem(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.score = 0
        self.font = pygame.freetype.SysFont(SCORING_SYSTEM_UI_FONT, SCORING_SYSTEM_UI_FONT_SIZE)
        
        
    def draw(
            self, 
            screen: pygame.Surface, 
            pos_x = SCORING_SYSTEM_UI_POSITION_X, 
            pos_y = SCORING_SYSTEM_UI_POSITION_Y,
            ):
        self.font.render_to(
            screen,
            (
                pos_x, 
                pos_y
            ),
            f"Score: {self.score}",
            SCORING_SYSTEM_UI_FONT_COLOR
            )

    def add_score(self, score: int):
        self.score += score

    def get_score(self):
        return self.score