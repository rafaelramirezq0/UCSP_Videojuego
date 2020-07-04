import pygame, sys
import math
import random 

ancho=800
alto=600

screen=pygame.display.set_mode([ancho,alto])
reloj=pygame.time.Clock()
#colores
blanco=(255,255,255)
negro=(0,0,0)
background=pygame.image.load("Backgrounds/forest_loop.png")
#===========
pygame.init()

listade_todoslos_sprites = pygame.sprite.Group()
#------------------------------------------------------------------------------
#Tipo de letra
tipo_letra = pygame.font.Font('freesansbold.ttf', 28)
vidas= 1000

#               ENEMIGO RAT !!!
#
#Enemigo (rat)
enemigo_rat= pygame.image.load("Sprites/rat/rat_idle.png")

#mover al raton
pos_rat_x= 800//2-(enemigo_rat.get_size()[0]//2)
pos_rat_y= 600-(enemigo_rat.get_size()[1])
rat_size= enemigo_rat.get_size()
rat_mov_x = 3

#               ENEMIGO SPIDER !!!
#
enemigo_spider=pygame.image.load("Sprites/spider/idle1.png")
'''
enemigo_spider2=pygame.image.load("game/idle1.png")
enemigo_spider3=pygame.image.load("game/idle1.png")
enemigo_spider4=pygame.image.load("game/idle1.png")
'''
pos_spider_x= random.randint(0,800)
pos_spider_y= random.randint(0,600)
spider_size= enemigo_spider.get_size()
spider_mov_y=3  #cae del cielo 

#Funciones 

def rat(x,y):
    screen.blit(enemigo_rat,(x,y))

def spider(x,y):
    screen.blit(enemigo_spider,(x,y))

def mostrar_vidas(x,y):
    vidas_render =  tipo_letra.render("Vidas : "+ str
    (vidas), True, (255,255,255))
    screen.blit(vidas_render,(x,y))

def hubo_colision(x1,x2,y1,y2):
    distancia = math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
    return True if distancia < 80 else False

def game_over(x,y):
    imprimir= tipo_letra.render("GAME OVER ", True, (255,255,255))
    screen.blit(imprimir,(x,y))

#------------------------------------------------------------------------------
#Jugador (o sea el perrito)
run1=pygame.image.load("Sprites/dog/run1.png")
run2=pygame.image.load("Sprites/dog/run2.png")
run3=pygame.image.load("Sprites/dog/run3.png")
run4=pygame.image.load("Sprites/dog/run4.png")
run5=pygame.image.load("Sprites/dog/run5.png")
run6=pygame.image.load("Sprites/dog/run6.png")
run7=pygame.image.load("Sprites/dog/run7.png")
run1i=pygame.transform.flip(run1,True,False)
run2i=pygame.transform.flip(run2,True,False)
run3i=pygame.transform.flip(run3,True,False)
run4i=pygame.transform.flip(run4,True,False)
run5i=pygame.transform.flip(run5,True,False)
run6i=pygame.transform.flip(run6,True,False)
run7i=pygame.transform.flip(run7,True,False)
run=[run1,run2,run3,run4,run5,run6,run7]
run_inv=[run1i,run2i,run3i,run4i,run5i,run6i,run7i]
runs=[run,run_inv]
#Atacado
hurt1=pygame.image.load("Sprites/dog/hurt1.png")
hurt2=pygame.image.load("Sprites/dog/hurt2.png")
hurt3=pygame.image.load("Sprites/dog/hurt3.png")

hurt1i=pygame.transform.flip(hurt1,True,False)
hurt2i=pygame.transform.flip(hurt2,True,False)
hurt3i=pygame.transform.flip(hurt3,True,False)

hurt=[hurt1,hurt2,hurt3]
hurt_inv=[hurt1i,hurt2i,hurt3i]
hurts=[hurt,hurt_inv]
#Muere
dead1=pygame.image.load("Sprites/dog/dead1.png")
dead2=pygame.image.load("Sprites/dog/dead2.png")
dead3=pygame.image.load("Sprites/dog/dead3.png")
dead4=pygame.image.load("Sprites/dog/dead4.png")
dead1i=pygame.transform.flip(dead1,True,False)
dead2i=pygame.transform.flip(dead2,True,False)
dead3i=pygame.transform.flip(dead3,True,False)
dead4i=pygame.transform.flip(dead4,True,False)
dead=[dead1,dead2,dead3,dead4]
dead_inv=[dead1i,dead2i,dead3i,dead4i]
dies=[dead,dead_inv]
plataformas=pygame.Rect(300,520,120,15)
#------------------------------------------------------------
#Atacado
hurt1=pygame.image.load("Sprites/dog/hurt1.png")
hurt2=pygame.image.load("Sprites/dog/hurt2.png")
hurt3=pygame.image.load("Sprites/dog/hurt3.png")

