from Bala import *
from Music import *
from Nave import *
from Piedra import *

import pygame
from pygame.locals import *
import math
from random import randint

ANCHO = 600
ALTO = 600
TotalB = 7
# colores RGB (red green blue)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR_A = (85, 56, 200)


# def Game_init():
pygame.init()
espacio = pygame.display.set_mode((ANCHO, ALTO))  # pantalla
pygame.display.set_caption('Naves en el espacio')
# espacio.fill(BLANCO)  # color de fondo


def Game_music():
    musica = Music()
    musica.PlayMusic('recursos/new_level.wav')


def Game_timer():
    # tiempo (para notar la animacion y ver el movimiento de la pelota )
    reloj = pygame.time.Clock()


def draw_init():
    # background=pygame.Surface((espacio.get_rect().width, espacio.get_rect().height))
    # espacio.blit(background, background.get_rect())
    bg = pygame.image.load('img/FONDO1.png').convert()
    
    espacio.blit(bg, (0,0))
    pygame.display.flip()
    pygame.time.delay(2000)
	# espacio.fill(BLANCO)#color de fondo


def draw_nave(image):
    image = pygame.image.load(image).convert()
    espacio.blit(image, ((ANCHO/2)-100, (ALTO/2)-100))  # imagen ne el centro
    pygame.display.flip()
    # pygame.time.delay(2000)
    # espacio.fill(BLANCO)  # color de fondo


if __name__ == '__main__':
    # una nave
    nave1 = Nave()

    # Un array de balas
    pbala = []
    pbala = [Bala() for i in range(TotalB)]

    pbala2 = []
    pbala2 = [Bala() for i in range(TotalB)]

    pbala3 = []
    pbala3 = [Bala() for i in range(TotalB)]

    # Piedras
    pPiedra = []
    pPiedra = [Piedra() for i in range(TotalB)]

    # Iniciar ventana
    # Game_init()
    Game_timer()
    Game_music()

    draw_init()

    
    while True:
        draw_nave('img/nave.png')
    # print pbala[1].get_AltoB()

    pygame.quit()#cerrar venta
