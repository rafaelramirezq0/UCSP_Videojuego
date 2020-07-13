import pygame, sys
import time
from __INTRO__ import *
from __LOAD__ import *
pygame.init()
pygame.mixer.init()
pygame.init()

#Constante
ancho= 800
alto = 600
vidas=10

pygame.display.set_caption("Doggo Adventure")
pygame.display.set_icon(pygame.image.load("Sprites/icon.png"))
screen = pygame.display.set_mode((ancho,alto))
reloj = pygame.time.Clock()
listade_todoslos_sprites = pygame.sprite.Group()

# Estado del Juego
Intro1 = False
Intro2 = False
Tutorial = False
Nivel1 = True

# Fondos Niveles
bosque_fondo_lv1 = pygame.image.load("Backgrounds/nivel1_x3.png").convert()
bosque_fondo_lv2 = pygame.image.load("Backgrounds/nivel2_x3.png").convert()
bosque_fondo_lv3 = pygame.image.load("Backgrounds/nivel3_x4.png").convert()
fondo_x = -100


# Jugador
run=[run1,run2,run3,run4,run5,run6,run7,attack]
run_inv=[run1i,run2i,run3i,run4i,run5i,run6i,run7i,attack_inv]
runs=[run,run_inv]

class Player(pygame.sprite.Sprite):
    #velocidad inicial
    speed_x=0
    speed_y=0
    #animación base
    cambio=0
    imagen=0
    direc=0
    #constructor
    def __init__(self): 
        super().__init__() 
        # reemplazar con el sprite:
        self.image = runs[self.direc][self.imagen]
        # rectángulo que ocupa
        self.rect = self.image.get_rect()
        
    #esto efectúa el movimiento, va "actualizando" la velocidad e imagen
    def update(self):
        self.ancho=self.image.get_size()[1]
        self.largo=self.image.get_size()[0]
        self.gravity()
        self.deten_ataque()
        #moverse
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #animación
        self.imagen += self.cambio
        if self.imagen > len(run)-2 or self.speed_x==0:
            self.imagen = 0
        if self.speed_y!=0:
            self.imagen = 5
        if abs(self.speed_x)>5:
            self.imagen=len(run)-1
        self.image=runs[self.direc][self.imagen]
        #falta aquí chocar (o sea, poner lo que pasa si choca)   
    #gravedad
    def gravity(self):
        if self.speed_y == 0:
            self.speed_y = 5
        else:#aceleración de la gravedad
            self.speed_y += 0.35
        #tocar el suelo
        if self.rect.y >= 600 - self.ancho and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = 600 - self.ancho
        #paredes
        if self.rect.x > 800 -self.largo:
            self.rect.x = 800 -self.largo
        if self.rect.x <0:
            self.rect.left =0
        #Estancar al jugador
        if fondo_x <= -1*bosque_fondo_lv1.get_rect().width + ancho or fondo_x == 0:
            mover_fondo = False
            dfx = 0
        else:
            if self.rect.right >=350:
                self.rect.x = 350 - self.rect.width
            if self.rect.left <= 0:
                self.rect.x = 0
            if self.rect.left >= 350 - (1.1*self.rect.width):
                self.rect.x = 350 - self.rect.width


    #movimientos sin considerar plataformas
    
    def izquierda(self):
        self.speed_x = -5
        self.cambio = 1
        self.direc=1
    def derecha(self):
        self.speed_x = 5
        self.cambio = 1
        self.direc=0
    def saltar(self):
        if self.rect.bottom >= 600:
            self.speed_y = -10
    def stop(self):
        self.speed_x = 0
        self.gravity()
    def ataque(self):
        if self.imagen!=len(run)-1:
            self.speed_x*=2
    #frenos (funciona de forma similar a la gravedad, solo que desacelera)
    def deten_ataque(self):
        if self.speed_x>5:
            self.speed_x-=0.15
        if self.speed_x<-5:
            self.speed_x+=0.15  
jugador=Player()
listade_todoslos_sprites.add(jugador)
done=False
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height



# Sonidos
def load_intro():
    pygame.mixer.music.load("Sounds/title02.mp3")
    pygame.mixer.music.play(-1)
def unload_music():
    pygame.mixer.music.stop()  
def load_level1():
    pygame.mixer.music.load("Sounds/nivel_01.mp3")
    pygame.mixer.music.play(-1)
if Intro1 == True:
    pygame.mixer.music.load("Sounds/title02.mp3")
    pygame.mixer.music.play(-1)
elif Nivel1 == True:
    pygame.mixer.music.load("Sounds/nivel_01.mp3")
    pygame.mixer.music.play(-1)
while Intro1 == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(2500)
                time.sleep(2.5)
                unload_music()
                load_level1()
                Intro1 = False
                Nivel1 = True
    

    animation_intro1()
    Intro1 = False
    Intro2 = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)
while Intro2 == True:

    animation_intro2()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(2000)
                fadeout_screen(800,600)
                time.sleep(2.0)
                unload_music()
                load_level1()
                Intro2 = False
                Nivel1 = True


    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)

