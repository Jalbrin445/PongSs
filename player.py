import os
import pygame
import settings
import C_pantalla


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HEART_IMAGE = pygame.image.load(os.path.join(BASE_DIR, "assets\\images\\heart.png"))
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (30, 30))

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(settings.white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.screen_height = screen_height
        self.lives = 3

    def move(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(self.rect.y, settings.heightv - self.rect.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect) 

    def draw_lives1(self, screen):
        for i in range(self.lives):
            x = 10 + i * 30
            y = 10
            screen.blit(HEART_IMAGE, (x, y))

    def draw_lives2(self, screen):
        for i in range(self.lives):
            x = settings.widthv - (i + 1) * 30
            y = 10
            screen.blit(HEART_IMAGE, (x, y))
    
    def take_damage(self):
        self.lives -= 1
        if self.lives == 0:
            self.kill()
            
    def reset(self):
        self.lives = 3
        self.rect.center = (settings.widthv // 2, settings.heightv - 20)
    
    def get_rect(self):
        return self.rect
    
    def change_color(self, color):
        self.image.fill(color)


