import pygame
import settings

class Ball:
    def __init__(self, x, y, radius, x_speed, y_speed, color = settings.white):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.color = color

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def bounce_y(self):
        self.y_speed *= -1

    def bounce_x(self):
        self.x_speed *= -1

    def reset_position(self):
        self.x = settings.widthv // 2
        self.y = settings.heightv // 2
        self.bounce_x()
        self.bounce_y()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
    
    def change_color(self, color):
        self.color = color
    
        