# Este es un videojuego explicativo
# Importación de librerias
import pygame
# Importación de módulos
import settings


# Inicialización de pygame
pygame.init()

class Jugador:
    def __init__(self, x, y, width, height, speed, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.screen_height = screen_height

    def mover(self):
        self.y += self.speed
        self.y = max(0, min(self.y, self.screen_height - self.height))

    def dibujar(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



#Creamos la ventana y el reloj que controla los fps
screen = pygame.display.set_mode((settings.widthv, settings.heightv))
clock = pygame.time.Clock()

# Coordenadas del jugador 1
player1_coor_x = 50
player1_coor_y = 300 - (settings.player_height // 2)

# Coordenadas del jugador 2
player2_coor_x = 750 - settings.player_width
player2_coor_y = 300 - (settings.player_height // 2)

# Coordenadas de la pelota
pelota_coor_x = settings.widthv // 2
pelota_coor_y = settings.heightv // 2

#Velocidad pelota
pelota_x_speed = 3
pelota_y_speed = 3

# Instancias de los jugadores
jugador1 = Jugador(player1_coor_x, player1_coor_y, settings.player_width, settings.player_height, 0, settings.heightv)
jugador2 = Jugador(player2_coor_x, player2_coor_y, settings.player_width, settings.player_height, 0, settings.heightv)
game_over = False # Incialización de la variable de salida

while not game_over:
    # Recorre todos los eventos que pasan con pygame (Evento de teclado, de salida y entre otros)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            # Comprobar teclas para el jugador 1
            if event.key == pygame.K_w:
                jugador1.set_speed(-settings.speed_player)
            if event.key == pygame.K_s:
                jugador1.set_speed(settings.speed_player)
            # Comprobar teclas para el jugador 2
            if event.key == pygame.K_UP:
                jugador2.set_speed(-settings.speed_player)
            if event.key == pygame.K_DOWN:
                jugador2.set_speed(settings.speed_player)
        # Comprobar eventos si no se pulsa una de las teclas
        if event.type == pygame.KEYUP:
            # Comprobar teclas para el jugador 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                jugador1.set_speed(0)
            # Comprobar teclas para el jugador 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                jugador2.set_speed(0)
    
    ## ---> Estado principal
    
    ## ---> Estado playing
    # Logica de movimiento de los jugadores
    jugador1.mover()
    jugador2.mover()

    # Lógica para que no salga de la pantalla la pelota
    if pelota_coor_y > (settings.heightv - settings.pelota_r) or pelota_coor_y < settings.pelota_r:
        pelota_y_speed *= -1

    if pelota_coor_x > 800 or pelota_coor_x < 0:
        pelota_coor_x = 400
        pelota_coor_y = 300
        #Si sale de la pantalla, invierte dirección
        pelota_x_speed *= -1
        pelota_y_speed *= -1

    # Movimiento de la pelota
    pelota_coor_x += pelota_x_speed
    pelota_coor_y += pelota_y_speed
    

    screen.fill(settings.black) # Dibujar el fondo de pantalla
    # Dibujo
    #jugador1 = pygame.draw.rect(screen, settings.white, (player1_coor_x, player1_coor_y, settings.player_width, settings.player_height))
    #jugador2 = pygame.draw.rect(screen, settings.white, (player2_coor_x, player2_coor_y, settings.player_width, settings.player_height))
    jugador1.dibujar(screen, settings.white)
    jugador2.dibujar(screen, settings.white)

    pelota = pygame.draw.circle(screen, settings.white, (pelota_coor_x, pelota_coor_y), settings.pelota_r)

    # Colisiones
    pelota_rect = pygame.Rect(pelota_coor_x - settings.pelota_r, pelota_coor_y - settings.pelota_r, settings.pelota_r * 2, settings.pelota_r * 2)
    if pelota_rect.colliderect(jugador1.get_rect()) or pelota_rect.colliderect(jugador2.get_rect()):
        pelota_x_speed *=-1
    
    # Actualizar pantalla y actualizar reloj 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
