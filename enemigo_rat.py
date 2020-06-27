import sys, pygame
from pygame.locals import *
#import random 
import math
pygame.init()

#Constante
width= 1340
heigth = 600
vidas=10

#IMAGENES
screen = pygame.display.set_mode((width,heigth))

icono_juego = pygame.image.load("hamster.jpg")
fondo= pygame.image.load("forest_loop.png")
enemigo_rat= pygame.image.load("rat_idle.png")
perrito= pygame.image.load("hurt1.png")

tipo_letra = pygame.font.Font('freesansbold.ttf', 28)

pygame.display.set_icon(icono_juego)
pygame.display.set_caption("Prueba 1")
#mover al raton
pos_rat_x= width//2-(enemigo_rat.get_size()[0]//2)
pos_rat_y= heigth-(enemigo_rat.get_size()[1])

pos_perrito_x,pos_perrito_y= 100, 530

#Obtener los tamaños de...
rat_size= enemigo_rat.get_size()
perrito_size = perrito.get_size()
#FUNCIONES 

#Poner al raton en una posicion x,y
def rat(x,y):
    screen.blit(enemigo_rat,(x,y))

def pos_perrito(x,y):
    screen.blit(perrito,(x,y))

def mostrar_vidas(x,y):
    vidas_render =  tipo_letra.render("Vidas : "+ str(vidas), True, (255,255,255))
    screen.blit(vidas_render,(x,y))

def hubo_colision(x1,x2,y1,y2):
    distancia = math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
    return True if distancia < 80 else False

def main():
    #pygame.init()
    pos_rat_x= width//2-(rat_size[0]//2)
    rat_mov = 3
    while True :
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(fondo,(0,0))
        #-----------------------------------------------------------
        pos_rat_x -= rat_mov
        #izquierda
        if pos_rat_x <= 0:
            rat_mov = -3
        #derecha
        elif pos_rat_x >= width - rat_size[0]:
            rat_mov = 3

        rat(pos_rat_x,pos_rat_y)
        #-----------------------------------------------------------

        pos_perrito(pos_perrito_x,pos_perrito_y)
    
        #-----------------------------------------------------------
        mostrar_vidas(10,10)
        colision = hubo_colision(pos_rat_x,pos_perrito_x,pos_rat_y,pos_perrito_y)
        
        if colision:
            vidas -=1

        pygame.display.update()

main()