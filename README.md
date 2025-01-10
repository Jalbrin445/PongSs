# **PONGSss** *(Ven y relajate un rato)*

## **Descripción del Proyecto**
    Este es un videojuego básico para aquellos apasionados al desarrollo de videojuego.

## **Características principales**

1. Sistema de vidas del jugador.

2. Enemigo dinámicos (Pelota)

3. Modularidad para mantener el código organizado.

4. Sistema de colisiones.

## **Requsitos del sistema**

- **Python 3.10** o superior.

- Pygame instalado: `pip install pygame` **(En la consola)**.

## **Instalación y Ejecución**

1. Clona el repositorio: 
    ```bash
        `git clone `

2. Instala las dependencias: 
    ```bash
    `pip install pygame`

3. Ejecuta el juego: 
    python main.py


## **Estructura del Proyecto** (descripción de los módulos).

BioQuest
- |
- |--> main.py (Archivo principal del juego).
- |--> settings.py (Configuraciones globales del juego (no todas se encuentran aquí, hay algunas que están en otros archivos)).
- |--> player.py (Clase del jugador (vidas, movimiento, dibujo)).
- |--> enemy.py (Clase de los enemigos (movimiento y colisiones)).
- |--> questions_manager.py (Módulo para gestionar preguntas y respuestas).
- |--> menu_go_ps.py (Funciones para los menús (pausa y game over)).
- |--> main_menu.py (Menu principal de juego (Inicar a jugar/Salir))
- |--> music.py (Sistema para cambiar música según estados).
- |--> assets/ (Recursos visuales y de sonido)
- |   |--> images/
- |   |--> sounds/
- |--> README.md (Este archivo)

## **Visualización del proyecto**


## **Próximas mejoras**

- Añadir clase pelota.
- Añadir menu principal, menú game over y pausa.
- Añadir sonidos.
- 
- Añadir dificultad progresiva a lo largo de un nivel.
- Añadir más enemigos.

## **Controles del juego**

- W: mover hacia arriba.
- S: Mover hacia abajo.
- A: Mover hacia la izquierda.
- D: Mover hacia la derecha.
- P: Pausar el juego.
- Q: Salir del juego.

## Autor.

- Nombre: Juan Albrin Meza Guzmán.

- GitHub: https://github.com/Jalbrin445

- Correo: mezaguzmanjuanalbrin@gmail.com

## Licencia

    Este proyecto está bajo la licencia MIT.
