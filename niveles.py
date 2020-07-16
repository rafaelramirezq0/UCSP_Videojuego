import pygame, sys
import time
import random
from game_intro import *
from jugador import *
from enemigos import *
from plataformas import *
pygame.init()
pygame.mixer.init()
pygame.init()

#Constante
ancho= 800
largo = 600

pygame.display.set_caption("Doggo Adventure")
pygame.display.set_icon(pygame.image.load("game/Sprites/icon.png"))
screen = pygame.display.set_mode((ancho,largo))
reloj = pygame.time.Clock()
listade_todoslos_sprites = pygame.sprite.Group()

# Estado del Juego
Intro1 = False
Intro2 = False
Tutorial = False
Juego = True

# Fondos Niveles
bosque_fondo_lv1 = pygame.image.load("game/Backgrounds/nivel1_x3.png").convert()
bosque_fondo_lv2 = pygame.image.load("game/Backgrounds/nivel2_x3.png").convert()
bosque_fondo_lv3 = pygame.image.load("game/Backgrounds/nivel3_x4.png").convert()
fondos=[bosque_fondo_lv1,bosque_fondo_lv2,bosque_fondo_lv3]
fondo_x = 0
espacio = bosque_fondo_lv1.get_rect().width
paredes = [fondo_x,fondo_x+espacio]
pos_ini= 0

enemigo_rat= pygame.image.load("game/Sprites/rat/rat_idle.png")
enemigo_rat_inv= pygame.transform.flip(enemigo_rat,True,False)
rats=[enemigo_rat,enemigo_rat_inv]

enemigo_spider=pygame.image.load("game/Sprites/spider/idle1.png")
enemigo_spider2=pygame.image.load("game/Sprites/spider/idle2.png")
enemigo_spider3=pygame.image.load("game/Sprites/spider/idle3.png")
enemigo_spider4=pygame.image.load("game/Sprites/spider/idle4.png")
spiders=[enemigo_spider,enemigo_spider2,enemigo_spider3,enemigo_spider4]

car_plat1=[[150,40,200,220],[150,40,600,450],[100,30,400,350],[150,40,1000,450],[100,30,1200,350],
[100,30,1400,220],[150,40,2600,450],[100,30,2800,350],[150,40,3000,220],[100,30,3500,220]]
car_plat2=[[150,40,200,220],[150,40,600,450],[100,30,400,350],[150,40,1000,450],[100,30,1200,350],
[100,30,1400,220],[150,40,2600,450],[100,30,2800,350],[150,40,3000,220],[100,30,3500,220]]
car_plat3=[[150,40,200,220],[150,40,600,450],[100,30,400,350],[150,40,1000,450],[100,30,1200,350],
[100,30,1400,220],[150,40,2600,450],[100,30,2800,350],[150,40,3000,220],[100,30,3500,220]]
car_plats=[car_plat1,car_plat2,car_plat3]

def escribir_plataformas(nivel):
    plataformas=pygame.sprite.Group()
    for caract in car_plats[nivel-1]:
        plat=Plataforma(caract[0],caract[1],caract[2],caract[3])
        plataformas.add(plat)
    return plataformas

def escribir_ratas(nivel):
    enemigos_rata = pygame.sprite.Group()
    for r in range(nivel*3):
        rat=Rat(rats,4,paredes)
        rat.rect.x=random.randint(0,espacio-rat.rect.width)
        rat.rect.y=600-(rat.size[1])
        enemigos_rata.add(rat)
    return enemigos_rata

def escribir_arañas(nivel):
    enemigos_spider=pygame.sprite.Group()
    for s in range(nivel*4):
        spider=Spider(spiders,3)
        spider.rect.x= random.randint(0,espacio-spider.rect.width)
        spider.rect.y= random.randint(0,399)
        enemigos_spider.add(spider)
    return enemigos_spider

def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col

def mostrar_vidas(x,y):
    vidas_render =  tipo_letra1.render("Vidas : "+ str
    (vidas), True, blanco)
    screen.blit(vidas_render,(x,y))

def game_over(x,y):
    imprimir= tipo_letra2.render("GAME OVER ", True, blanco)
    screen.blit(imprimir,(x,y))

def win(x,y):
    imprimir= tipo_letra2.render("YOU WIN ", True, blanco)
    screen.blit(imprimir,(x,y))

