#Archivo de música.


import pygame
import os

pygame.init()
pygame.mixer.init() # Carga de sonidos

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sonido_colision = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets\\sounds\\Boing_Sound.mp3"))