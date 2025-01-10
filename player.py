import os
import pygame
import settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEART_IMAGE = pygame.image.load(os.path.join(BASE_DIR, "assets\\images\\heart.png"))
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (30, 30))

class Player(pygame.sprite.Sprite):

    def ___init___(self):
        super().__init__()
        self.image = pygame.Surface([10, 50])
        self.image.fill(settings.white)
        self.rect = self.image.get_rect()
        self.lives = 3

    def move(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect) 

    def take_damage(self):
        self.lives -= 1
        if self.lives == 0:
            self.kill()

    def draw_lives(screen, player_v):
        for i in range(player_v.lives):
            x = settings.widthv - (i + 1) * 20
            y = 10
            screen.blit(HEART_IMAGE, (x, y))
            
    def reset(self):
        self.lives = 3
        self.rect.center = (settings.widthv // 2, settings.heightv - 20)