hurt1i=pygame.transform.flip(hurt1,True,False)
hurt2i=pygame.transform.flip(hurt2,True,False)
hurt3i=pygame.transform.flip(hurt3,True,False)

hurt=[hurt1,hurt2,hurt3]
hurt_inv=[hurt1i,hurt2i,hurt3i]
hurts=[hurt,hurt_inv]
#Muere
dead1=pygame.image.load("Sprites/dog/dead1.png")
dead2=pygame.image.load("Sprites/dog/dead2.png")
dead3=pygame.image.load("Sprites/dog/dead3.png")
dead4=pygame.image.load("Sprites/dog/dead4.png")
dead1i=pygame.transform.flip(dead1,True,False)
dead2i=pygame.transform.flip(dead2,True,False)
dead3i=pygame.transform.flip(dead3,True,False)
dead4i=pygame.transform.flip(dead4,True,False)
dead=[dead1,dead2,dead3,dead4]
dead_inv=[dead1i,dead2i,dead3i,dead4i]
dies=[dead,dead_inv]
plataformas=pygame.Rect(300,520,120,15)

#------------------------------------------------------------
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
        self.image = pygame.image.load("Sprites/dog/run1.png")
        self.image = runs[self.direc][self.imagen]
        # rectángulo que ocupa
        self.rect = self.image.get_rect()
    #esto efectúa el movimiento, va "actualizando" la velocidad
    #esto efectúa el movimiento, va "actualizando" la velocidad e imagen
    def update(self):
        self.gravity()
        #moverse
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #animación
        self.imagen += self.cambio
        if self.imagen > len(run)-1 or self.speed_x==0:
            self.imagen = 0
        if self.speed_y!=0:
            self.imagen = 5
        self.image=runs[self.direc][self.imagen]
        #falta aquí chocar (o sea, poner lo que pasa si choca)   
    #gravedad
    def gravity(self):
        if self.speed_y == 0:
            self.speed_y = 5
        else:#aceleración de la gravedad
            self.speed_y += 0.35
        #tocar el suelo
        if self.rect.y >= 600 - self.rect.height and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = 600 - self.rect.height
        #paredes
        if self.rect.right >=800:
            self.rect.x = 800 - self.rect.width
        if self.rect.left <=0:
            self.rect.x = 0

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
    
jugador=Player()
listade_todoslos_sprites.add(jugador)
done=False
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height
while not done:
    screen.fill(blanco)
    screen.blit(background,(0,0))
    jugador.update()
    
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            done=True
        #movimiento del perrito
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                jugador.izquierda()

            if event.key == pygame.K_RIGHT:
                jugador.derecha()
                

            if event.key == pygame.K_UP:
                jugador.saltar()

                
        #detenerse            
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
                jugador.stop()
                                
            if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
                jugador.stop()
                
#-------------------------------------------------------------------------------
    #poner rat y spider 
    pos_rat_x -= rat_mov_x
    pos_spider_y+=spider_mov_y 
    
    rat(pos_rat_x,pos_rat_y)
    spider(pos_spider_x,pos_spider_y)

    #PARA EL MOVIMIENTO DE LA RAT
    #izquierda
    if pos_rat_x <= 0:
        rat_mov_x = -3
    #derecha
    elif pos_rat_x >= ancho- rat_size[0]:
        rat_mov_x = 3

    #PARA EL MOVIMIENTO DE LA SPIDER
    #cuando choca arriba
    if pos_spider_y <= 0:
        spider_mov_y = 3
    #cuando choca abajo 
    elif pos_spider_y >= random.randint(400, alto):#alto- spider_size[0]:
        spider_mov_y = -3

    #Mostrar las vidas del perrito
    if vidas > 0:
        mostrar_vidas(10,10)
    elif vidas <=0:
        game_over(10,10)
    #Colision rat y perrito
    colision_con_rat = hubo_colision(pos_rat_x,jugador.rect.x,pos_rat_y,jugador.rect.y)
    if colision_con_rat:
            vidas -=1
    #Colision spider y perrito
    colision_con_spider=hubo_colision(pos_spider_x,jugador.rect.x,pos_spider_y,jugador.rect.y)
    if colision_con_spider:
            vidas -=3
#-------------------------------------------------------------------------------

    
    
    listade_todoslos_sprites.draw(screen)

    pygame.display.flip()
    reloj.tick(60)
    pygame.display.update()
pygame.quit() 
reloj.tick(50)
pygame.quit()