# Función Intro
lista = [intro1,intro2,intro3,intro4,intro5,intro6,intro7,intro8,intro9,intro10,intro11,intro12,intro13,intro14,intro15,intro16,intro17,intro18,intro19,intro20,intro21,intro22,intro23,intro24,intro25,intro26,intro27,intro28,intro29,intro30,intro31,intro32,intro33,intro34,intro35,intro36,intro37,intro38,intro39,intro40,intro41,intro42,intro43,intro44,intro45,intro46,intro47,intro48,intro49,intro50,intro51,intro52,intro53,intro54,intro55,intro56,intro57,intro58,intro59,intro60,intro61,intro62,intro63,intro64,intro65,intro66,intro67,intro68,intro69,intro70,intro71,intro72,intro73,intro74,intro75,intro76,intro77,intro78,intro79,intro80,intro81,intro82,intro83,intro84,intro85,intro86,intro87,intro88,intro89,intro90,intro91,intro92,intro93,intro94,intro95,intro96,intro97,intro98,intro99,intro100,intro101,intro102,intro103,intro104,intro105,intro106,intro107,intro108,intro109,intro110,intro111,intro112,intro113,intro114,intro115,intro116,intro117,intro118,intro119,intro120,intro121,intro122,intro123,intro124,intro125,intro126,intro127,intro128,intro129,intro130,intro131,intro132,intro133,intro134,intro135,intro136,intro137,intro138,intro139,intro140,intro141,intro142,intro143,intro144,intro145,intro146,intro147,intro148,intro149,intro150,intro151,intro152,intro153,intro154,intro155,intro156,intro157,intro158,intro159,intro160,intro161,intro162,intro163,intro164,intro165,intro166,intro167,intro168,intro169,intro170,intro171,intro172,intro173,intro174,intro175,intro176,intro177,intro178,intro179,intro180,intro181,intro182,intro183,intro184,intro185,intro186,intro187,intro188,intro189,intro190,intro191,intro192,intro193,intro194,intro195,intro196,intro197,intro198,intro199,intro200,intro201,intro202,intro203,intro204,intro205,intro206,intro207,intro208,intro209,intro210,intro211,intro212,intro213,intro214,intro215,intro216,intro217,intro218,intro219,intro220,intro221,intro222,intro223,intro224,intro225,intro226,intro227,intro228,intro229,intro230,intro231,intro232,intro233,intro234,intro235,intro236,intro237,intro238,intro239,intro240,intro241,intro242,intro243,intro244,intro245,intro246,intro247,intro248,intro249,intro250,intro251,intro252,intro253,intro254,intro255,intro256,intro257,intro258,intro259,intro260,intro261,intro262,intro263,intro264,intro265,intro266,intro267,intro268,intro269,intro270,intro271,intro272,intro273,intro274,intro275,intro276,intro277,intro278,intro279,intro280,intro281,intro282,intro283,intro284,intro285,intro286,intro287,intro288,intro289,intro290,intro291,intro292,intro293,intro294,intro295,intro296,intro297,intro298,intro299,intro300,intro301,intro302,intro303,intro304,intro305,intro306,intro307,intro308,intro309,intro310,intro311,intro312,intro313,intro314,intro315,intro316,intro317,intro318,intro319,intro320,intro321,intro322,intro323,intro324,intro325,intro326,intro327,intro328,intro329,intro330,intro331,intro332,intro333,intro334,intro335,intro336,intro337,intro338,intro339,intro340,intro341,intro342,intro343,intro344,intro345,intro346,intro347,intro348,intro349,intro350,intro351,intro352,intro353,intro354,intro355,intro356,intro357,intro358,intro359,intro360,intro361,intro362,intro363,intro364,intro365,intro366,intro367,intro368,intro369,intro370,intro371,intro372,intro373,intro374]
lista2 = [intro_img1,intro_img2,intro_img3,intro_img4]
def animation_intro1():
    for i in lista:
        screen.blit(i, [0,0])
        time.sleep(0.015)
        pygame.display.update()        
def animation_intro2():
    for i in lista:
        screen.blit(i, [0,0])
        time.sleep(0.3289)
        pygame.display.update()


# Otras Funciones
def fadeout_screen(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        #redrawWindow()
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)
def evento():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
def KeyDown():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            jugador.izquierda()
            mover_fondo = True
            dfx = 5

        if event.key == pygame.K_RIGHT:
            jugador.derecha()
            mover_fondo = True
            dfx = -5
                
        if event.key == pygame.K_UP:
            jugador.saltar()
def KeyUp():
    if event.type == pygame.KEYUP:
        mover_fondo = False 
        if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
            jugador.stop()
                                
        if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
            jugador.stop()




###        While Loop Juego         ###
# Intro1
while Intro1 == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(2500)
                time.sleep(2.5)
                unload_music()
                load_level1()
                Intro1 = False
                Nivel1 = True
    
    animation_intro1()
    Intro1 = False
    Intro2 = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)

# Intro2
while Intro2 == True:
    animation_intro2()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x or event.key == pygame.K_RETURN:
                pygame.mixer.music.fadeout(2000)
                fadeout_screen(800,600)
                time.sleep(2.0)
                unload_music()
                load_level1()
                Intro2 = False
                Nivel1 = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)

# Nivel1
mover_fondo = False

while Nivel1 == True:

    screen.blit(bosque_fondo_lv1, [fondo_x,0])
    jugador.update()

    if mover_fondo == True or jugador.speed_x > 0 or jugador.speed_x < 0:
      fondo_x += dfx
    if fondo_x <= 0 or fondo_x >= ancho:
        mover_fondo = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #mover_fondo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador.izquierda()
                if fondo_x <= 0:
                    pass
                else:
                    mover_fondo = True
                    dfx = 5


            if event.key == pygame.K_RIGHT:
                jugador.derecha()
                if fondo_x >= 4020 - ancho:
                    pass
                else:
                    mover_fondo = True
                    dfx = -5    
                
            if event.key == pygame.K_UP:
                jugador.saltar()        
        #detenerse            
        if event.type == pygame.KEYUP:
            mover_fondo = False 
            if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
                jugador.stop()
                                
            if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
                jugador.stop()

    listade_todoslos_sprites.draw(screen)
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()






