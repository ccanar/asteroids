import pygame
import pygame.freetype
from constants import SCORING_SYSTEM_FONT_SIZE
from constants import SCORING_SYSTEM_FONT_COLOR
from constants import SCORING_SYSTEM_POSITION_X
from constants import SCORING_SYSTEM_POSITION_Y

class ScoringSystem(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.score = 0
        self.font = pygame.freetype.SysFont(None, SCORING_SYSTEM_FONT_SIZE)
        
        
    def draw(self, screen: pygame.Surface):
        text_surface = self.font.render(str(self.score), SCORING_SYSTEM_FONT_COLOR)
        screen.blit(text_surface[0], (SCORING_SYSTEM_POSITION_X , SCORING_SYSTEM_POSITION_Y))

    def add_score(self, score: int):
        self.score += score

    def get_score(self):
        return self.score