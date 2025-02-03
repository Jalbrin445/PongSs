# Este es un videojuego explicativo
# Importación de librerias
import pygame
# Importación de módulos
import settings, player, music, C_pantalla, Enemy_Ball
#import menu_go_ps


# Inicialización de pygame
pygame.init()

#Creamos la ventana y el reloj que controla los fps
screen = pygame.display.set_mode((settings.widthv, settings.heightv))
clock = pygame.time.Clock()

# Coordenadas iniciales de la pelota
pelota = Enemy_Ball.Ball(settings.widthv // 2, settings.heightv // 2, settings.pelota_r, 3, 3)

# Coordenadas del jugador 1
player1_coor_x = 50
player1_coor_y = 300 - (settings.player_height // 2)

# Coordenadas del jugador 2
player2_coor_x = 750 - settings.player_width
player2_coor_y = 300 - (settings.player_height // 2)

# Velocidad de los jugadores
player1_speed = 0
player2_speed = 0

# Instancias de los jugadores
jugador1 = player.Player(player1_coor_x, player1_coor_y, settings.player_width, settings.player_height, player1_speed, settings.heightv)
jugador2 = player.Player(player2_coor_x, player2_coor_y, settings.player_width, settings.player_height, player2_speed, settings.heightv)
running = True # Incialización de la variable de salida del bucle principal

while running:
    # Recorre todos los eventos que pasan con pygame (Evento de teclado, de salida y entre otros)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Comprobar teclas para el jugador 1
            if event.key == pygame.K_w:
                player1_speed = -settings.speed_player
            if event.key == pygame.K_s:
                player1_speed = settings.speed_player
            # Comprobar teclas para el jugador 2
            if event.key == pygame.K_UP:
                player2_speed = -settings.speed_player
            if event.key == pygame.K_DOWN:
                player2_speed = settings.speed_player
        # Comprobar eventos si no se pulsa una de las teclas
        if event.type == pygame.KEYUP:
            # Comprobar teclas para el jugador 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_speed = 0
            # Comprobar teclas para el jugador 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_speed = 0
    
    ## ---> Estado principal
    
    ## ---> Estado playing
    # Logica de movimiento de los jugadores
    jugador1.move(player1_speed)
    jugador2.move(player2_speed)

    # Movimiento de la pelota
    pelota.move()

    # Lógica para que no salga de la pantalla la pelota
    if pelota.y > (settings.heightv - pelota.radius) or pelota.y < pelota.radius:
        pelota.bounce_y()

    # Verifica si la pelota sale por los bordes izquierdo o derecho de la pantalla, quita vida y reinicia la posición de la pelota
    if pelota.x <= 0:
        jugador1.take_damage()
        pelota.reset_position()
    elif pelota.x >= settings.widthv:
        jugador2.take_damage()
        pelota.reset_position()

    # Verifica si un jugador se queda sin vidas
    if jugador1.lives == 0 or jugador2.lives == 0:
        running = False

    # Colisiones
    if pelota.get_rect().colliderect(jugador1.get_rect()) or pelota.get_rect().colliderect(jugador2.get_rect()):
        music.sonido_colision.play()
        pelota.bounce_x()
        C_pantalla.score += 20
    
    # Cambiar color de los jugadores y la pelota si el puntaje es igual o mayor a 100
    C_pantalla.cambiar_color_PP(C_pantalla.score, pelota, jugador1, jugador2)

    # Cambio de pantalla
    C_pantalla.CambioPantalla(C_pantalla.score)
    
    # Dibujo de jugadores y pelota
    jugador1.draw(screen)
    jugador2.draw(screen)
    jugador1.draw_lives1(screen)
    jugador2.draw_lives2(screen)
    pelota.draw(screen)

    # Actualiza pantalla y actualiza reloj 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