# Sonidos
def load_intro():
    pygame.mixer.music.load("game/Sounds/title02.mp3")
    pygame.mixer.music.play(-1)
def unload_music():
    pygame.mixer.music.stop()  
def load_level1():
    pygame.mixer.music.load("game/Sounds/nivel_01.mp3")
    pygame.mixer.music.play(-1)
if Intro1 == True:
    pygame.mixer.music.load("game/Sounds/title02.mp3")
    pygame.mixer.music.play(-1)
elif Juego == True:
    pygame.mixer.music.load("game/Sounds/nivel_01.mp3")
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
                Juego = True
    

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
                Juego = True


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
                Juego = True
    
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
                Juego = True

    pygame.display.update()
    pygame.display.flip()
    reloj.tick(60)

# Nivel1
#JUEGO
while Juego:
    Partida=True
    tipo_letra1 = pygame.font.Font('freesansbold.ttf', 28)
    tipo_letra2 = pygame.font.Font('freesansbold.ttf', 100)
    vidas=1000
    nivel=1
    while Partida:
        Nivel = True
        jugador=Player()
        listade_todoslos_sprites = pygame.sprite.Group()
        jugador.rect.x=0
        jugador.rect.y=600-jugador.rect.height
        mover_fondo = False
        gets_hit = False
        fondo_x = 0
        fondo=fondos[nivel-1]
        plataformas=escribir_plataformas(nivel)
        enemigos_rata=escribir_ratas(nivel)
        enemigos_spider=escribir_arañas(nivel)
        enemigos = pygame.sprite.Group()
        enemigos.add(enemigos_rata,enemigos_spider)
        listade_todoslos_sprites.add(jugador,enemigos,plataformas)
        
        while Nivel == True:

            screen.blit(fondo, [fondo_x,0])
            jugador.update(gets_hit,vidas,plataformas)
            for enemigo in enemigos:
                enemigo.mover()
            for rat in enemigos_rata:
                rat.paredes = [fondo_x,fondo_x+espacio]
            if vidas >0:
                if mover_fondo == True or jugador.speed_x!=0:
                    fondo_x += dfx
                    for plat in plataformas:
                        plat_movimiento=False
                        if ancho-espacio+plat.x_inicial<=plat.rect.x+dfx<=plat.x_inicial:
                            plat_movimiento=True
                            plat.mover(dfx)
                    for enemy in enemigos:
                        if plat_movimiento==True:
                            enemy.rect.x += dfx
                if fondo_x <= ancho-espacio or fondo_x >=0:
                    mover_fondo = False
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    Juego=False
                    Nivel=False
                    Partida=False
                #mover_fondo = False
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
                    if event.key == pygame.K_SPACE:
                        jugador.ataque()        
                #detenerse            
                if event.type == pygame.KEYUP:
                    mover_fondo = False
                    if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
                        jugador.stop()              
                    if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
                        jugador.stop() 

            if fondo_x >= 0:
                fondo_x = 0
            
            if fondo_x <= -1*espacio + ancho:
                fondo_x = -1*espacio + ancho
            
            if vidas > 0:
                mostrar_vidas(10,10)
            elif vidas <=0:
                game_over(100,250)
                jugador.die()

            for spider in enemigos_spider:
                if checkCollision(spider,jugador)==True and spider in listade_todoslos_sprites:
                    if jugador.imagen!=7:#imagen cuando está atacando
                        gets_hit=True
                        vidas-=1
                        if vidas>0:
                            jugador.get_hurt()
                    else:
                        enemigos.remove(spider)
                        listade_todoslos_sprites.remove(spider)
                else:
                    gets_hit=False

            for rat in enemigos_rata:
                if checkCollision(rat,jugador)==True and rat in listade_todoslos_sprites:
                    if jugador.imagen!=7:
                        gets_hit=True
                        vidas-=3
                        if vidas>0:
                            jugador.get_hurt()
                    else:
                        enemigos.remove(rat)
                        listade_todoslos_sprites.remove(rat)
                else:
                    gets_hit=False

            if len(enemigos)==0:
                nivel+=1
                if nivel>3:
                    win(180,260)
                else:
                    Nivel=False
                

            listade_todoslos_sprites.draw(screen)
            pygame.display.flip()
            reloj.tick(60)

pygame.quit()