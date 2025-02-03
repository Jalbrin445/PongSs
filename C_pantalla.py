# Description: Este archivo contiene la función CambioPantalla que se encarga de cambiar el color de la pantalla y de la puntuación dependiendo de la puntuación del jugador.
import pygame, settings, Enemy_Ball

pygame.init()
score = 0 # Inicialización de la variable de puntuación


screen = pygame.display.set_mode((settings.widthv, settings.heightv))
font_scores = pygame.font.Font(None, 30)

def CambioPantalla(score):
    if score < 100:
        text_score = font_scores.render(f"Scores: {score}", True, settings.white)
        screen.fill(settings.black) # Dibujar el fondos de pantalla
    elif score >= 100:
        text_score = font_scores.render(f"Scores: {score}", True, settings.black) 
        screen.fill(settings.white) # Dibujar el fondo de pantalla
    screen.blit(text_score, (settings.widthv // 2 - 50, 10)) # Dibujar la puntuación

def cambiar_color_PP(score, pelota, jugador1, jugador2):
    if score >= 100:
        jugador1.change_color(settings.black)
        jugador2.change_color(settings.black)
        pelota.change_color(settings.black)