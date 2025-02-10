import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y, file_path, name_of_file, num_sprites, animation_speed = 4, scale = 1):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.scale = scale
        self.images = []
        for i in range(num_sprites):
            image = pygame.image.load(f"{file_path}/{name_of_file}{i}.png")
            image = pygame.transform.scale(image, (100 * self.scale, 100 * self.scale))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        self.animation_speed = animation_speed


    def update(self, dt):
            self.counter += 1  
            if self.counter >= self.animation_speed and self.index < len(self.images):
                self.counter = 0
                self.index += 1
                self.image = self.images[self.index]

            # if the animation is complete, reset animation index
            if self.index >= len(self.images) - 1 and self.counter >= self.animation_speed - 1:
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)